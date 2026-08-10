# AI skills

Резервная копия пользовательских навыков ChatGPT/Codex.

## Представленные навыки

| Навык | Статус | Назначение |
|---|---|---|
| [making-pragmatic-architecture-decisions](skills/making-pragmatic-architecture-decisions/SKILL.md) | Активен | Выбор и пересмотр границ программной системы: размещение поведения и состояния, конфигурация или код, форма расширения, интеграция, развёртывание, миграция, владение и build-versus-buy. |
| [fileflows-flow-authoring](skills/fileflows-flow-authoring/SKILL.md) | Активен | Создание и проверка импортируемых FileFlows flow JSON, подбор узлов, JavaScript/C#-логика, FFmpeg, Docker-пути и интеграция с Sonarr/Radarr. |
| [gathering-architecture-context](skills/gathering-architecture-context/SKILL.md) | Активен | Сбор и проверка недостающих, спорных или устаревших фактов о текущей системе перед решениями, влияющими на границы, сохранность данных, внешние контракты, миграцию, развёртывание или восстановление. |
| [challenging-architecture-decisions](skills/challenging-architecture-decisions/SKILL.md) | Активен | Стресс-тест готового архитектурного решения на переусложнение, неподтверждённые предположения, лишние компоненты, риски жизненного цикла и готовность к реализации. |

## Структура

- `skills/<skill-name>/SKILL.md` — основные инструкции активного навыка.
- `skills/<skill-name>/agents/` — метаданные интерфейса.
- `skills/<skill-name>/references/` — справочные материалы.
- `skills/<skill-name>/scripts/` — вспомогательные сценарии.
- `skills/<skill-name>/assets/` — ресурсы навыка.
- `skills/uninstalled/<skill-name>/` — отключённые навыки.

Имена каталогов формируются из поля `name` в YAML frontmatter файла `SKILL.md`. Резервная копия обновляется автоматически. История изменений сохраняется в Git.
