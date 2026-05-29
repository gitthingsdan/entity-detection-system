> # Tu siguiente tarea
> Tu siguiente mini-meta podría ser esta:
> * Definir las tablas que vas a crear.
> * Decidir qué columnas van en cada una.
> * Anotar de qué endpoint sale cada columna.
> * Recién después abrir el editor y programar.
>
> Si quieres mantener el impulso sin que yo te sople demasiado, el paso natural ahora es que tú me propongas tu borrador
> de tablas para schema.py, aunque sea en texto y no en código.

Tabla: "species"

| Columna                   | Endpoint                |
|---------------------------|-------------------------|
| `id`                      |                         |
| `capture_rate`            | `/pokemon-species/{id}` |
| `egg_group_1`             | `/pokemon-species/{id}` |
| `egg_group_2`             | `/pokemon-species/{id}` |
| `evolves_from_species_id` |                         |
| `generation`              | `/pokemon-species/{id}` |
| `growth_rate`             | `/pokemon-species/{id}` |
| `is_legendary`            | `/pokemon-species/{id}` |
| `is_mythical`             | `/pokemon-species/{id}` |
| `name`                    | `/pokemon-species/{id}` |
| `resource_url`            | `/pokemon-species/{id}` |

Tabla: "pokemon"

| Columna           | Endpoint        |
|-------------------|-----------------|
| `id`              |                 |
| `ability_1`       | `/pokemon/{id}` |
| `ability_2`       | `/pokemon/{id}` |
| `ability_3`       | `/pokemon/{id}` |
| `base_experience` | `/pokemon/{id}` |
| `height`          | `/pokemon/{id}` |
| `name`            | `/pokemon/{id}` |
| `order`           | `/pokemon/{id}` |
| `resource_url`    | `/pokemon/{id}` |
| `species_id`      |                 |
| `type_1`          | `/pokemon/{id}` |
| `type_2`          | `/pokemon/{id}` |
| `weight`          | `/pokemon/{id}` |

Tabla: "stats"

| Columna           | Endpoint        |
|-------------------|-----------------|
| `id`              |                 |
| `pokemon_id`      |                 |
| `hp`              | `/pokemon/{id}` |
| `attack`          | `/pokemon/{id}` |
| `defense`         | `/pokemon/{id}` |
| `special_attack`  | `/pokemon/{id}` |
| `special_defense` | `/pokemon/{id}` |
| `speed`           | `/pokemon/{id}` |
