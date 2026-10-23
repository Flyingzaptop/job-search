

======== FILE: C__Users_r3d_flzp_Desktop_manualCV_GITHUB_PORTFOLIO.md ========

# GitHub-портфолио Denis Gruszkiewicz

Проверено 14.10.2026: https://github.com/Flyingzaptop. Полный публичный список: 14 репозиториев. Проверены деревья default branches, README, конфигурации и выбранные реализации/тесты. Все деревья получены без truncation. Это обзор всех проектов, не построчный аудит всего кода, не запуск тестов и не проверка всех исторических веток.

Снимок доказательств: `sources/github/2026-10-14/`. `inventory.json` содержит default branch, commit SHA, число файлов, пути первоначально выбранных источников; `tree.json` в каждом проекте содержит полное дерево. Подкаталог `files/` хранит исходники для повторного разбора. Дополнительные файлы кода также скачаны и находятся в `files/`.

## Как использовать при подготовке CV

- Читать вместе с PROFILE_BASE.md перед каждой адаптацией. Этот обзор уточняет старые записи базы.
- Наличие библиотеки в dependencies не равно глубокой практике: выбирать claim по реализованному коду и задаче проекта.
- Разделять большие собственные проекты, академические задания, концепты и планы. Учебные репозитории с одинаковыми notebook не считать разными коммерческими проектами.
- Свежие метрики из отчёта имеют дату и границы проверки; не выдавать их за повторно измеренные сегодня.
- Не выводить стаж работы, промышленное внедрение, личную долю чужого кода или уровень senior из объёма репозитория.
- CI подтверждён в нескольких проектах; continuous deployment не следует автоматически из CI.

## 1. jobhunter-n8n — Node.js, workflow automation и LLM applications

https://github.com/Flyingzaptop/jobhunter-n8n

**Задача:** локальная платформа поиска и анализа вакансий с workflow, состоянием в БД, браузерными действиями и human-in-the-loop.

**Подтверждено:**
- Главный backend — JavaScript / Node.js 24, ES modules `.mjs`; не представлять как Python-backend.
- n8n: шесть основных workflow, стадийная оркестрация и очередь задач.
- PostgreSQL: SQL migrations, durable state и данные приложения.
- Ollama, локальные LLM; в package.json также LM Studio SDK. LLM extraction/analysis отделены от deterministic scoring; schema validation через AJV.
- Playwright / Chromium: browser service, adapters для ATS, семантика полей, формы и проверки состояния.
- React / TypeScript dashboard, SSE/live events, авторизация и human review.
- Telegram HITL, durable обработка, ограничения/подтверждения действий.
- Dockerfile и Docker Compose с PostgreSQL, core, browser и n8n; конфигурация контейнерного стека есть, завершённый Docker production rollout README не подтверждает.
- GitHub Actions: Node 24, PostgreSQL service, Chromium, frontend tests/build, Node tests, генерация n8n workflows и контроль git diff.
- Python используется в отдельных helper scripts, например PDF/render и LM Studio helper; не единственный и не основной язык приложения.

**Доказательства:** `package.json`, `docker-compose.yml`, `.github/workflows/ci.yml`, `services/browser-service/server.mjs`, `services/browser-service/ats-adapters.mjs`, `db/migrations/`, `docs/ARCHITECTURE.md`, `docs/REAL_WORLD_READINESS_V2_REPORT.md`, `tests/*.test.mjs`.

**Метрики:** отчёт readiness v2 от 04.10.2026 содержит 13 911 canonical vacancies; 146/146 local PostgreSQL/Chromium regression tests, 12/12 frontend tests, 22/22 UI checks. Это исторический отчёт с разграничением реальных и mock checks, не текущий запуск тестов. Там же status PARTIAL и отсутствие реальных отправок на ту дату. Не писать production-ready автономную подачу на все ATS.

**CV keywords:** Node.js, JavaScript, TypeScript, n8n, workflow orchestration, LLM integration, browser automation, Playwright, PostgreSQL, SQL, Docker Compose, GitHub Actions, CI, React, SSE, human-in-the-loop, schema validation, data provenance, regression testing.

## 2. LabFlow — full-stack workflow и администрирование

https://github.com/Flyingzaptop/LabFlow

- React 19 / TypeScript / Vite, Django 5.2 / DRF, PostgreSQL/SQLite, REST/OpenAPI.
- CSS interfejsu: src/styles.css, style/layout i elementy formularzy; potwierdzone po dodatkowym odczycie przy CV CodeTwo.
- Versioned procedures, образцы и этапы процесса, state transitions, примечания и роль пользователя.
- Server-side permissions/RBAC, sessions, CSRF, throttling, audit log; миграция immutability на уровне БД.
- Ollama client реализован: HTTP requests, ошибки, проверка GPU, streaming chat. Это конкретный LLM integration, а не только пункт в README.
- `faster-whisper` реализован в `backend/apps/core/transcription.py`: local speech-to-text, польский язык, VAD; не TTS.
- RADIUS backend и отдельный FreeRADIUS deployment guide.
- Windows/Ubuntu: Waitress, Gunicorn, Caddy, systemd; install/upgrade, backup/restore документация.
- Backend tests и Vitest frontend; не заявлять текущий PASS без запуска.
- Публичная версия — демонстратор с фиктивными данными; AI опционален, в Linux может быть отключён.

**Доказательства:** `backend/apps/accounts/{backends,permissions,throttles}.py`, `backend/apps/auditlog/`, `backend/apps/core/{ollama,transcription}.py`, `backend/requirements.txt`, `package.json`, `deploy/linux/README.md`, `deploy/radius/README.md`, backend tests.

**CV keywords:** full-stack, Django REST Framework, React, TypeScript, authentication, authorization, RBAC, audit logging, workflow, OpenAPI, PostgreSQL, Linux deployment, speech-to-text, faster-whisper, Ollama, streaming, RADIUS.

## 3. ARC — systems programming и GPU R&D

https://github.com/Flyingzaptop/ARC

- C++/D3D12, CMake/CTest, Windows SDK; Python/PowerShell для экспериментов и harness.
- Observer/interception, resources/dependencies, descriptor/lifetime tracking, barriers и command state.
- GPU attribution, quality/performance experiments, rollback, memory arbitration.
- CPU task discovery, machine-code analysis; capstone/pefile в отдельном benchmark, CPU-to-GPU offload research.
- CI реально описан в `.github/workflows/build.yml`: Windows Debug/Release, CMake/CTest, PowerShell parse checks, renderer integrations; Linux Release CMake/Ninja/CTest.
- GPU/hardware checks не равны Linux/host CI; ограничения каждого measurement сохранять.
- ARC2 runtime IR — архитектура миграции; не всё целевое поведение реализовано.

**Доказательства:** `src/backends/dx12/`, `src/backends/cpu/`, `.github/workflows/build.yml`, `CMakeLists.txt`, `docs/ARC_IMPLEMENTATION_STATUS.md`, `docs/CPU_GPU_OFFLOAD_STATUS.md`, tests.

**CV keywords:** C++, D3D12, GPU profiling, performance analysis, CMake, CTest, GitHub Actions, cross-platform CI, resource lifetime, graphics runtime, memory, benchmarking, Python automation, PowerShell.

## 4. gc-mbo-research — ML, Rust и event-level data engineering

https://github.com/Flyingzaptop/gc-mbo-research

- Python package/CLI и Rust binaries; Databento CME GC MBO/L3, replay и order book reconstruction.
- Conservative FIFO execution simulation, bid/ask и latency/cost stress, causality checks.
- NumPy, Polars, PyArrow, PyTorch; dependency/config и исследовательские ветки с scikit-learn, LightGBM/XGBoost.
- Feature engineering, метрики, walk-forward validation, экспериментальные гипотезы, calibration/stability checks.
- Форматы DBN/Parquet, сжатие zstd в Rust; serialization serde, CLI clap.
- Двадцать experiment folders; агрегированные результаты и методология.
- Текущий README: NO_TRADE; полезная инфраструктура и отвергнутые гипотезы, не подтверждённая прибыльная стратегия.

**Доказательства:** `pyproject.toml`, `rust/gc-mbo/Cargo.toml`, `rust/gc-mbo/src/book.rs`, `src/gc_mbo/`, `scripts/`, `tests/`, `docs/EXPERIMENTS.md`.

**CV keywords:** Python, Rust, Polars, PyArrow, Parquet, Databento, market microstructure, event streams, feature engineering, PyTorch, tree models, walk-forward, causality, backtesting infrastructure, experiment analysis.

## 5. stargazin — offline/online ML pipeline и Rust/PyO3

https://github.com/Flyingzaptop/stargazin

- Parquet ingestion, row-stream normalization, feature engineering, labels, train/valid/test, checkpoints и inference.
- PyTorch; RetNet-lite, CT-LSTM, shared-trunk three-class head, loss functions и margin objectives.
- Dual-clock online packet normalization, manifest согласованности offline/online.
- Rust/PyO3 native extensions: `three_plus_three_stacks_native` и `dualclock_unpacketizer_native`.
- NumPy/Polars/PyArrow, unit/integration/regression tests.
- README metrics относятся к апрелю 2026; не использовать как свежие production показатели.

**Доказательства:** `core/model_files/`, `core/pipeline/`, `online/dualclock_unpacketizer.py`, два Cargo.toml, `ONLINE_OFFLINE_PARITY_MANIFEST.md`, `tests/`.

**CV keywords:** PyTorch, sequence modeling, RetNet, LSTM, losses, feature pipelines, model evaluation, Rust, PyO3, native extensions, online inference, data contracts.

## 6. stargaze-l2-vwap — collectors, streaming, desktop tooling и ML

https://github.com/Flyingzaptop/stargaze-l2-vwap

- Async Python/aiohttp collectors; connectors Binance, OKX, Kraken, Bybit, Coinbase, Bitfinex, Deribit и Hyperliquid.
- Order-book/trade events, sequence handling, reconnect, timestamps, incremental replay и L2/L3 state.
- Append-only `.mrec`: независимые zstd-compressed Parquet frames, checksums, tail recovery после сбоя и immutable snapshots.
- Desktop recorder, disk limits, PyInstaller/build_exe; pystray/Pillow.
- Syncthing и aria2 для sharing, настройка Windows Firewall и background recovery; это проектный scope, не enterprise network administration.
- ML/VWAP исследования, LSTM и policy/REINFORCE эксперименты, причинные split и frozen runtime.
- cTrader API/Protobuf и L2 recorder; paper-only/frozen evaluation, не автоматически live trading.
- GitHub Actions `.github/workflows/tests.yml`: Python 3.12 и pytest.

**Доказательства:** `market_collector/connectors/`, `market_collector/{record_log,writer,sharing,snapshot}.py`, `desktop_recorder.py`, `stargaze_ml/data/`, `stargaze_ml/gold/`, tests и CI.

**CV keywords:** asyncio, aiohttp, streaming ingestion, WebSocket connectors, Parquet, zstd, recovery, checksums, incremental processing, desktop utilities, PyInstaller, cTrader, Protobuf, PyTorch, LSTM, pytest, CI.

## 7. xauusd — свежие ML-эксперименты и причинность

https://github.com/Flyingzaptop/xauusd

- Снимок прогресса README: 09.10.2026; angular representations для XAUUSD.
- PyTorch causal TCN с residual/dilated convolutions; H/C/L multi-output prediction, custom losses и geometry constraints.
- Asynchronous MBO fast branch, learned attention pooling; запрет future events в input проверяется assert и causality tests.
- Chronological walk-forward, distillation, bidirectional infilling/reconstruction и controlled baseline comparison.
- Python/NumPy/Pandas/SciPy/scikit-learn/PyArrow, Databento и Matplotlib; CUDA Torch environment.
- Различать causal forecasting и bidirectional reconstruction: второе использует оба края разрыва и не доказывает forecasting accuracy.
- MBO experiment остановлен в текущем снимке; partial training/smoke checks не означают выигрыш над baseline или прибыльность.

**Доказательства:** `experiments/angular_mbo/{model,prepare,train,test_causality}.py`, `experiments/angular_walkforward/`, `experiments/angular_reconstruction_v2/core.py`, `experiments/angular_infill/`, `requirements.txt`, README.

**CV keywords:** PyTorch, TCN, attention pooling, asynchronous sequences, custom losses, time series, causal validation, leakage checks, chronological evaluation, reconstruction, distillation, experimental design.

## 8. Python-Colab — учебная и исследовательская практика

https://github.com/Flyingzaptop/Python-Colab

- Jupyter/Colab notebooks: NumPy/Pandas, plotting, regression и pipelines.
- scikit-learn: ColumnTransformer, Pipeline, SimpleImputer, OneHotEncoder, LinearRegression, train_test_split и метрики.
- NLP: NLTK tokenization, stemming, lemmatization, stopwords; TF-IDF + TruncatedSVD + SVC text classification.
- PyTorch Dataset/DataLoader, training и neural classification/regression exercises.
- Hugging Face Transformers `pipeline('text-generation', model='mistralai/Mistral-7B-Instruct-v0.2')` в notebook с названием langchain.
- Название `Практика + Домашня langchain.ipynb` не подтверждает LangChain: в просмотренном коде используется Transformers, не LangChain/LangGraph/RAG.
- `depthds_features.ipynb`: NumPy/Pandas/Matplotlib для анализа depth features.

**CV keywords:** academic hands-on NLP, NLTK, scikit-learn, TF-IDF, SVM, preprocessing pipelines, Jupyter, Colab, Transformers, text generation, PyTorch.

## 9. Statystyka-Inzynierska — академическая подборка notebooks

https://github.com/Flyingzaptop/Statystyka-Inzynierska

- Во многом та же учебная коллекция, что Python-Colab: preprocessing/regression, NumPy/Pandas, PyTorch, NLTK и text classification.
- Польские пояснения для академической работы; не считать вторым независимым software продуктом.
- Практика Transformers тоже есть; LangChain не доказывается именем notebook.

## 10. MultiNeuro — небольшой AI Telegram bot

https://github.com/Flyingzaptop/MultiNeuro

- Python, pyTelegramBotAPI/telebot, OpenAI ChatCompletion API, gpt-3.5-turbo.
- NLTK/sentence splitting, handlers и ответы в Telegram.
- Исторический компактный проект; не современная multi-agent платформа и не cloud production evidence.
- Основная реализация: `multineuro v.1.0.py`.

## 11. Project1_Informatyka_III — C++ OOP / Harmonogram

https://github.com/Flyingzaptop/Project1_Informatyka_III

- Академическое консольное приложение с классами Czas и Harmonogram.
- Constructors/overloads, operator overloading, copy constructor/assignment/destructor, dynamic array, aggregation и меню.
- Прямое свидетельство OOP C++, manual memory management и объяснения кода.
- Не смешивать с отдельной профессиональной системой управления графиками: публичный репозиторий — учебный проект.
- Доказательства: `Project1/{Czas,Harmonogram}.{h,cpp}`, `Project1/Project1.cpp`.

## 12. mark — теоретические заметки, не приложение

https://github.com/Flyingzaptop/mark

- Только `questions.md`: PCB types/substrates, SMT/THT/COB, soldering, thermal systems, heatsinks, connectors/AWG и другие технические темы.
- Может подтверждать учебное знакомство с electronics/thermal topics, но не изготовление PCB, схемотехнику или коммерческое hardware design.

## 13. kr — базовый Python exercise

https://github.com/Flyingzaptop/kr

- `main.py`: проверка простого числа до sqrt(n), input/output.
- Не отдельный значимый CV project; учитывается в полноте инвентаризации.

## 14. tast — базовый Python/file exercise

https://github.com/Flyingzaptop/tast

- `main.py`: чтение файла, split, max(words,key=len), обработка FileNotFoundError.
- Не доказательство Java/Go/Ruby: их названия в input.txt — строки данных, не используемые языки.
- Не отдельный значимый CV project.

## Сводная карта навыков для keywords

| Направление | Навыки и доказательные проекты |
|---|---|
| Web/backend | Python/Django/DRF, React/TypeScript, REST/OpenAPI — LabFlow; Node.js/JavaScript, PostgreSQL, SSE — JobHunter |
| Automation | n8n, Playwright, browser adapters, durable workflows — JobHunter; Python/PowerShell tooling — ARC/collectors |
| LLM/GenAI | Ollama/LM Studio, schema-constrained analysis — JobHunter; streaming Ollama + STT — LabFlow; OpenAI Telegram — MultiNeuro; Transformers — notebooks |
| Data engineering | asyncio/aiohttp, stream connectors, Polars/PyArrow/Parquet, zstd, recovery — stargaze; MBO/DBN/Rust — gc-mbo |
| ML/research | PyTorch, feature/label/loss design, RetNet/LSTM/TCN, attention, walk-forward/causality — stargazin/stargaze/xauusd/gc-mbo |
| NLP (учебная практика) | NLTK, TF-IDF, SVD, SVM, Transformers — Python-Colab/Statystyka |
| Native/performance | C++/D3D12/CMake/CTest — ARC; Rust/PyO3 — stargazin; Rust replay — gc-mbo |
| CI/testing | GitHub Actions — ARC, JobHunter, stargaze; Node tests, pytest, Vitest, CTest; Docker Compose configuration — JobHunter |
| Auth/admin | RBAC, audit, session/CSRF, RADIUS, Ubuntu/systemd/Caddy — LabFlow |
| Engineering | CAD/RobotStudio/mechanics — пользователь и CV; публичные репозитории не заменяют CAD portfolio |

## Границы, которые остаются актуальными

RAG/vector search, LangGraph и законченные LangChain applications не подтверждены. AWS/GCP enterprise services и completed Azure production deployment не подтверждены. SAP/ERP implementation, PHP, Inventor и промышленный mechanical стаж не следуют из публичного GitHub. Java/Android остаются подтверждением пользователя, а не просмотренного публичного кода.

## Что исправлено относительно старой базы

JobHunter больше не пропускать и не приписывать ему Python как основной язык. Docker/Compose и CI подкреплены конкретными файлами, но deployment readiness PARTIAL. Добавлены Node.js, n8n, Playwright, SSE, Polars/PyArrow, streaming collectors/recovery, Rust/PyO3, Hugging Face Transformers, учебный NLP/scikit-learn, speech-to-text и RADIUS. Учтены xauusd и все маленькие репозитории без раздувания их масштаба.


======== FILE: C__Users_r3d_flzp_Desktop_manualCV_PROFILE_BASE.md ========

# Denis Gruszkiewicz — база для CV

Дата актуализации: 14.10.2026. Это рабочая база, а не готовое CV для отправки.

Актуальный полный обзор всех 14 публичных репозиториев: [GITHUB_PORTFOLIO.md](GITHUB_PORTFOLIO.md). Перед адаптацией каждого CV читать эту карту вместе с базой; детали этого обзора уточняют прежние неполные записи. Исходники/деревья/commit SHA сохранены в sources/github/2026-10-14/.

Ключевые дополнения после просмотра кода: Node.js/JavaScript backend JobHunter; n8n, Playwright, Docker Compose, SQL migrations, React/SSE, GitHub Actions CI; streaming collectors asyncio/aiohttp и Parquet/zstd; Polars/PyArrow, Rust/PyO3; scikit-learn/NLTK/Transformers notebooks; local faster-whisper STT, streaming Ollama и RADIUS в LabFlow; свежий xauusd TCN/attention/causality R&D.

## Контакты

- Имя для всех CV: Denis Gruszkiewicz.
- Единственный email для новых CV и сопроводительных писем: r3dflzp.ns@gmail.com.
- Телефон из прежних CV: +48 511 592 887.
- Город из прежних CV: Wrocław, Polska.
- GitHub: https://github.com/Flyingzaptop.
- Сайт собственной инициативы: https://antillia.tech/.
- Польское гражданство — указано в прежних CV.
- В сертификате исходное имя Denys Hrushkevych; сертификат не переименовывать и не исправлять.

## Подтверждённые пользователем обновления

- Продолжает работать в ZOZ w Bolesławcu. Начало по CV: 06.2025. На 14.10.2026 — около 1 года 4 месяцев опыта.
- Politechnika Wrocławska: окончен V семестр. Не выводить номер текущего семестра из календаря.
- WSB Merito: учится на II семестре.
- Управление сотрудниками, лаборатория и управление графиками — три отдельных проекта.
- Приложение для сотрудников передано/продано; исходники не доступны для публичной демонстрации.
- LabFlow — отдельный лабораторный проект, публичный репозиторий.
- ARC / Adaptive Runtime Core — отдельный собственный проект.
- Начинает вместе с другими развивать Antillia; сайт уже существует, проект на раннем этапе.
- Текущая работа, по сообщению пользователя, предполагается до конца 2026 года. Это внутренний контекст, не формулировка для CV.
- Возможен более ранний переход к новому работодателю; точную дату начала согласовывать. Не писать безусловное «доступен немедленно».

## Профессиональный опыт

### Młodszy Administrator IT — ZOZ w Bolesławcu

06.2025 – obecnie. Точное официальное название должности берётся из прежнего CV; при необходимости уточнить.

- Поддержка сотрудников и диагностика аппаратных, системных и прикладных проблем.
- Подключение и настройка рабочих мест, сетевых устройств и switch; LAN-кабели и базовая диагностика сети.
- Создание внутренних инструментов для сокращения повторяющихся ручных действий.
- Анализ рабочих процессов, тестирование сценариев, воспроизведение ошибок и исправление приложений.
- Разработка отдельных приложений для сотрудников, лабораторных процессов и графиков.
- Нет подтверждённых чисел пользователей, часов экономии или процентов улучшения; не придумывать.

## Реестр проектов

### JobHunter и CI — уточнение пользователя 14.10.2026

- Пользователь предоставил сводку истории: JobHunter — n8n, PostgreSQL, Ollama (qwen3.5:4b), Playwright/Chromium, Docker/local services, Telegram HITL, React dashboard/SSE, автоматический сбор и анализ вакансий, GitHub Actions CI и тестирование; Greenhouse/Teamtailor workflows.
- Показатели 146/146 regression tests и 13 911 canonical vacancies теперь найдены в публичном docs/REAL_WORLD_READINESS_V2_REPORT.md от 04.10.2026. Это исторические результаты ограниченного scope, не текущий запуск. README одновременно помечает production readiness PARTIAL.
- ARC: по сообщённой истории есть Git, CMake/CTest, CI builds, Windows/Linux, Debug/Release и regression/GPU tests. CI не означает автоматически continuous deployment.
- Docker, n8n и CI включать как практический опыт по подтверждению пользователя. JobHunter — LLM application, не RAG.
- Azure: обсуждение/настройка Ubuntu VM, SSH, GitHub/scp, Python, tmux; завершённый production deployment не подтверждён. Формулировать как базовое знакомство/экспозицию, без cloud production experience.
- Google Colab для ML/GPU — практика; полноценный GCP experience не подтверждён.
- AWS, RAG, LangGraph не подтверждены; LangChain обсуждался, законченной реализации нет.

### LabFlow — координация лабораторных процессов

Источник: https://github.com/Flyingzaptop/LabFlow, README просмотрен 14.10.2026.

- React 19, TypeScript, Vite; Python, Django 5.2, Django REST Framework.
- SQLite для разработки, PostgreSQL для варианта развёртывания.
- REST API, OpenAPI, серверные сессии, CSRF, роли и разрешения (RBAC).
- Процедуры с версиями, образцы, этапы обработки, статусы, заметки и журнал аудита.
- Документированы тесты backend и Vitest frontend; это свидетельство содержания проекта, не утверждение о прохождении тестов в этой сессии.
- Развёртывание на Windows и Ubuntu: Waitress, Gunicorn, Caddy, systemd; backup и инструкции восстановления.
- Опциональные интеграции RADIUS, Ollama, Whisper. Не описывать как обязательные или активные функции.
- Публичная версия — демонстратор с фиктивными данными. Фактическое использование в больнице и соответствие публичной версии уточнить перед утверждением о production deployment.
- Подходит для акцентов: full-stack, backend, internal tools, workflow automation, API, access control, testing, deployment.

### Приложение для управления сотрудниками

- Отдельный проект; по словам пользователя, передан/продан.
- Можно описывать задачу и личный вклад без публикации кода.
- Стек, функции, сроки, заказчик и измеримый результат пока не уточнены.
- Не переносить автоматически Django/React, AI/LLM и другие функции LabFlow на этот проект.

### Система управления графиками

- Отдельный проект, подтверждён пользователем.
- Тип графиков, технологии, состояние внедрения и функции пока не уточнены.

### ARC — Adaptive Runtime Core

Источник: https://github.com/Flyingzaptop/ARC, README просмотрен 14.10.2026.

- Экспериментальный graphics runtime: C++, D3D12, CMake, Windows SDK.
- Наблюдение/interception D3D12, граф ресурсов и зависимостей, lifetime tracking и GPU attribution.
- Исследование обратимых действий над GPU workloads, контроля качества и rollback.
- Эксперименты CPU-to-GPU offload и измерение накладных расходов.
- ARC 2.0 / runtime IR описан как направление миграции; не выдавать всю целевую архитектуру за реализованную.
- Не заявлять универсальное ускорение FPS. Описывать конкретные измерения только с условиями эксперимента.
- Подходит для акцентов: C++, systems programming, graphics, GPU, performance analysis, R&D.

### Финансовые данные и ML / R&D

Общее описание в прежних CV: многолетнее самостоятельное исследование золота и финансовых временных рядов; подготовка данных, признаки, target/labels, loss/reward, метрики и сравнение моделей.

Публичные подтверждения:

- https://github.com/Flyingzaptop/gc-mbo-research — CME GC event-level MBO/L3; Rust replay и FIFO execution simulation, Python feature engineering, ML, walk-forward validation, latency/execution stress, causality tests. README содержит 20 каталогов экспериментов и отрицательные результаты. Не заявлять прибыльную стратегию.
- https://github.com/Flyingzaptop/stargazin — pipeline XAUUSD: Parquet ingestion, normalization, features, labels, training/checkpoints, offline scoring, online preprocessing; RetNet-lite и трёхклассовая модель; Rust/PyO3 для отдельных горячих участков. Описанные метрики датированы апрелем 2026 и не являются актуальной оценкой всей работы.
- https://github.com/Flyingzaptop/stargaze-l2-vwap — проект сбора и исследования рыночных данных, L2/VWAP. README сохранён локально; полный разбор кода ещё не выполнен.
- В прежних CV перечислены NumPy, Pandas, PyTorch/TensorFlow, CNN, GRU, LSTM, TCN, Transformer, Mamba/Mamba2 и основы RL. Наличие каждого инструмента и глубину личной практики уточнять по проектам, а не объявлять одинаковый уровень владения.
- Подходит для акцентов: Python, data engineering, time series, machine learning, feature engineering, model evaluation, reproducibility, Rust, performance.

### MultiNeuro

Источник: https://github.com/Flyingzaptop/MultiNeuro, README просмотрен 14.10.2026.

- Telegram bot с AI API; README упоминает openai, pyTelegramBotAPI и nltk.
- Небольшой дополнительный проект. Не использовать как доказательство production-scale AI systems.

### Antillia — ранняя предпринимательская инициатива

Источники: сообщение пользователя и https://antillia.tech/, HTML сайта просмотрен 14.10.2026.

- Написание бренда на сайте: Antillia (две l).
- Сайт, позиционирование и предложения услуг: websites, web applications, design, AI, automation, business process analysis.
- Портфолио сайта прямо обозначено как демонстрационные концепты, не клиентские реализации.
- Можно включать как «Współtworzenie inicjatywy Antillia — web, software i automatyzacja».
- Точная роль, дата начала и личный вклад в сайт/коммерческие процессы пока не подтверждены. Не назначать автоматически CEO или зарегистрированную компанию.
- Перечень услуг компании сам по себе не подтверждает личное владение всеми дисциплинами.

### Инженерные проекты

Источники: ранее предоставленные CV; подтверждение деталей по файлам проектов ещё предстоит.

- Axial turbojet engine — концепция и CAD-моделирование элементов осевого двигателя; не заявлять изготовленный/работающий двигатель.
- Cycloidal drive — геометрия и моделирование циклоидальной передачи.
- RobotStudio — академические станции сварки и паллетизации, траектории и логика процесса.
- 3D printing / prototyping — STEP/STL, проектирование деталей, ограничения FDM.
- Fusion 360 — основное CAD-средство по прежнему CV; AutoCAD; основы NX и FluidSim.

## Образование и курсы

- Politechnika Wrocławska — Robotyka i Automatyzacja Procesów, studia inżynierskie; начало 10.2022 по CV; окончен V семестр по обновлению пользователя.
- Uniwersytet WSB Merito we Wrocławiu — Inżynieria sieci, systemów i bezpieczeństwa IT, studia inżynierskie niestacjonarne; начало 03.2026 по CV; текущий II семестр.
- Сертификат Python AI: 28.02.2024–04.12.2024; Python Programming Language и Artificial Intelligence Using Python — оценки 10 (Excellent).
- Программа IT Step включает Python, SQL/PostgreSQL, ORM, NumPy/Pandas, scikit-learn, PyTorch, NLP, computer vision и LLM. Учебную программу не выдавать за практический опыт по каждой теме.
- ITStep 11.2021 — указан в CV, отдельного подтверждения пока нет.

## Языки и дополнительные навыки

Дополнение пользователя 14.10.2026 при разборе PITax: базовые знания Java; ранее занимался разработкой под Android. Стек, объём и проекты Android пока не уточнены. iOS и React Native не подтверждены. Среднюю оценку не указывать без конкретного значения; соответствие требованию PITax 4,8+ не подтверждено.

По прежним CV: польский — продвинутый; английский — продвинутый/технический; украинский и русский — родные. CEFR уровни не назначать без уточнения.

Windows/Linux, диагностика ПК, сборка и модернизация, hard-tube water cooling; основы DHCP, MAC, routing и настройки router. AI-assisted development: Cursor, Claude Code, Codex; локальные LLM и Protobuf/API по прежним CV.

Права/SEP в прежнем CV были placeholder: удалить placeholder из готового CV, наличие не утверждать.

## Правила адаптации под вакансии

Дополнительное требование пользователя: для каждой вакансии выдавать FIT N/10 с коротким обоснованием сильных совпадений и основных пробелов. Оценивать задачи, обязательный стек и глубину/стаж отдельно от желательных навыков. FIT не является вероятностью оффера и не включается в CV для работодателя.

1. Прочитать вакансию целиком; выделить обязанности, обязательные/желательные технологии, язык и ограничения.
2. Сопоставить keywords с подтверждённой базой. Использовать точное название технологии или компетенции там, где опыт его поддерживает.
3. Перестроить headline, summary, порядок skills, проектов и bullets вокруг требований работодателя.
4. Для IT-вакансии оставить инженерные проекты компактно; для инженерной роли раскрыть CAD/robotics и сократить IT/R&D. Не удалять инженерную основу по умолчанию.
5. Не уменьшать масштаб реального проекта и не придумывать опыт ради keywords; при сокращении сохранять задачу, вклад и результат.
6. Различать профессиональную работу, собственные проекты, академическую практику и учебные темы.
7. Не заявлять коммерческое использование, безопасность, экономию времени, доход или production readiness без подтверждения.
8. Сделать читаемую ATS-friendly версию: стандартные заголовки, текстовые контакты, понятные даты, без keyword stuffing.
9. Везде в новых материалах использовать Denis Gruszkiewicz и r3dflzp.ns@gmail.com.
10. Исторические исходные PDF остаются источниками; обновлённые документы создавать отдельно.

## Открытые вопросы перед финальным основным CV

- Точная роль и личный вклад в Antillia; дата начала.
- Стек, реализованные функции и статус системы графиков и проданного приложения для сотрудников.
- Какие версии проектов реально используются сотрудниками, сколько пользователей и какие результаты можно доказать.
- Приватные репозитории Flyingzaptop: подключённый GitHub connector сейчас показывает преимущественно fuxassistant, поэтому доступа ко всем приватным Flyingzaptop не подтверждено. Их не делали публичными.
- Просмотрены все 14 публичных репозиториев: деревья, документация, конфигурации и выбранные реализации/тесты. Полного построчного аудита и анализа всех веток/истории личного вклада нет; точный scope и источники в GITHUB_PORTFOLIO.md.

## Исходные материалы

Шесть PDF из Downloads: denys_hrushkevych (1).pdf; Programma_Python_AI_2024 (3) 2 pl.pdf; Denis_Gruszkiewicz_Master_CV (2).pdf; Denis_Gruszkiewicz_Engineer_CV.pdf; Denis_Gruszkiewicz_IT_CV.pdf; Denis_Gruszkiewicz_IT_Automation_CV.pdf.

Извлечённый текст: tmp/pdfs/. README публичных репозиториев: tmp/*-README.txt. HTML Antillia: tmp/antillia.html. Это технические исходники для дальнейшего разбора, не готовые CV.


======== FILE: PROFILE_UPDATES_2026-10-22.txt ========

Уточнения профиля от 22.10.2026, подтверждены пользователем
ПОЗДНЕЕ УТОЧНЕНИЕ ГРАФИКА (приоритет над старой готовностью к визитам): нужны гибкие часы. С марта 2027 максимум 1-2 дня стационарно в неделю во Вроцлаве; остальная работа удаленно. Допускается часть ставки либо fully remote из Польши. Hybrid без числа дней и flexible shifts без права согласовать график считать неподтвержденными. Расширить поиск на CAD/remote-friendly engineering; freelance учитывать отдельно от найма.
Имя: Denis Gruszkiewicz. Email: r3dflzp.ns@gmail.com.
Права B: есть, стаж владения 3 года.
AD: практика ограничена подключением компьютеров к домену; не утверждать администрирование AD/GPO.
Windows Server: практического опыта нет.
Microsoft 365: пользователь оценивает знание как очень хорошее; конкретные административные функции tenant/Exchange/Intune не уточнены.
Визиты и дежурства у местных клиентов приемлемы пользователю независимо от частоты.
Желаемый формат: часть ставки или полный день гибридно в районе Вроцлава; дата начала по договорённости.

DRACO, oferta 1005150644
FIT после уточнений: 8/10. Прямой опыт поддержки, Windows/PC, LAN, Linux basics, M365 и подтверждённые права/выезды. Разрыв: Windows Server, полноценное AD, конкретная серверная/backup/M365 administration. Не выдавать желательные технологии за освоенные.
Польское CV: output/pdf/Denis_Gruszkiewicz_CV_DRACO_IT_Support_PL.pdf; 1 страница, текстовые контакты, актуальные статусы учёбы. Заявка не отправлялась.
Старые PROFILE_BASE.md и GITHUB_PORTFOLIO.md по прежнему пути в текущей среде не найдены; эти новые уточнения сохранены отдельно без реконструкции неподтверждённых данных.

