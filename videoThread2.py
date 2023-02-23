from PyQt5.QtCore import QThread,QObject,pyqtSignal,pyqtSlot
import numpy as np
import cv2
import datetime

class CamsTh(QObject) :
    ch_signal = pyqtSignal(np.ndarray)

    def __init__(self, url) :

        super().__init__()
        self.url = url
        self.cap = cv2.VideoCapture(url)
        self.w = 960
        self.h = 540
        self.font = cv2.FONT_ITALIC
  
    #@pyqtSlot
    def run(self):
  
        while True :
            ret , frame = self.cap.read()
      
            if ret :

                dt1 = datetime.datetime.now()
                dt = dt1.strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]
                osd1 = 'IP CAM ' + dt
                #frame =cv2.putText(frame, osd1,
                #            (10, 100),
                #            self.font, 1,
                #            (0, 0, 0),
                #            3, cv2.LINE_8)
                frame = cv2.resize(frame,dsize=(self.w,self.h), interpolation=cv2.INTER_CUBIC)
                self.ch_signal.emit(  cv2.cvtColor( frame , cv2.COLOR_BGR2RGB ) )

            else :
                self.cap = cv2.VideoCapture( self.url )
        
            #self.ch_signal.emit()
