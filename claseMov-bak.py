from time import sleep
from onvif import ONVIFCamera
import zeep

class MoverCam:

    def __init__(self):
        self.XMAX = 1
        self.XMIN = -1
        self.YMAX = 1
        self.YMIN = -1
        self.IP = '192.168.78.225'
        self.USER = 'admin'
        self.PASS = 'Admin321'
        self.PORT_PROTOCOL = 554

    def zeep_pythonvalue(self, xmlvalue):
        return xmlvalue

    def perform_move(self,ptz, request, timeout):
        # Start continuous move
        ptz.ContinuousMove(request)
        # Wait a certain time
        #sleep(timeout)
        # Stop continuous move
        ptz.Stop({'ProfileToken': request.ProfileToken})

    def move_up(self,ptz, request, timeout=1):
        print('move up...')
        request.Velocity.PanTilt.x = 0
        request.Velocity.PanTilt.y = self.YMAX
        self.perform_move(ptz, request, timeout)

    def move_down(self,ptz, request, timeout=1):
        print('move down...')
        request.Velocity.PanTilt.x = 0
        request.Velocity.PanTilt.y = self.YMIN
        self.perform_move(ptz, request, timeout)

    def move_right(self,ptz, request, timeout=1):
        print('move right...')
        request.Velocity.PanTilt.x = self.XMAX
        request.Velocity.PanTilt.y = 0
        self.perform_move(ptz, request, timeout)

    def move_left(self,ptz, request, timeout=1):
        print('move left...')
        request.Velocity.PanTilt.x = self.XMIN
        request.Velocity.PanTilt.y = 0
        self.perform_move(ptz, request, timeout)

    def zoom_up(self,ptz, request, timeout=1):
        print('zoom up')
        request.Velocity.Zoom.x = 1
        request.Velocity.PanTilt.x = 0
        request.Velocity.PanTilt.y = 0
        self.perform_move(ptz, request, timeout)

    def zoom_dowm(self,ptz, request, timeout=1):
        print('zoom down')
        request.Velocity.Zoom.x = -1
        request.Velocity.PanTilt.x = 0
        request.Velocity.PanTilt.y = 0
        self.perform_move(ptz, request, timeout)

    def continuous_move(self):

        mycam = ONVIFCamera(self.IP, 80, self.USER, self.PASS)
        # VER MOVIMIENTO

        # Create media service object
        media = mycam.create_media_service()
        # Create ptz service object
        ptz = mycam.create_ptz_service()

        # Get target profile
        zeep.xsd.simple.AnySimpleType.pythonvalue = self.zeep_pythonvalue
        media_profile = media.GetProfiles()[0]

        # Get PTZ configuration options for getting continuous move range
        request = ptz.create_type('GetConfigurationOptions')
        request.ConfigurationToken = media_profile.PTZConfiguration.token
        ptz_configuration_options = ptz.GetConfigurationOptions(request)

        request = ptz.create_type('ContinuousMove')
        request.ProfileToken = media_profile.token
        ptz.Stop({'ProfileToken': media_profile.token})

        if request.Velocity is None:
            request.Velocity = ptz.GetStatus({'ProfileToken': media_profile.token}).Position
            request.Velocity = ptz.GetStatus({'ProfileToken': media_profile.token}).Position
            request.Velocity.PanTilt.space = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].URI
            request.Velocity.Zoom.space = ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace[0].URI

        # Get range of pan and tilt
        # NOTE: X and Y are velocity vector
        #global XMAX, XMIN, YMAX, YMIN
        self.XMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
        self.XMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
        self.YMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
        self.YMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min

        for i in range(10):
            self.zoom_up(ptz, request)

        for i in range(10):
            self.zoom_dowm(ptz, request)
        # move right
        for i in range(10):
            self.move_right(ptz, request)

        # move left
        for i in range(10):
            self.move_left(ptz, request)

        # Move up
        for i in range(10):
            self.move_up(ptz, request)

        # move down
        for i in range(10):
            self.move_down(ptz, request)


    def continuous_move2(self,num = None):

        mycam = ONVIFCamera(self.IP, 80, self.USER, self.PASS)
        # VER MOVIMIENTO

        # Create media service object
        media = mycam.create_media_service()
        # Create ptz service object
        ptz = mycam.create_ptz_service()

        # Get target profile
        zeep.xsd.simple.AnySimpleType.pythonvalue = self.zeep_pythonvalue
        media_profile = media.GetProfiles()[0]

        # Get PTZ configuration options for getting continuous move range
        request = ptz.create_type('GetConfigurationOptions')
        request.ConfigurationToken = media_profile.PTZConfiguration.token
        ptz_configuration_options = ptz.GetConfigurationOptions(request)

        request = ptz.create_type('ContinuousMove')
        request.ProfileToken = media_profile.token
        ptz.Stop({'ProfileToken': media_profile.token})

        if request.Velocity is None:
            request.Velocity = ptz.GetStatus({'ProfileToken': media_profile.token}).Position
            request.Velocity = ptz.GetStatus({'ProfileToken': media_profile.token}).Position
            request.Velocity.PanTilt.space = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].URI
            request.Velocity.Zoom.space = ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace[0].URI

        # Get range of pan and tilt
        # NOTE: X and Y are velocity vector
        #global XMAX, XMIN, YMAX, YMIN
        self.XMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
        self.XMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
        self.YMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
        self.YMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min

        '''
        for i in range(10):
            self.zoom_up(ptz, request)

        for i in range(10):
            self.zoom_dowm(ptz, request)
        # move right
        for i in range(10):
            self.move_right(ptz, request)

        # move left
        for i in range(10):
            self.move_left(ptz, request)

        # Move up
        for i in range(10):
            self.move_up(ptz, request)

        # move down
        for i in range(10):
            self.move_down(ptz, request)

    '''
        if num==1:
            self.move_up(ptz, request)
        elif num ==2:
            self.move_down(ptz, request)
        elif num==3:
            self.move_left(ptz, request)
        elif num==4:
            self.move_right(ptz,request)
        else:
            pass
    




if __name__=='__main__':
    ob = MoverCam()
    ob.continuous_move()