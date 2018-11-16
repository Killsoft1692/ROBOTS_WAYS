class Robot:
    __slots__ = 'coordinates'
    """
    Basic robot with coordinates(X, Y, angle)
    """
    def __init__(self):
        self.coordinates = [0, 0, 0]

    async def choose_direction(self, step):
        """
        Get direction in order to given angle
        """
        if abs(self.coordinates[2]) < 90:
            self.coordinates[0] += int(step[1][0])
        elif 90 <= abs(self.coordinates[2]) < 180:
            if self.coordinates[2] < 0:
                self.coordinates[1] += int(step[1][0])
            else:
                self.coordinates[1] -= int(step[1][0])
        elif 180 <= abs(self.coordinates[2]) < 270:
            if self.coordinates[2] < 0:
                self.coordinates[0] -= int(step[1][0])
            else:
                self.coordinates[0] += int(step[1][0])
        else:
            if self.coordinates[2] < 0:
                self.coordinates[1] -= int(step[1][0])
            else:
                self.coordinates[1] += int(step[1][0])

    async def walking(self, route):
        """
        Implementing of walking
        """
        assert len(route) > 1 and route[0][0] == 'START', 'This route isn\'t valid'
        steps = []
        for step in route:
            steps.append(step[0])
            if self.coordinates[2] == 360:
                self.coordinates[2] = 0
            if 'START' == step[0]:
                self.coordinates = [int(step[1][0]), int(step[1][1]), 0]
            elif 'TURN_RIGHT' == step[0]:
                self.coordinates[2] += 90
            elif 'TURN_LEFT' == step[0]:
                self.coordinates[2] -= 90
            elif 'GO' == step[0]:
                await self.choose_direction(step)
        print('MY WAY IS:', ';'.join(steps), self.coordinates, '\n')
