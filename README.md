##IAN OLMEDO

#  ajedrez-2024-IanOlmedo


#  CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-IanOlmedo/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-IanOlmedo/tree/main)

#  Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/5349b66ff7e7f31f9aed/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-IanOlmedo/maintainability)

#  Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/5349b66ff7e7f31f9aed/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-IanOlmedo/test_coverage)



# Juego de Ajedrez Educativo

Este proyecto es un juego de ajedrez educativo implementado en Python. El juego incluye una interfaz de línea de comandos (CLI) que te permite jugar al juego ingresando comandos en la consola.

## Requisitos
* coverage==7.6.1

## Características del Juego

* El juego consta de un tablero de ajedrez de 8 filas x 8 columnas, ademas de este tiene cada pieza correspondiente al juego,
con es el Peon, Alfil, Torre, Reina y Rey. Los movimientos de las piezas estan establecido segun las normas de ajedrez. El juego 
terminara cuando uno de los 2 jugadores se rinda o alguno de los jugadores pieda a su Rey.

* contiene a "cli.py" que es el archivo que permite conectar/posibilitar al usuario interactuar con el ajedrez.

## Ejecución

1. Clona el repositorio: `git clone https://github.com/um-computacion-tm/ajedrez-2024-IanOlmedo.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Juega en la consola: `python3 cli.py`

## Dockerfile

Comandos:
1. `docker buildx build -t ajedrez .`
2. `docker run -i ajedrez`

