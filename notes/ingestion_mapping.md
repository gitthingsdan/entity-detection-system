# Mini ejercicio guiado

Hacer una tabla o lista con **tres categorías**:

* Persistir sí o sí.
* Persistir quizá.
* No persistir por ahora.

Y empezar solo con estos candidatos que los archivos muestran de forma clara:

* `/pokemon/{id}`: `id`, `[pokemon-]name`, `height`, `weight`, `base_experience`, `species`, `stats`, `types`,
  `abilities`.
* `/pokemon-species/{id}`: `[species-]name`, `evolves_from_species`, `generation`, `is_legendary`, `is_mythical`,
  `capture_rate`, `color`,
  `habitat`, `shape`, `egg_groups`, `growth_rate`.

## Próximo paso

La tarea ahora podría ser muy concreta:
> Tomar **10 a 15 campos máximo** de [`pokemon_articuno.json`](../perplexity/pokemon_articuno.json) y [
`pokemon_species_articuno.json`](../perplexity/pokemon_species_articuno.json), clasificándolos en estas tres categorías.

| Persistir sí o sí      | Persistir quizás | No persistir por ahora |
|------------------------|------------------|------------------------|
| `id`                   |                  | `color`                |
| `name`                 |                  | `habitat`              |
| `height`               |                  | `shape`                |
| `weight`               |                  |                        |
| `base_experience`      |                  |                        |
| `species`              |                  |                        |
| `stats`                |                  |                        |
| `types`                |                  |                        |
| `abilities`            |                  |                        |
| `evolves_from_species` |                  |                        |
| `generation`           |                  |                        |
| `is_legendary`         |                  |                        |
| `is_mythical`          |                  |                        |
| `capture_rate`         |                  |                        |
| `egg_groups`           |                  |                        |
| `growth_rate`          |                  |                        |

_Nota: la "base_experience" de la PokéAPI corresponde a las Generaciones V, VI y VII._