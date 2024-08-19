## [1.1.1] - 13 de agosto de 2024
# Agregado
- Carpetas tets con el test para board, proximamente los que faltan
- Carpeta para pieces con todos los archivos para casa pieza
- La interfaz con el usuario (cli)
- El Tablero (board)
- Ajedrez que es la comunicacion directa con el cliente (chess)

## [1.1.2] - 14 de agosto de 2024
# Agregado
- Primeros Tests de Board
- Archivo test para Chess, verifica la composicion del tablero

## [1.1.3] - 15 de agosto de 2024
# Agregado
- Archivos __init__.py para cada carpeta de test y pieces
- En board ubique en board todas las piezas en su posicion inicial
- Corregi los tests de board y verfico que casillas deben estar vacias en un comienzo

## [1.1.4] - 16 de agosto de 2024
# Agregado
- Defini para todas las piezas los metodos posibles_movimientos--> dependiente de funciones aun no definidas
- Metodo mover_a (aun no definida)
- get_moves(nombreP) (No definida aun)
- Todos los metodos fueron estabecidos 
- proximo commit intentare crear los movimiento para alguna pieza

## [1.1.5] - 17 de agosto de 2024
# Agregado
- Defini el metodo get_moves_rook que define todos los movimientos posibles para la torre
siempre y cuando este dentro del tablero.
- Hice un test verificando este mismo metodo (get_moves_rook), que por el momento solo verfica que devuelva toda la lista de movimientos disponibles para la torre, sin tener en cuenta si esta afuera
o si tiene una pieza aliada por delante
- Y dentro de board cree un metodo (set_piece) que mueve la pieza de lugar

## [1.1.6] - 18 de agosto de 2024
# Agregado
- Este commit se baso en arreglar muchos errores o intentar de entenderlos, termine de configurar coverage pero aun tengo problemas con las importaciones para cada archivo.
- Agregue una funcion que devuelve el tamaño del tablero (lo de menos en este commit)

## [1.1.7] - 19 de agosto de 2024
# Agregado
- Aun sigo teniendo errores de importacion que no logro solucionar ni entender
- Mas alla de eso complete los test para board sin poder verificar si estan bien hechos. Pero
su funcion es verificar que el tablero tenga todas las piezas bien posicionadas y que la casillas vacia esten en None

