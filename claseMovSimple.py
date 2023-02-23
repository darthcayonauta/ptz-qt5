from time import sleep
from onvif import ONVIFCamera
import zeep

class MoverCamSimple:

    def __init__(self):
        self.XMAX = 1
        self.XMIN = -1
        self.YMAX = 1
        self.YMIN = -1
        self.IP = '192.168.78.90'
        self.USER = 'admin'
        self.PASS = 'Admin321'
        self.PORT_PROTOCOL = 554

    def zeep_pythonvalue(self, xmlvalue):
        return xmlvalue

    def moves(self):
        mycam = ONVIFCamera(self.IP, 80, self.USER, self.PASS)
        media = mycam.create_media_service()
        # Create ptz service object
        self.ptz = mycam.create_ptz_service()

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
        # NOTE: X and Y are velocity vector
        #global XMAX, XMIN, YMAX, YMIN
        self.XMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
        self.XMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
        self.YMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
        self.YMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min
        

    def perform_move(self,timeout):
        # Start continuous move
        self.ptz.ContinuousMove(self.request)
        # Wait a certain time
        sleep(timeout)
        # Stop continuous move
        self.ptz.Stop({'ProfileToken': self.request.ProfileToken})

    def move_up(self,timeout=1):
        print('move up...')
        self.request.Velocity.PanTilt.x = 0
        self.request.Velocity.PanTilt.y = self.YMAX
        self.perform_move(self.ptz, self.request,timeout)

    def move_down(self,timeout=1):
        print('move down...')
        self.request.Velocity.PanTilt.x = 0
        self.request.Velocity.PanTilt.y = self.YMIN
        self.perform_move(self.ptz, self.request,timeout)

    def move_right(self,timeout=1):
        print('move right...')
        self.request.Velocity.PanTilt.x = self.XMAX
        self.request.Velocity.PanTilt.y = 0
        self.perform_move(self.ptz, self.request,timeout)

    def move_left(self,timeout=1):
        print('move left...')
        self.request.Velocity.PanTilt.x = self.XMIN
        self.request.Velocity.PanTilt.y = 0
        self.perform_move(self.ptz, self.request,timeout)

    def zoom_up(self,timeout=1):
        print('zoom up')
        self.request.Velocity.Zoom.x = 1
        self.request.Velocity.PanTilt.x = 0
        self.request.Velocity.PanTilt.y = 0
        self.perform_move(self.ptz, self.request,timeout)

    def zoom_down(self,timeout=1):
        print('zoom down')
        self.request.Velocity.Zoom.x = -1
        self.request.Velocity.PanTilt.x = 0
        self.request.Velocity.PanTilt.y = 0
        self.perform_move(self.ptz, self.request,timeout)


    # VER MOVIMIENTO

    # Create media service object

if __name__=='__main__':
    ob = MoverCamSimple()
    ob.moves()
    ob.move_up(5)

