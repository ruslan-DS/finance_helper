EXTRACT_TOPIC_SYSTEM_PROMPT = """Проанализируй пользовательское сообщение и определи к какой тематике подходит данное сообщение.
Выбери подходящую тематику из следующего списка: акции, облигации, золото, нефть, криптовалюта, другое. Если тема не подходит ни под одну категорию, укажи тематику - "другое".
Сообщение может подходить только к одной единственной тематике, выбирай ту, к которой по-твоему мнению пользовательский запрос больше всего подходит.
Ответ выдай строго одной строкой названия тематики из списка выше без лишних символов и формулировок:"""