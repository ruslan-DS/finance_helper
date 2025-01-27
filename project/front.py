import streamlit as st
from datetime import date
from src.llm.inference import get_predict


def main():
    st.set_page_config(page_title="Финансовый помощник", layout="wide")

    st.title("Финансовый помощник")
    st.info("""**Финансовый помощник** поможет вам проанализировать, случившиеся события на фондовом рынке, 
    находя причинно-следственные связи между изменениями состояния активов и новостями. 
    Используйте помощника, чтобы разобраться в том, что влияет на рынок, 
    чтобы в будущем правильно реагировать на мировые изменения.""")

    with st.sidebar:
        st.header("Настройки")

        st.info('Для корректного ответа выберите подходящий год')
        start_date = st.date_input("Выберите год начала анализа (месяц и день не важны):", value=date(2024, 12, 31), min_value=date(2021, 1, 1), max_value=date(2024, 12, 31))

    query = st.text_input("Введите ваш запрос:", placeholder="Например: Почему нефть подорожала?")

    if st.button("\u23f3 Построить анализ события"):
        if not query:
            st.warning("Пожалуйста, введите запрос.")
        else:
            with st.spinner("Анализируем данные... Пожалуйста, подождите."):
                response = get_predict(query, start_date)

                st.subheader("Ответ модели:")
                with st.chat_message("assistant"):
                  st.markdown(f'**{response}**')
    else:
        with st.expander("Примеры запросов"):
            st.markdown("""
            - Почему акции Газпрома выросли?
            - Какие события повлияли на курс рубля?
            - Что вызвало рост золота?
            """)

if __name__ == "__main__":
    main()
