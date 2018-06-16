class Camera():
    '''
    The Game Camera that follows the player around the map.
    '''
    def __init__(self, width, height, x, y):
        '''
        width = the width of the window viewing the game map

        height = the height of the window viewing the game map

        (x, y) = the x and y coordinates of the game camera
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def move_camera(self, target_x, target_y, fov_recompute, game_map):
        '''
        Moves the camera based on a target on the game map and then
        recomputes the fov
        '''
        x = int(target_x - self.width / 2)
        y = int(target_y - self.height / 2)

        if x < 0: x = 0
        if y < 0: y = 0
        if x > game_map.width - self.width - 1:
            x = game_map.width - self.width - 1
        if y > game_map.height - self.height - 1:
            y = game_map.height - self.height - 1

        if x != self.x or y != self.y:
            fov_recompute = True

        (self.x, self.y) = (x, y)

    def to_camera_coordinates(self, x, y):
        '''
        Translates the coordinates from map to camera
        '''
        # (x, y) have to be int because tcod.map_is_in_fov(m, x, y)
        # gives a wrong type error because it sees (x, y) as a
        # float instead of an int which it requires.
        (x, y) = (int(x - self.x), int(y - self.y))

        if (x < 0 or y < 0 or x >= self.width or y >= self.height):
            return (None, None)

        return (x, y)