from map import Map


class Camera:
    def __init__(self, ):
        """class for camera"""
        # Camera scrolling speed
        self.camera_speed = 12

    def do_camera(self, moving_left: bool, moving_right: bool, level: Map):
        pass
        # moving_left will be true if player is moving left
        # moving_right will be true if player is moving right
        # level.width is total no. of tiles in map
        # change value of level.x and see what happens
