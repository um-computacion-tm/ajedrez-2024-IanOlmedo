## [1.2.1] - 23 de agosto de 2024
# Agregado
- Todos los test de rook para verificar posibles movimientos ya estan funcionando bien, agregue uno mas 
- Metodo de get_moves_queen realizado tengo un problema con uno de los test en el que al devolverme 
las posiciones posibles de la reina en 4,4 el metodo me devuelve algunos valores repetidos 
asi que ese test estara en desarrollo.

## [1.2.0] - 22 de agosto de 2024
# Agregado
- Pude Arreglar los test de board
- Verifican que las posiciones iniciales esten bien asignadas y que el tablero se muestre bien
- Añadi todos los test necesarios para chess: init, playing, show_board, change_turn y move que fue el que mas me costo
- Cree un metodo remove_piece para que cada vez que se mueva una pieza se coloque un "None" en su lugar
- Proximo commit queda arreglar unos errores en test_rook y empezar el desarrollo de las demas piezas!
- Agregue el test correcto para ver los movimientos realizables por rook

## [1.1.9] - 21 de agosto de 2024
# Agregado
- Agregué todo lo de la clase del 20/08/24 con los `__str__`, `cli`, `chess`, menos los `except`.
- Completé el test de `str_board` con todas las fichas faltantes.
- El commit de mañana será intentar solucionar los problemas.

## [1.1.8] - 20 de agosto de 2024
# Agregado
- Solucioné los problemas de importación con el profe Daniel.

## [1.1.7] - 19 de agosto de 2024
# Agregado
- Aún sigo teniendo errores de importación que no logro solucionar ni entender.
- Más allá de eso, completé los test para `board` sin poder verificar si están bien hechos. Pero su función es verificar que el tablero tenga todas las piezas bien posicionadas y que las casillas vacías estén en `None`.

## [1.1.6] - 18 de agosto de 2024
# Agregado
- Este commit se basó en arreglar muchos errores o intentar entenderlos, terminé de configurar `coverage` pero aún tengo problemas con las importaciones para cada archivo.
- Agregué una función que devuelve el tamaño del tablero (lo de menos en este commit).

## [1.1.5] - 17 de agosto de 2024
# Agregado
- Definí el método `get_moves_rook` que define todos los movimientos posibles para la torre, siempre y cuando esté dentro del tablero.
- Hice un test verificando este mismo método (`get_moves_rook`), que por el momento solo verifica que devuelva toda la lista de movimientos disponibles para la torre, sin tener en cuenta si está fuera o si tiene una pieza aliada por delante.
- Y dentro de `board` creé un método (`set_piece`) que mueve la pieza de lugar.

## [1.1.4] - 16 de agosto de 2024
# Agregado
- Definí para todas las piezas los métodos `posibles_movimientos` → dependiente de funciones aún no definidas.
- Método `mover_a` (aún no definida).
- `get_moves(nombreP)` (No definida aún).
- Todos los métodos fueron establecidos.
- Próximo commit intentaré crear los movimientos para alguna pieza.

## [1.1.3] - 15 de agosto de 2024
# Agregado
- Archivos `__init__.py` para cada carpeta de `test` y `pieces`.
- En `board` ubiqué todas las piezas en su posición inicial.
- Corregí los tests de `board` y verifiqué qué casillas deben estar vacías en un comienzo.

## [1.1.2] - 14 de agosto de 2024
# Agregado
- Primeros tests de `Board`.
- Archivo `test` para `Chess`, verifica la composición del tablero.

## [1.1.1] - 13 de agosto de 2024
# Agregado
- Carpetas `test` con el test para `board`, próximamente los que faltan.
- Carpeta para `pieces` con todos los archivos para cada pieza.
- La interfaz con el usuario (`cli`).
- El Tablero (`board`).
- `Ajedrez` que es la comunicación directa con el cliente (`chess`).
