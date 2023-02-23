import pygame
from claseMov import *
import threading
import time

class Mando:
    def __init__(self) :
       pygame.joystick.init()
       self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
       self.clock     = pygame.time.Clock()
       self.user    = 'admin'
       self.passw   = 'Admin321'
       self.ip      = '192.168.78.90'
       self.obj_mover = MoverCam(self.ip,self.user,self.passw)


    def process(self) :
        print(self.joysticks)
        pygame.init()
        
        while True :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    break

                #presionando los botonos del 1 al 4
                if event.type == pygame.JOYBUTTONDOWN :
                    if pygame.joystick.Joystick(0).get_button(0) :
                        print("Presionaste el Boton 1 / Derecha Arriba")
                        self.diagonalDerSup()

                    elif pygame.joystick.Joystick(0).get_button(1) :
                        print("Presionaste el Boton 2 / Derecha Abajo")
                        self.diagonalDerInf()

                    elif pygame.joystick.Joystick(0).get_button(2) :
                        print("Presionaste el Boton 3 / Izquierda Inferior")
                        self.diagonalIzqInf()


                    elif pygame.joystick.Joystick(0).get_button(3) :
                        print("Presionaste el Boton 4 / Izquierda Arriba")
                        self.diagonalIzqSup()

                    elif pygame.joystick.Joystick(0).get_button(4) :
                        print("Presionaste el Boton 5 (L1)/ Adjuste 1")
                        #self.diagonalIzqSup()
                    
                    elif pygame.joystick.Joystick(0).get_button(5) :
                        print("Presionaste el Boton 6 (R1)/ ZOOM In")
                        self.zoomIn()

                    elif pygame.joystick.Joystick(0).get_button(6) :
                        print("Presionaste el Boton 7 (L2)/ Adjuste 2")
                        #self.diagonalIzqSup()

                    elif pygame.joystick.Joystick(0).get_button(7) :
                        print("Presionaste el Boton 8 (R2)/ ZOOM Out")
                        self.zoomOut()


                if event.type == pygame.JOYAXISMOTION :
                    x_speed = round(pygame.joystick.Joystick(0).get_axis(0))
                    y_speed = round(pygame.joystick.Joystick(0).get_axis(1))
       
                    if x_speed == 0 and y_speed == -1 :
                        time.sleep(1)
                        print("Direccionando hacia ARRIBA")
                        self.moveUp()

                    elif x_speed == 0 and y_speed == 1 :
                        time.sleep(1)
                        print("Direcionando hacia ABAJO")
                        self.moveDown()

                    elif x_speed ==1 and y_speed == 0 :
                        time.sleep(1)
                        print("Direcionando hacia la DERECHA")
                        self.moveRight()

                    elif x_speed == -1 and y_speed == 0 :
                        time.sleep(1)
                        print("Direcionando hacia la IZQUIERDA")
                        self.moveLeft()

                    elif x_speed == -1 and y_speed == -1 :
                        time.sleep(1)
                        print("Direcionando hacia la IZQUIERDA y ARRIBA")
                        self.diagonalIzqSup()

                    elif x_speed == 1 and y_speed == -1 :
                        print("Direcionando hacia la DERECHA y ARRIBA")
                        self.diagonalDerSup()

                    elif x_speed == -1 and y_speed == 1 :
                        time.sleep(1)
                        print("Direcionando hacia la IZQUIERDA y ABAJO")
                        self.diagonalIzqInf()
                    
                    elif x_speed == 1 and y_speed == 1 :
                        time.sleep(1)
                        print("Direcionando hacia la DERECHA y ABAJO")
                        self.diagonalDerInf()

    #movimientos PTZ // Calling movement functions
    def moveUp(self):
        #self.obj_mover.moves(1)
        hilo = threading.Thread(target=self.obj_mover.moves,kwargs={'num':1})
        hilo.start()

    def moveDown(self):
        #self.obj_mover.moves(2)
        hilo = threading.Thread(target=self.obj_mover.moves,kwargs={'num':2})
        hilo.start()
    
    def moveLeft(self):
        #self.obj_mover.moves(3)
        hilo = threading.Thread(target=self.obj_mover.moves,kwargs={'num':3})
        hilo.start()

    def moveRight(self):
        #self.obj_mover.moves(4)
        hilo = threading.Thread(target=self.obj_mover.moves,kwargs={'num':4})
        hilo.start()

    def zoomIn(self) :
        #self.obj_mover.moves(5)
        hilo = threading.Thread(target=self.obj_mover.moves,kwargs={'num':5})
        hilo.start()

    def zoomOut(self) :
        #self.obj_mover.moves(6)
        hilo = threading.Thread(target=self.obj_mover.moves,kwargs={'num':6})
        hilo.start()

    def diagonalIzqSup(self) :
        hilo = threading.Thread(target=self.obj_mover.moves, kwargs={'num':9})
        hilo.start()

    def diagonalIzqInf(self) :
        hilo = threading.Thread(target=self.obj_mover.moves, kwargs={'num':10})
        hilo.start()

    def diagonalDerSup(self) :
        hilo = threading.Thread(target=self.obj_mover.moves, kwargs={'num':7})
        hilo.start()

    def diagonalDerInf(self) :
        hilo = threading.Thread(target=self.obj_mover.moves, kwargs={'num':8})
        hilo.start()

if __name__ == '__main__' :
    mando = Mando()
    mando.process()