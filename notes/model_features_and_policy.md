# Próximo paso

> Tu siguiente avance podría ser separar tu tabla en dos lentes: campos a persistir en BD y campos candidatos para el
> modelo.

Decidí hacerlo yo solo, a continuación (los campos a persistir en BD están en la tabla
de [ingestion_mapping.md](../notes/ingestion_mapping.md)):

| Usar para modelo | Usar quizás       | No usar para modelo |
|------------------|-------------------|---------------------|
| `height`         | `base_experience` | `id`                |
| `weight`         | `capture_rate`    | `name`              |
| `stats`          | `egg_groups`      | `generation`        |
| `types`          | `growth_rate`     |                     |
| `abilities`      |                   |                     |
| `is_legendary`   |                   |                     |
| `is_mythical`    |                   |                     |

Naturalmente, `is_legendary` e `is_mythical` son prácticamente el posible target, así que no serán usadas como features.

> Tu siguiente decisión importante no es escribir código todavía, sino definir una política de features: “baseline
> conservador” versus “baseline ampliado”.

## Baseline conservador:

- `height`
- `weight`
- `stats`
- `types`
- `abilities`

## Baseline ampliado:

[Baseline conservador](#baseline-conservador), además de:

- `base_experience`
- `generation`
- `capture_rate`
- `egg_groups`
- `growth_rate`

## Política de interpretación:

* Independientemente del rendimiento con el baseline conservador, probar posteriormente el baseline ampliado.
    * Si rinde un poco mejor, se podría utilizar como nuevo baseline.
    * Si rinde mucho mejor, ahí entrar a sospechar y no cantar victoria, porque puede que el modelo esté
      sobreajustándose y no esté detectando reglas generalizadoras, sino que podría estar descansando demasiado en esas
      nuevas features.