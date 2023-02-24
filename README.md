# ptz-qt5 , V1.0
Requerimientos:
--------------------------------------------------------------
1. PyQT5
2. Bibliotecas numpy,opencv (cv2), onvif, zeep, time, threading

# Interfaz Principal


#Clase MoverCam
Uso, ejemplo:
ob_moves = MoverCam(IP_PTZ,USER,MY_PASSWORD)

para ejecutar movimientos
-----------------------------

1. arriba                      :  ob_moves.moves(1)
2. abajo                       :  ob_moves.moves(2)
3. izquierda                   :  ob_moves.moves(3)
4. derecha                     :  ob_moves.moves(4)
5. zoom up                     :  ob_moves.moves(5)
6. zoom down                   :  ob_moves.moves(6)
7. diagonal superior derecha   :  ob_moves.moves(7)
8. diagonal inferior derecha   :  ob_moves.moves(8)
9. diagonal superior izquierda :  ob_moves.moves(9)
10. diagonal inferior izquierda :  ob_moves.moves(10)

# Uso de Joystick
también se puede añadir o combinar las funciones de pygame para el uso de mandos o joysticks, ver archivo 'joystickPtz.py'
# Uso 
La clase principal de este archivo se llama Mando() y tiene los siguientes parámetros de entrada :
1. user : usuario de la cámara PTZ
2. passwd : password de del usuario de la cámara PTZ
3. ip : ip de la cámara PTZ

Se debe tener un mando o joystick conectado al PC y para su ejecución, escribir lo siguiente:

Uso, ejemplo:

mando = Mando('admin','Admin321','192.168.78.90')

mando.process()

