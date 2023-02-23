# ptz-qt5 , V1.0
Requerimientos:
--------------------------------------------------------------
1. PyQT5
2. Bibliotecas numpy,opencv (cv2), onvif, zeep, time, threading



#Clase MoverCam
Uso, ejemplo:
ob_moves = MoverCam(IP_PTZ,USER,MY_PASSWORD)

para ejecutar movimientos
-----------------------------

arriba                      :  ob_moves.moves(1)
abajo                       :  ob_moves.moves(2)
izquierda                   :  ob_moves.moves(3)
derecha                     :  ob_moves.moves(4)
zoom up                     :  ob_moves.moves(5)
zoom down                   :  ob_moves.moves(6)
diagonal superior derecha   :  ob_moves.moves(7)
diagonal inferior derecha   :  ob_moves.moves(8)
diagonal superior izquierda :  ob_moves.moves(9)
diagonal inferior izquierda :  ob_moves.moves(10)
