import streamlit as st
from datetime import date, timedelta
from src.llm.inference import analyze_query

def main():
    st.set_page_config(page_title="Финансовый помощник", layout="wide")

    st.title("Финансовый помощник")
    st.info("""
    **Финансовый помощник** поможет вам проанализировать, случившиеся события на фондовом рынке, 
    находя причинно-следственные связи между изменениями цен активов и новостями. 
    Используйте помощника, чтобы разобраться в том, что влияет на рынок, 
    чтобы в будущем правильно реагировать на мировые изменения.
    """)

    with st.sidebar:
        st.header("Настройки")

        MAX_DAYS = 30
        today = date.today()
        end_date = today - timedelta(days=MAX_DAYS)
        
        st.info('Для выбора доступны новости, которым не более 30 дней!')
        start_date = st.date_input("Выберите дату начала анализа (ограничение в 30 дней):", end_date, min_value=end_date, max_value=today)

        # INVEST_TOOLS = ['Акции', 'Золото', 'Облигации', 'Нефть']
        # STOCKS = ['Сбер', 'Яндекс', 'Газпром', 'Норникель', 'РЖД']
        # selected_invest_tool = st.selectbox('Выберите любой инвестиционный инструмент из списка:', options=INVEST_TOOLS)

        # if selected_invest_tool == 'Акции':
        #    st.info('Количество акций пока ограничено, но мы расширяем список, чтобы вам было комфортно :)')
        

    query = st.text_input("Введите ваш запрос", placeholder="Например: Почему нефть подорожала?")

    if st.button("\u23f3 Построить анализ события"):
        if not query:
            st.warning("Пожалуйста, введите запрос.")
        else:
            with st.spinner("Анализируем данные... Пожалуйста, подождите."):
                response = analyze_query(query, start_date)
                
                st.subheader("Ответ модели:")
                with st.chat_message("assistant"):
                   st.markdown(f'**{response}**')
    else:
        with st.expander("Примеры запросов"):
            st.markdown("""
            - Почему акции Сбера выросли?
            - Какие события повлияли на курс рубля?
            - Что вызвало рост золота?
            """)

if __name__ == "__main__":
    main()
