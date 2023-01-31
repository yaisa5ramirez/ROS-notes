# ROS2 notes

Colcon es para poder compilar todo el workspace y poder ver todas las carpetas. Colcon es el reemplazo de catkin make, catkin tools y ament tools. Al compilar, colcon crea build, install y log. Ya no existe el devel

Ament: sistema de compilacion
Colcon: herramienta de compilacion

Todos los paquetes se crean sobre src

Siempre que inicie el ws debo correr el . /.bash  para que reconozca todos los paquetes

Siempre que modifique el ws debo correr colcon build para compilar. Puedo compilar unicamente el packete o archivo que modifique o cree con eso no se demora tanto.  colcon build --packages-select [package_name]

Un paquete de ROS2 creado con Pyhton debe tener: package.xml, setup.py, setup.cfg y /package_name (directorio con el mismo nombre dle paquete que contiene el archivo 
__init__.py)

La carpeta se debe llamar igual al nodo (recomendado)

** Crear un paquete ** y dentro de el un ejecutable llamado my_node que ya se crea con un codigo base para saludar. 

ros2 pkg create --build-type ament_python --node-name my_node my_first_ros2_package

** Correr un nodo **: ros2 run [package_name] [executable_name]

** Comandos nodos y topicos: ** 

ros2 node list
ros2 node info [node_name]
rqt_graph : para visualizar el grafo de computacion
ros2 topic list
ros2 topic echo [topic] :dice que se esta punlicando en el topico

Publisher y suscriber deben manejar el mismo tipo de mensaje, para conocerlo: 
ros2 topic info [topic]

Para conocer la estructura de un mensaje, 
ros2 interface show [msg type]
 
si es por ejemplo de tipo geometry_msgs/msg/Twist :

ros2 interface show geometry_msgs/msg/Twist

** Para publicar datos en un topico activo **
ros2 topic pub [topic] [msg_type] [args]

donde args son los datos que se pasaran. Si se pone --once antes de [topic], una vez se haya publicado el mensaje se deja de publicar. En cambio, si se pone --rate se mantedra un flujo constante del comando

** Escribir un subscriber y un publisher **

Mirar archivos de ejemplo, *publisher_ej2* y *subscriber_ej2*. En estos, ambos nodos se asocian a un mismo topico. 

En el archivo package.xml se deben incluir las dependencias de los nodos

En el archivo setup.py se pueden incluir el nombre del nodo para correrlo en consola directamente. Los campos maintainer, mantainer email, description y license deben ser iguales en el setup.py y en el package.xml

Antes de construir el paquete ** asegurarse de que las dependencias estan completas corriendo**: rosdep install -i --from-path src --rosdistro humble -y

**Construir el paquete**: 
colcon build --packages-select [nombre_paquete]

Correr .install/setup.bash

Ya se pueden correr los nodos

Servicios

Otra forma para que los nodos se comuniquen entre si, pueden enviarse solicitudes y respuestas entre ellos (arquitectura cliente-servidor). La diferencia con los topicos es que los servicios (servidores) solo le dan datos al cliente cuando este lo llame especificamente.

** Comandos servicios: **
ros2 service list
ros2 service type [service_name]

Para ver los tipos de todos los servicios: 
ros2 service list -t

Encontrar todos los servicios de un tipo especifico

ros2 service find <type_name>

Para ver lo que necesita un servicios para solicitarlo

ros2 interface show <type_name>

Para llamar/solicitar a un servicio

ros2 service call [service_name] [arguments]

los argumentos deben ir de la forma dada al correr el comando interface show de arriba

*Ej*:

ros2 pkg create --build-type ament_python py_srvcli --dependencies
rclpy example_interfaces

El --dependencies agrega automaticamente las lineas de dependencia necesarias a package.xml

Preguntas

Cuando debo hacer . install/local_setup.bash

No me funciona la parte final del sevicio cuando corro ros2 run py_srvcli service

https://app.theconstructsim.com/Desktop

Comandos útiles:

Abrir archivos para editar:
gedit [nombre_archivo]

Ctrl + H: mostrar archivos ocultos

# ROS-notes

Nano: editor de Linux. Comando: nano.  Para salir de nano: Ctrl + X |Y|Enter
Cd: change directory 
rmdir: remove filder


1. Crear paquete: 
catkin_create_pkg <nombre_paquete> <dependencias separadas por espacio>
Ejemplo paquete llamado visión con 3 dependencias: 
catkin_create_pkg vision std_msgs rospy roscpp
  
Compilar el paquete:
Es major usar catkin_make que catkin_build a pesar de que hacen lo mismo
Una vez creo el paquete se crean las carpetas: devel src ….

 2.  Crear Nodos: 
  Mirar ejemplos publisher y subscriber
  A los tópicos solo se les puede publicar un tipo de mensaje 
. devel/setup.bash   #super necesario, es de comportamiento interno del computador

  
3. Ejecutar la aplicación 
3.1 Opcion 1: correr los nodos por separado uno por uno
3.2 Opcion 2: Ejecutar todos los nodos al tiempo:  
Roslaunch files: nombro todos los nodos que quiero ejecutar 
Debo crear la carpeta launch en la cual voy a poner los launch files 


Todos los pasos están en la presentación:
  https://docs.google.com/presentation/d/1dcxUdE2Qhh68PRWdMzYk-tVv3kMFFG7CdgbKspdl4XU/edit#slide=id.g11853f65f98_4_38 
  Autor: Cristobal Arroyo

  LINKS: 
  
  http://docs.ros.org/en/indigo/api/moveit_tutorials/html/doc/ros_visualization/visualization_tutorial.html 
  https://arxiv.org/pdf/1909.05035.pdf 
  https://docs.ipswitch.com/MOVEit/DMZ8.1/Manuals/MOVEit%20DMZ%20Administrator's%20Guide.pdf 
  http://wiki.ros.org/moveit_msgs 
  http://docs.ros.org/en/kinetic/api/moveit_tutorials/html/doc/motion_planning_pipeline/motion_planning_pipeline_tutorial.html#:~:text=In%20MoveIt%2C%20the%20motion%20planners,(e.g.%20for%20time%20parameterization). 
  https://slaterobotics.medium.com/how-to-implement-ros-control-on-a-custom-robot-748b52751f2e
  

  Opciones:
  Crear un .launch para ver el estado actual de los joints y la solucion de cinematica inversa. 
 http://docs.ros.org/en/melodic/api/moveit_tutorials/html/doc/robot_model_and_robot_state/robot_model_and_robot_state_tutorial.html
  
  Planear un goal y visualizarlo
  http://docs.ros.org/en/melodic/api/moveit_tutorials/html/doc/motion_planning_api/motion_planning_api_tutorial.html
  
  
  
  Desde cero:
  
  Crear xacros e iniciar todo usando el Moveit Setup Assistant
  http://docs.ros.org/en/kinetic/api/moveit_tutorials/html/doc/setup_assistant/setup_assistant_tutorial.html
  
