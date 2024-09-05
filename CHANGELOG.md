## [1.3.2] - 05 de agosto de 2024
# Agregado
- Generando avances en chess, con un poco de problemas con la importacion con board
- Testeado todos las posubles instancias del metodo move en board y ahora intentando de aplicarlas en chess
- mi ultimo problema es que el test no me identifica que haya alguna figura en el 4,4, mientras claramente estoy seteando el rey ahii


## [1.3.1] - 04 de agosto de 2024
# Agregado
- Refactorizando todos test antiguos en base a los nuevos metodos relacionado con los mover_a
- Cree un metodo en board (move) que valida a que pieza pertece la direccion inicial(from_row, from_col) y dependiendo de esto, 
le devuelve los metodos correspondientes dependiendo de la clase. Hice un par de test pero estoy teniendo problemas con validar 
las piezas que estan rodeadas por aliedas(que no pueden moverse). 

## [1.3.0] - 03 de agosto de 2024
# Agregado
- Rediceñado los metodo de movimientos para cada pieza con sus test funcionando(Problema del anterior commit)
- Faltaria Agregar lo visto hoy en clases e empezar a implementar las excepciones y trabajar mas con el cli y chess

## [1.2.9] - 01 de agosto de 2024
# Agregado
- Este commit es un poco caotico, no funciona nada porque agregue inits en cada pieza con las direcciones a las que puede moverse cada pieza
- Hices una limpieza en los metodos del peon
- Intente mejorar la presicion del metodo deejecucion de los movimientos pero estoy teniendo complejidades que no estoy pudiendo resolver, intentare resolverlas mañana
o derectamente consultare en clase

## [1.2.8] - 31 de agosto de 2024
# Agregado
- Mismo dia que el commit anterior intentando de refactorizar(me esta costando bastante por lo visto)
- Dia diferente al commit anterior movi el  metodo mover_a a piezas.py y me tengo coverage al 100.

## [1.2.7] - 30 de agosto de 2024
# Agregado
- Refactorizando el Peon separando el metodo global en 3 diferentes
- voy a intentar de mañana seguir refactorizando

## [1.2.6] - 28 de agosto de 2024
# Agregado
- Refactorizando todas las funciones compatibles en los test de queen, bishop y rook
- Cree un archivo test_pieces.py para evitar la redundacia en los test y ahi poner los test que comparten las piezas(por el momento queen, rook y bishop)

## [1.2.5] - 27 de agosto de 2024
# Agregado
- Lo estoy agregando el dia 30 por que me olvide de agregarlo en su momento (no me acuerdo lo que hacbia hecho)

## [1.2.4] - 26 de agosto de 2024
# Agregado
- Terminado el Alfil con sus test correspondientes, coverage con 100%

## [1.2.3] - 25 de agosto de 2024
# Agregado
- Cree todos los metodos para el rey y el caballo y sus test corren al 100% (es bastante similar al de las demas piezas, por eso ni aclaro muchos metodos)
- Solo queda definir y testear bishop, pero voy bien!
- Aun sigo sin poder ver la complegidad, ni lo del circleci

## [1.2.2] - 24 de agosto de 2024
# Agregado
- Test para la reina, movimientos coverage al 100%
- Peon, sus movimientos, comer en diagonal y extras
- Testeo al 97%

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
