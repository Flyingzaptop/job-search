# Поиск вакансий: инструкция запуска («Искать»)

Запуск: кнопка «Искать» в трекере → scheduled task `job-search: run` → эта сессия получает задание и выполняет шаги ниже.
Ничего не отправлять работодателям. Только найти, оценить, показать.

## 0. Перед стартом
- `PROFILE.md` — профиль и **жёсткие условия графика**.
- `tools/search/sources.json` — ≥100 источников. `tools/search/keywords.json` — ключевые слова.
- Исключения: `tracker/applications.json` + `PROFILE.md` («Уже подготовлено / подано») + уже оценённые id в `data/scored_*.jsonl`.

## 1. Сбор (Sonnet-сабагенты, до 8 параллельно)
- API-источники запускаю сам: `python3 tools/fetch_apis.py jooble fantastic arbeitnow apify_linkedin2` (+ remoteok/himalayas/jobicy, если добавлены).
  Бюджеты: Apify ≤ $1 за запуск; Fantastic ≤ 100 вакансий за запуск.
- Остальные источники (`method: site|fetch`) делю на пачки по ~14 и отдаю Sonnet-сабагентам. Каждый:
  - для каждого источника делает 2–4 запроса WebSearch вида `site:<domain> (<keywords eng>) (Wrocław OR zdalnie OR remote)` и `site:<domain> (<keywords it>) ...`;
  - открывает (WebFetch) только объявления, похожие на junior/intern/staż и подходящие по локации;
  - пишет найденное в `data/raw/web_<YYYY-MM-DD>_<batch>.jsonl` в формате fetch_apis (`source`, `id`=`web:<url>`, `title`, `company`, `location`, `type`, `salary`, `posted`, `url`, `text` ≤ 4000 символов);
  - пишет журнал покрытия `data/logs/coverage_<YYYY-MM-DD>_<batch>.json`: по каждому источнику — запросы, число результатов, ошибки/блокировки.
  - не обходит капчи и защиту от ботов: заблокировано → отмечает `blocked` и идёт дальше.

## 2. Фильтр
`python3 tools/prefilter.py` → `data/candidates.jsonl` (дедуп, senior/немецкий, исключение уже поданных).
Новые = кандидаты без оценки → `data/part_<дата>.jsonl`.

## 3. Оценка (Sonnet-сабагенты по ~300 строк)
Каждая вакансия оценивается вручную по `tools/search/SCORING.md`. Результат → `data/scored_<дата>_<n>.jsonl`.

## 3b. CV под лучшие вакансии
Для вакансий с fit ≥ 7 и schedule ≥ 7 (не больше 10 за запуск): сделать `cv/content/job_<safe id>.json` на основе
`cv/content/base_<Engineering|IT>_<PL|EN>.json` (язык — по языку объявления), подогнать role/profil/порядок навыков под требования
без выдуманного опыта (правила в context/1_skills_projects_base.md), собрать `python3 tools/cv/build_cv.py ...` и положить PDF в
`tracker/cv/tailored/<safe id>.pdf` (safe id = id, где всё кроме `A-Za-z0-9_-.~@+` и `:` заменено на `_`). В карточке появится «CV под вакансию».
Для тех же вакансий написать мотивационное сообщение (PL и/или EN, ≤ 1000 символов, без обещаний вложений, с условием графика)
в `data/messages.json` как `{"<id>": {"PL": "...", "EN": "..."}}`. Иначе кнопка «Сообщение» копирует шаблон по направлению.

## 4. Публикация
`python3 tools/build_tracker.py` → публикую трекер (`tracker/index.html` + `jobs.json` + `applications.json` + все PDF из `tracker/cv/`),
коммичу и пушу в `main`, коротко пишу пользователю: сколько источников реально проверено (по журналам), сколько новых, топ-10.
