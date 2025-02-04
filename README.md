# Анализ финансовых новостей и их влияния на фондовый рынок

# Описание проекта
Проект предназначен для анализа финансовых новостей и определения их влияния на различные финансовые инструменты, такие как акции, облигации, золото, нефть и криптовалюты. Проект построен на основе LLM-Driven решения, используя RAG для извлечения релевантных новостей и генерации объяснений причинно-следственных связей по запросу пользователя.

# Структура проекта:
<pre>
project/                                           # Корень проекта        
        ├── benchmark/                             # Директория с бенчмарком         
            ├── finance_helper_benchmark.ipynb     # Ноутбук с оценкой модели и пайплайна        
        │── notebooks/                             # Директория со всеми экспериментами и прототипированием пайплайнов        
            ├── data/                              # Внутренняя директория с данными в формате .csv, .json и etc.       
                ├── contextual_dataset.json        # Первая версия предобработанного датасета с новостям      
                ├── contextual_dataset_v2.json     # Вторая версия (более актуальная) предобработанного датасета с новостям       
                ├── data.tsv                       # Датасет с финансовыми новостями      
                ├── merged_news_dataset.csv        # Объединенный датасет с финансовыми новостями из всех поддерживаемых источников      
            ├── cleaned_dataset.ipynb              # Ноутбук с процессом предобработки датасета    
            ├── create_contextual_chunks.ipynb     # Ноутбук с реализацией Contextual-Retrieval новостей из датасет    
            ├── create_embeddings_and_db.ipynb     # Ноутбук с векторизацией датасета и сохранением в Векторную БД      
            ├── get_embeddings_test.ipynb          # Ноутбук с примеров получения эмбеддингов текстов      
            ├── merge_datasets.ipynb               # Ноутбук с процессом объединения датасетов из поддерживаемых источников      
        │── src/                                   # Директория бэкенда проекта       
            ├── chroma/                            # Векторная БД      
            ├── llm/                               # Директория с кодом для работы с LLM     
                ├── inference.py                   # Основной функционал вызова LLM      
                ├── llm_client.py                  # Инициализация клиента API LLM      
            ├── prompts/                           # Директория с промптами для всех вызовов LLM     
            └── retrieval/                         # Эталонные ответы     
                ├── base_retrieval.py              # Основной функционал вызова Retrieval-части     
                ├── embeddings.py                  # Код с процессом векторизации текста     
                ├── encoder_client.py              # Инициализация клиента API Encoder-модели     
                ├── similarity.py                  # Запуск поиска релевантных чанков из Векторной БД     
        ├── requirements.txt                       # Зависимости           
        ├── front.py                               # Код с фронт-ендом   
        ├── FinanceHelper.pdf                      # PDF-презентация проекта
        └── .gitignore                             # Конфигурация игнорирований ненужных файлов      
README.md                                          # Документация        
</pre>

# Основной функционал:

### Retrieval-часть:
- Определение тематики запроса через LLM из следующего списка: [акции, облигации, золото, нефть, криптовалюта, другое] для дальнейшей фильтрации подходящих новостей.
- Поиск релевантных новостей к запросу пользователя, используя предобработанные новостные данные с 2021 года по 2024 год (включительно).
- Отобранные новости проходят процесс Contextual-препроцессинга из статьи [Anthropic](https://www.anthropic.com/news/contextual-retrieval).
- Далее контекстуальные куски новостей векторизуются с помощью **GigaChatEmbeddings** и кладутся в Векторную БД **ChromDB**

### Generation-часть:
- Генерация объяснений причинно-следственных связей на основе извлеченных новостей.
- Обеспечение согласованности и релевантности ответов по конкретному событию.
- В качестве LLM используется **API DeepSeek-V3**.

# Данные:

- Основной датасет содержит ~ 100 000 примеров новостей с 2021 по 2024 год (включительно).
- Векторизованная часть, хранящаяся в векторной БД, содержит более 12 000 примеров новостей.
- Датасет проходил процесс очистки, убирая дубли и маленькие новости (длина, которых меньше 100 символов).

# Оценка качества:

В качестве оценки качества для оценки retrieval и generation частей используется метрика **accuracy**, а также подход **LLM-as-a-Judge**.

### Результаты бенчмарка:

<table>
  <tr>
    <th colspan="2">Retrieval (ACC)</th>
    <th colspan="2">Generation (LLM-as-a-Judge)</th>
  </tr>
  <tr>
    <td>Метрика</td>
    <td>Оценка</td>
    <td>Метрика</td>
    <td>Оценка</td>
  </tr>
  <tr>
    <td>Определение топика</td>
    <td>1.0</td>
    <td>Согласованность генерации</td>
    <td>0.43</td>
  </tr>
  <tr>
    <td>Поиск релевантных чанков</td>
    <td>0.47</td>
    <td>Nan</td>
    <td>Nan</td>
  </tr>
</table>

# Установка и настройка

**Требования:** 
- Python 3.9 или выше
- Установленные зависимости из **requirements.txt**

### Установка
1. **Клонируйте репозиторий:**
```
git clone git@github.com:ruslan-DS/finance_helper.git
cd finance_helper
```

2. **Установите зависимости:**
```
pip install -r requirements.txt
```

3. **Настройте API-ключи к используемым моделям**:
Создайте файл .env в корне проекта и добавьте туда ваши API-ключи:
```
DEEPSEEK_API_KEY=ваш_api_ключ
GIGACHAT_API_KEY=ваш_api_ключ
```

# Запуск сервиса:

1. Перейдите в папку проекта:
```
cd finance_helper/project
```

2. Запустите streamlit-сервер:
```
streamlit run front.py
```

3. Откройте браузер и перейдите по адресу:
```
http://localhost:8501
```

# Контакты:
Автор: Волощенко Руслан     
Email: ruslanvolo9@gmail.com   
GitHub: ruslan-ds   
