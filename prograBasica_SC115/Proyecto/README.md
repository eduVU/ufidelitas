Complejo Futbolístico Los Mejengueros

Como parte de la digitalización de modelos de negocio, el complejo
futbolístico “Los Mejengueros” ha decido establecer su negocio en la
WEB, razón por la cual ustedes han sido contratados para desarrollar una
aplicación en Python como primer paso a la modernización. El complejo
cuenta con un Administrador, quién es el responsable de activar
clientes, llevar estadísticas de las reservas y llevar la caja diaria.
Los clientes pueden inscribirse brindando los datos básicos, sin
embargo, pueden realizar reservas únicamente si son aceptados (estar
activos) por el Administrador. Cuando un cliente quiere realizar una
reserva, se solicita el número de cancha, el día y la hora;
posteriormente el Administrador revisa la reserva y si los datos están
en orden, procede a confirmar la cancha. El local cuenta con tres
canchas de fútbol 5, una de fútbol 7 y una cancha para fútbol 11, todas
habilitadas los 7 días de la semana en horario de 10 am a 9 pm. El valor
de cada cancha se desglosa de la siguiente forma:

1) Cancha de fútbol 5: 30 mil colones.</li>
2) Cancha de fútbol 7: 50 mil colones.</li>
3) Cancha de fútbol 11: 95 mil colones.</li>

Módulo 1: Módulo de Clientes

En este módulo se podrá realizar lo siguiente:

1. El programa debe tener un menú con las siguientes opciones:
   a. Módulo de Clientes: En este módulo se podrá realizar lo siguiente:

i. Registrar un nuevo cliente, solicitando la siguiente información:

1. Identificación.
2. Nombre
3. Primer Apellido
4. Segundo Apellido.
5. Teléfono
6. Correo
7. Activo o Inactivo (Por defecto Inactivo)

ii. Actualizar un cliente existente: Permitiendo modificar toda la información del cliente, únicamente dejando intacto la Identificación.

iii. Consultar un cliente: Solicitando la identificación, desplegará la información básica del cliente.

iv. Listado de reservas: mediante el cual el cliente podrá revisar las reservas que ha realizado en el complejo.

Nota: Al registrar un nuevo cliente, se debe validar que este no exista previamente; además los clientes deben ser persistentes, no se deben perder al cerrar el programa.

Valor 25 pts.

Módulo 2: Módulo de Administrador

En este módulo se podrá activar los clientes y confirmar las citas.
En este módulo, el administrador contará con un menú de dos opciones:

i. Activar Clientes (únicamente un cliente activo puede realizar reservas).

ii. Revisar reservas: en esta opción se desplegarán todas las reservas realizadas para que sean verificadas y aceptadas por el Administrador. Únicamente se cuentan válidas las reservas confirmadas.

Nota: Se deben validar que las reservas no tengan conflictos entre sí.

Valor 25 pts.

Módulo 3: Módulo de Reserva Descripción

En este módulo el cliente puede realizar una reserva de una cancha, brindando la información requerida.
El cliente seleccionará la cancha que desea utilizar, el día y la hora y realizará la reserva respectiva.

Al finalizar la reserva, el sistema imprimirá un número de solicitud indicando el monto a pagar según los gastos administrativos, la cancha y un 13% de IVA.

Nota: La reserva previa no debe entrar en conflicto con ninguna reserva confirmada.

Opcional: Para desplegar la información de la cancha seleccionada al cliente, puede imprimir los datos en la pantalla en una matriz, marcando con una “X” los horarios reservados.

Valor 25 pts.