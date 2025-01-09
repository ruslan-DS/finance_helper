from langchain_gigachat.chat_models import GigaChat
from src.llm.prompts import SYSTEM
from src.retrieval.searching_scripts import launch_retrieval

giga_verify_dir = r'C:\Users\22533995\Desktop\llm_project\src\llm\verify'
giga = GigaChat(
    base_url = "https://gigachat-ift.sberdevices.delta.sbrf.ru/v1",
    cert_file = f"{giga_verify_dir}\server-sberca-cert.pem",
    key_file = f"{giga_verify_dir}\server-sberca-key.key",
    verify_ssl_certs = False,
    model = "GigaChat-Max",
    profanity_check = False,
    streaming = False,
    top_p = 0,
    timeout = 120
)

def analyze_query(query, start_date, system=SYSTEM):
    """Функция вызова и исполнения GigaChat"""

    ### go to retrieval
    context = launch_retrieval(query)
    system = system.format(context=context)

    message = [
        {'role': 'system', 'content': system},
        {'role': 'user', 'content': query}
    ]

    response = giga.invoke(message).content

    return response