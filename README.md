# Movies_Recommendation_System

## Index
- [Recomendation\_System](#movies_Recommendation_System)
	- [Index](#index)
	- [Nombre de los alumnos participantes](#integrantes)
    - [Introducción](#introducción)
	- [Objetivo del trabajo](#objetivos-del-trabajo)
	- [Breve descripción del dataset](#breve-descripción-del-dataset)
		- [`movies_metadata.csv`](#movies_metadatacsv)
		- [`ratings.csv`](#ratingscsv)
		- [`keywords.csv`](#keywordscsv)
		- [`credits.csv`](#creditscsv)
	- [Conclusiones](#conclusiones)
	- [Licencia](#licencia)
---

## Integrantes
- Espíritu Cueva, Renzo Andree (u202113340)
- Mancilla Cienfuegos, Paula Jimena (u202115844)
- John Davids Sovero Cubillas (u202115065)

**Docente:** Richard Fernando Fernandez Vasquez

## Introducción
El presente proyecto corresponde al trabajo parcial del curso de Aplicaciones de Data Science, el cual plantea el desarrollo de un sistema de recomendación de películas con el uso de redes neuronales densas con una interfaz GUI. Durante este proceso, se emplearán los conocimientos adquiridos durante el ciclo académico sobre entendimiento del negocio, comprensión de los datos, modelado, evaluación y despliegue.

## Objetivos del trabajo
- Crear un sistema de recomendación de películas para proporcionar a los usuarios una experiencia más personalizada en una plataforma de streaming de películas.
- Implementar una solución intuitiva y de fácil ejecución, asegurando al mismo tiempo una alta precisión en las recomendaciones proporcionadas.
- Ofrecer una experiencia de usuario personalizada y adaptada a las preferencias individuales, presentada a través de una interfaz gráfica (GUI) simple y amigable.

## Breve descripción del dataset
El dataset proporciona información detallada sobre una variedad de películas, incluyendo características como su título original y traducido, la fecha de lanzamiento, el idioma original, el presupuesto, los ingresos generados, la duración, el género, la popularidad y las calificaciones. También incluye información sobre la producción, como los nombres de las empresas y los países de origen. Además, proporciona detalles sobre la disponibilidad de la película para adultos, la presencia de un sitio web oficial, la presencia de un póster y la existencia de un video asociado. Esta amplia gama de atributos permite un análisis completo y la creación de modelos de recomendación de películas personalizados.

Nota: El conjunto de datos limpio se denominará "dataset.csv", ya que los otros archivos CSV son demasiado pesados para lo que soporta GitHub. En caso de que se necesiten estos archivos, se pueden consultar en el siguiente enlace de Kaggle: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&select=movies_metadata.csv

### `movies_metadata.csv`
| Columna               | Descripción                                                                       |
|-----------------------|-----------------------------------------------------------------------------------|
| Id                    | Identificador único para cada película.                                           |
| adult                 | Indica si la película es para adultos (true/false).                               |
| belongs_to_collection | Información sobre la colección a la que pertenece la película, si la tiene.       |
| budget                | Presupuesto de la película en dólares.                                             |
| genres                | Géneros asociados con la película.                                                |
| original_language     | Idioma original en el que se produjo la película.                                 |
| overview              | Breve descripción general de la trama de la película.                              |
| popularity            | Puntuación de popularidad de la película.                                         |
| production_companies  | Compañías productoras involucradas en la realización de la película.              |
| release_date          | Fecha de lanzamiento de la película.                                               |
| revenue               | Ingresos generados por la película en taquilla.                                   |
| runtime               | Duración de la película en minutos.                                               |
| spoken_languages      | Idiomas hablados en la película.                                                   |
| status                | Estado de la película (por ejemplo, lanzada, en producción, etc.).                |
| tagline               | Lema o eslogan asociado con la película.                                           |
| vote_average          | Promedio de las calificaciones de la película.                                     |
| vote_count            | Número total de votos recibidos por la película.                                   |

### `ratings.csv`
| Columna   | Descripción                                                            |
|-----------|------------------------------------------------------------------------|
| user_id   | Identificador único del usuario que proporcionó la calificación.       |
| movie_id  | Identificador único de la película que recibió la calificación.        |
| rating    | Calificación otorgada por el usuario a la película (escala del 1 al 5).|
| timestamp | Marca de tiempo que indica cuándo se registró la calificación.         |

### `keywords.csv`
| Columna  | Descripción                                                 |
|----------|-------------------------------------------------------------|
| Id       | Identificador único de la película.                         |
| keywords | Conjunto de palabras clave que describen la película.       |

### `credits.csv`
| Columna | Descripción                                                                        |
|---------|------------------------------------------------------------------------------------|
| Id      | Identificador único de la película.                                                 |
| crew    | Lista de información de cada involucrado en la película (director, escritor, etc.).|
| cast    | Lista de información de cada actor y qué personaje interpreta en la película.      |

## Conclusiones 
... en desarrollo

## Licencia
Este trabajo está disponible bajo la licencia [MIT License].