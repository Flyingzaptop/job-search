# Подача заявок с участием человека (для сессии на компьютере Denis)

Цель: Denis сам проходит проверки на бота (Cloudflare, reCAPTCHA) в своём браузере, всё остальное делает Claude. Запускать в Claude Desktop или `claude remote-control` в этой папке, чтобы были инструменты браузера и Computer Use.

## Правила
1. Банк ответов (контакты, зарплата, доступность, согласия, правила): https://claude.ai/artifact/36wdRLhu8dmo1WmQkawHtC (приватный; читать через Artifact read). Использовать только его. Чего там нет, не угадывать, а спросить Denis.
2. Перед отправкой каждой формы: показать Denis скриншот и список введённых значений, получить «ок». Для пачки можно позвать Opus-ревьюера.
3. Капча или «verify you are human»: остановиться, попросить Denis пройти проверку, продолжить после его «готово». Проверки не обходить и не маскировать браузер.
4. Аккаунт кандидата на портале работодателя создавать можно (почта r3dflzp.ns@gmail.com, случайный пароль, нигде не сохранять). Не создавать, если нужен KYC или платёж.
5. После отправки: проверить страницу подтверждения и письмо в r3dflzp.ns@gmail.com, затем записать результат: статус `applied` в трекере (ArtifactData коллекция `status`, doc id = id вакансии с заменой символов вне `A-Za-z0-9_-.~:@+` на `_`) и строку в `tracker/applications.json`.
6. Образование: если в форме есть вариант «wyższe niepełne / w trakcie studiów / student», выбирать его. Если есть только завершённые уровни, НЕ выбирать «Wyższe» самому и не подставлять «Średnie» молча: остановиться и попросить Denis выбрать вручную (решение и клик его). Высшее не закончено, диплома нет; сам Claude не заявляет завершённое высшее. Остальные поля формы заполнять как обычно.
7. Резюме нового дизайна лежат в `cv/out2/` (PDF), исходники в `cv/content2/`, сборка `python3 tools/cv/build_cv2.py cv/content2/<файл>.json`.

## Очередь (на 27.10.2026)
| # | Вакансия | Форма | Что мешало автоматике | CV |
|---|---|---|---|---|
| 1 | Fabrity S.A., Junior Python Developer (UoP, remote) | https://form.erecruiter.pl/form/cf0689d8231342e4b83d979568bb03df | сервер даёт 403 на загрузку CV из облака; нужен уровень английского: C1; модель работы «Zdalny»; зарплата цифрой | cv/out2/Denis_Gruszkiewicz_CV_Fabrity_PL.pdf |
| 2 | IRIS Galerie, Odoo support / Junior Python (UoP, 9–12k PLN, 90% remote, Skawina 10%) | страница justjoin: https://justjoin.it/job-offer/iris-galerie-distribution-sp-z-o-o--odoo-support-junior-python-developer-skawina-python, кнопка Apply | аккаунт justjoin и reCAPTCHA | cv/out2/Denis_Gruszkiewicz_CV_IRIS_Odoo_EN.pdf |
| 3 | smartware, Junior Test Automation Engineer (UoP 5000–6500 PLN, remote/hybrid) | LinkedIn, «Aplikuj»: pl.linkedin.com/jobs/view/junior-test-automation-engineer-at-smartware-sp-z-o-o-4475005096 | нужен вход в LinkedIn, реальная форма скрыта | собрать под вакансию |
| 4 | MasterBorn, Intern Integration Consultant (UZL 4300 PLN, ~6 ч/день, remote/hybrid) | LinkedIn: pl.linkedin.com/jobs/view/intern-integration-consultant-at-masterborn-4470211285 | то же | собрать под вакансию |
| 5 | Numatix, Quantitative Developer Intern (remote) | https://himalayas.app/companies/numatix-solutions/jobs/quantitative-developer-intern | Cloudflare; проверить договор (нужен UZ/UoP) | собрать |
| 6 | Ambit Iberia, Junior AI Engineer Pharma (full remote) | https://himalayas.app/companies/ambit-iberia/jobs/junior-ai-engineer-pharma-full-remote | Cloudflare; проверить договор | cv/tailored в трекере |
| 7 | Altimi, Robotics/PLC Automation Engineer | https://czyjesteldorado.pl/praca/381202-robotics-plc-automation-engineer-altimi | Cloudflare | cv в трекере |

Для 5–7 перед подачей проверить живость и тип договора (только UoP/UZ), для 3–4 найти настоящую ссылку подачи после входа в LinkedIn.

## Уже подано автоматически (27.10)
Cloudfide (Junior Software AI Engineer), Vertex Recruitments (Trainee Data Engineer): подтверждения на почте.
