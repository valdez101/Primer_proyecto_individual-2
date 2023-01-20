POYECTO INDIVIDUAL vs1.0.1
=============

**Table of Contents**

[TOCM]

[TOC]

### OBJETIVO

-Presentar y explicar en un archivo de texto de fácil acceso el propósito del proyecto, con información sobre cómo usar la API en deta.
-Que al momento de usar la API no quede ninguna duda sobre el proyecto.

## Resumen

-Esta es una API creada despues de haber realizado la limpieza de datos se trabaja con las 5 querys que son la principal funcion de la API.

## Contexto

Application Programming Interface es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles que permiten por ejemplo, crear pipelines facilitando mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.

Hoy en día contamos con FastAPI, un web framework moderno y de alto rendimiento para construir APIs con Python.

## Consultas:
##### Para disponibilizar los datos la empresa usa el framework FastAPI, las querys son las siguientes:
- Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma (query_1)
- Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (query_2)
- La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.(query_3)
- Película que más duró según año, plataforma y tipo de duración (query_4)
- Cantidad de series y películas por rating (query_5)

## Accesos a querys:

- query_1: podemos acceder con: '/get_word_count/{plataforma}/{keywords}'
- query_2 : podemos acceder con: '/get_score_count/{plataforma}/{score}/{year}'
- query_3: podemos acceder con : '/get_second_score/{plataform}'
- query_4: podemos acceder con: '/get_longest/{plataform}/{duration}/{year}'
- query_5: podemos acceder con: /get_rating_count/{rating}

## Fuente de datos
- Podrán encontrar los archivos con datos en la carpeta Datasets, en este mismo repositorio.

## Material de apoyo
-Imagen Docker con Uvicorn/Guinicorn para aplicaciones web de alta performance:
- https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/

-FAST API Documentation:
- https://fastapi.tiangolo.com/tutorial/

-Documentacion pandas
- https://pandas.pydata.org/docs/development/contributing_docstring.html

## Link de la API

- https://7chysr.deta.dev ( recordar que con la /docs podemos acceder a todas las querys)


###End
