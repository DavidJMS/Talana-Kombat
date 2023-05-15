# Talana:
Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte. Cada personaje tiene 2 golpes especiales que se ejecutan con una combinación de movimientos + 1 botón de golpe.

# Botones:
- (W) Arriba.
- (S) Abajo
- (D) Derecha.
- (A) Izquierda.
- (P) Puño.
- (K) Patada.

# Combo de Tonyn Stallone:
- Combinacion (DSD + P), Energia que quita (3), Nombre del movimiento (Taladoken).
- Combinacion (SD + K), Energia que quita (2), Nombre del movimiento (Remuyuken).
- Combinacion (P o K), Energia que quita (1), Nombre del movimiento (Puño o Patada).

# Combo Arnaldor Shuatseneguer:
- Combinacion (SA + K), Energia que quita (3), Nombre del movimiento (Remuyuken).
- Combinacion (ASA + P), Energia que quita (2), Nombre del movimiento (Taladoken ).
- Combinacion (P o K), Energia que quita (1), Nombre del movimiento (Puño o Patada).

# Nota:
Parte atacando el jugador que envio una combinacion menor de botones (movimiento + golpes), en caso de empate, parte el con menos movimientos, si empatan de nuevo, inicia el con menos
golpes, si hay empate de nuevo, inicia el player 1 (total el player 2 siempre es del hermano
chico).

La secuencia completa del combate de cada jugador se entrega de una vez (consolidada
en un json)
Cada personaje tiene 6 Puntos de energía
- Un personaje muere cuando su energía llega a 0 y de inmediato finaliza la pelea
- Tony es el player 1, siempre ataca hacia la derecha (y no cambia de lado)
- Arnaldor es el player 2, siempre ataca hacia la izquierda (y no cambia de lado)
- Los personajes se atacan uno a la vez estilo JRPG, por turnos hasta que uno es
derrotado, los golpes no pueden ser bloqueados, se asume que siempre son
efectivos.
Los datos llegan como un json con botones de movimiento y golpe que se correlacionan
para cada jugada
Los movimientos pueden ser un string de largo máximo 5 (puede ser vacío)
Los golpes pueden ser un solo botón maximo (puede ser vacío)
Se asume que el botón de golpe es justo después de la secuencia de movimiento, es decir,
AADSD + P es un Taladoken (antes se movió para atrás 2 veces); DSDAA + P son
movimientos más un puño

# Preguntas generales:
1. Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se soluciona si hiciste push, y cómo si aún no hiciste. 
De ser posible, que quede solo un commit con los cambios. 
2. Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has trabajado?.
3.¿Cuál ha sido la situación más compleja que has tenido con esto? 
4. ¿Qué experiencia has tenido con los microservicios? 
5. ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué? 

# Respuestas:
1. En ambos casos usualmente si ya hice commit vuelvo a agregar el archivo con git add . y luego un git commit --amend y luego un git push, si ya mergie tengo que realizar un pull en caso de que ya haya realizado un push.
2. Git Flow. Cuando hay conflictos en muchos archivos y hay muchos contribuidores.
3. Teorica, quisiera aprender!.
4. AWS me parece mas adaptable a las necesidades y actualmente es mas popular.