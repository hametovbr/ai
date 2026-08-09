# AI skills

Резервная копия пользовательских навыков ChatGPT/Codex.

## Представленные навыки

| Навык | Статус | Назначение |
|---|---|---|
| [making-pragmatic-architecture-decisions](skills/making-pragmatic-architecture-decisions/SKILL.md) | Активен | Выбор, проектирование, ревью и упрощение программной и системной архитектуры: интеграции, миграции, развёртывание, границы автоматизации и решения build-versus-buy. |
| [fileflows-flow-authoring](skills/fileflows-flow-authoring/SKILL.md) | Активен | Создание и проверка импортируемых FileFlows flow JSON, подбор узлов, JavaScript/C#-логика, FFmpeg, Docker-пути и интеграция с Sonarr/Radarr. |
| [gathering-architecture-context](skills/gathering-architecture-context/SKILL.md) | Активен | Сбор и проверка требований, текущего поведения системы, нативных возможностей, аналогов и эксплуатационных ограничений перед архитектурным решением. |
| [challenging-architecture-decisions](skills/challenging-architecture-decisions/SKILL.md) | Активен | Независимый стресс-тест архитектуры, ADR, интеграции, миграции, выбора платформы или плана реализации до утверждения. |

## Структура

- `skills/<skill-name>/SKILL.md` — основные инструкции активного навыка.
- `skills/<skill-name>/agents/` — метаданные интерфейса.
- `skills/<skill-name>/references/` — справочные материалы.
- `skills/<skill-name>/scripts/` — вспомогательные сценарии.
- `skills/<skill-name>/assets/` — ресурсы навыка.
- `skills/uninstalled/<skill-name>/` — отключённые навыки.

Имена каталогов формируются из поля `name` в YAML frontmatter файла `SKILL.md`. Резервная копия обновляется автоматически. История изменений сохраняется в Git.
