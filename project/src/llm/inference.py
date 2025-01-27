from datetime import date
from src.llm.llm_client import llm_client
from src.prompts.base_prompt import BASE_SYSTEM_PROMPT
from src.retrieval.base_retrieval import launch_retrieval


def get_predict(query: str, select_date: date) -> str:
    """Функция вызова и исполнения GigaChat """

    context = launch_retrieval(query, select_date)
    system = BASE_SYSTEM_PROMPT.format(context=context)

    message = [
        {'role': 'system', 'content': system},
        {'role': 'user', 'content': query}
    ]

    response = llm_client.chat.completions.create(
        model="deepseek-chat",
        messages=message,
        stream=False
    ).choices[0].message.content

    return response
