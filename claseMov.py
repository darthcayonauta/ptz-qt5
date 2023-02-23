'''
@class   : MoverCam
@author  : Claudio Guzmán Herrera
@version : 1.0
@package : CAM-TK

Uso, ejemplo:
ob_moves = MoverCam('192.168.78.90','admin','somePassword')

para ejecutar movimientos
-----------------------------

arriba    : ob_moves.moves(1)
abajo     : ob_moves.moves(2)
izquierda : ob_moves.moves(3)
derecha   : ob_moves.moves(4)
zoom up   : ob_moves.moves(5)
zoom down : ob_moves.moves(6)

'''

from time import sleep
from onvif import ONVIFCamera
import zeep

class MoverCam:

    def __init__(self,IP,USER,PASS):
        self.XMAX = 1
        self.XMIN = -1
        self.YMAX = 1
        self.YMIN = -1
        self.IP = IP
        self.USER = USER
        self.PASS = PASS
        self.timeout = 0.15
        self.mycam = ONVIFCamera(self.IP, 80, self.USER, self.PASS)        
    
    '''
    jump(): inicializacion componentes de camara
    @return void 
    '''
    def jump(self):

        # Create media service object
        media = self.mycam.create_media_service()
        # Create ptz service object
        self.ptz = self.mycam.create_ptz_service()

        # Get target profile
        zeep.xsd.simple.AnySimpleType.pythonvalue = self.zeep_pythonvalue
        media_profile = media.GetProfiles()[0]

        # Get PTZ configuration options for getting continuous move range
        self.request = self.ptz.create_type('GetConfigurationOptions')
        self.request.ConfigurationToken = media_profile.PTZConfiguration.token
        ptz_configuration_options = self.ptz.GetConfigurationOptions(self.request)

        self.request = self.ptz.create_type('ContinuousMove')
        self.request.ProfileToken = media_profile.token
        self.ptz.Stop({'ProfileToken': media_profile.token})

        if self.request.Velocity is None:
            self.request.Velocity = self.ptz.GetStatus({'ProfileToken': media_profile.token}).Position
            self.request.Velocity = self.ptz.GetStatus({'ProfileToken': media_profile.token}).Position
            self.request.Velocity.PanTilt.space = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].URI
            self.request.Velocity.Zoom.space = ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace[0].URI

        # Get range of pan and tilt
  
        self.XMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
        self.XMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
        self.YMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
        self.YMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min

    def zeep_pythonvalue(self, xmlvalue):
        return xmlvalue

    '''
    perform_move(): generacion de movimiento contínuo
    @ptz
    @request
    @timeout
    return void
    '''
    def perform_move(self,ptz, request, timeout):
        # Start continuous move
        ptz.ContinuousMove(request)
        # Wait a certain time
        sleep(timeout)
        # Stop continuous move
        ptz.Stop({'ProfileToken': request.ProfileToken})

    '''
    move_up(): mueves hacia arriba
    @ptz
    @request
    return void
    '''
    def move_up(self,ptz, request):
        print('move up...')
        request.Velocity.PanTilt.x = 0
        request.Velocity.PanTilt.y = self.YMAX
        self.perform_move(ptz, request, self.timeout)


    '''
    move_down(): mueves hacia abajo
    @ptz
    @request
    return void'''
    def move_down(self,ptz, request):
        print('move down...')
        request.Velocity.PanTilt.x = 0
        request.Velocity.PanTilt.y = self.YMIN
        self.perform_move(ptz, request, self.timeout)

    '''
    move_right(): mueves hacia la derecha
    @ptz
    @request
    return void'''
    def move_right(self,ptz, request):
        print('move right...')
        request.Velocity.PanTilt.x = self.XMAX
        request.Velocity.PanTilt.y = 0
        self.perform_move(ptz, request, self.timeout)


    '''
    move_left(): mueves hacia la izquierda
    @ptz
    @request
    return void'''
    def move_left(self,ptz, request):
        print('move left...')
        request.Velocity.PanTilt.x = self.XMIN
        request.Velocity.PanTilt.y = 0
        self.perform_move(ptz, request, self.timeout)

    '''
    zoom_up(): aumentas zoom
    @ptz
    @request
    return void'''
    def zoom_up(self,ptz, request):
        print('zoom up')
        request.Velocity.Zoom.x = 1
        request.Velocity.PanTilt.x = 0
        request.Velocity.PanTilt.y = 0
        self.perform_move(ptz, request, self.timeout)

    '''
    zoom_down(): disminuyes zoom
    @ptz
    @request
    return void'''
    def zoom_down(self,ptz, request):
        print('zoom down')
        request.Velocity.Zoom.x = -1
        request.Velocity.PanTilt.x = 0
        request.Velocity.PanTilt.y = 0
        self.perform_move(ptz, request, self.timeout)

    '''
    move_diagonal_sup_der(): mueves diagonal arriba
    @ptz
    @request
    ID : 7
    return void
    '''
    def move_diagonal_sup_der(self,ptz,request) :
        print("move diagonal superior derecha")
        request.Velocity.PanTilt.x = self.XMAX
        request.Velocity.PanTilt.y = self.YMAX
        self.perform_move(ptz, request, self.timeout)

    '''
    move_diagonal_inf_der(): mueves diagonal abajo
    @ptz
    @request
    ID : 8
    return void
    '''
    def move_diagonal_inf_der(self,ptz,request) :
        print("move diagonal inferior derecha")
        request.Velocity.PanTilt.x = self.XMAX
        request.Velocity.PanTilt.y = self.YMIN
        self.perform_move(ptz, request, self.timeout)

    '''
    move_diagonal_sup_izq(): mueves diagonal izquierda arriba 
    @ptz
    @request
    ID : 9
    return void
    '''
    def move_diagonal_sup_izq(self,ptz,request) :
        print("move diagonal inferior derecha")
        request.Velocity.PanTilt.x = self.XMIN
        request.Velocity.PanTilt.y = self.YMAX
        self.perform_move(ptz, request, self.timeout)

    '''
    move_diagonal_inf_izq(): mueves diagonal izquierda abajo
    @ptz
    @request
    ID : 10
    return void
    '''
    def move_diagonal_inf_izq(self,ptz,request) :
        print("move diagonal inferior izquierda")
        request.Velocity.PanTilt.x = self.XMIN
        request.Velocity.PanTilt.y = self.YMIN
        self.perform_move(ptz, request, self.timeout)

    '''
    @num = 1, hacia arriba
    @num = 2, hacia abajo
    @num = 3, hacia la izquierda
    @num = 4, hacia la derecha
    @num = 5, zoom in
    @num = 6, zoom out
    @num = 7, diagonal superior derecha
    @num = 8, diagonal inferior derecha
    @num = 9, diagonal superior izquierda
    @num = 10, diagonal inferior izquierda

    moves(): llamas al movimiento correspondiente
    @int num
    @return void
    '''
    def moves(self,num = None):
        self.jump()

        if num==1:
            self.move_up(self.ptz, self.request)
        elif num ==2:
            self.move_down(self.ptz, self.request)
        elif num==3:
            self.move_left(self.ptz, self.request)
        elif num==4:
            self.move_right(self.ptz,self.request)
        elif num==5:
            self.zoom_up(self.ptz,self.request)
        elif num==6:
            self.zoom_down(self.ptz,self.request)
        elif num == 7 :
            self.move_diagonal_sup_der(self.ptz,self.request)
        elif num == 8 :
            self.move_diagonal_inf_der(self.ptz,self.request)
        elif num == 9 :
            self.move_diagonal_sup_izq(self.ptz,self.request)
        elif num == 10 :
            self.move_diagonal_inf_izq(self.ptz,self.request)
        else:
            pass