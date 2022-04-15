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
  

  Opciones:
  Codigo para usar el moveit_commander. Se encuentra en: Moveit Commander Scripting del tutorial de moveit
