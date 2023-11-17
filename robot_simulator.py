# Globals for the directions
# Change the values as you see fit
NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = x_pos, y_pos

    def move(self, action: str):
        actions = list(action)
        self.coordinates = list(self.coordinates)
        for action_move in actions:
            if action_move == "R":
                if self.direction == 4:
                    self.direction = 1
                else:
                    self.direction += 1
            
            if action_move == "L":
                if self.direction == 1:
                    self.direction = 4
                else:
                    self.direction -= 1
            
            if action_move == "A":
                if self.direction == NORTH:
                    self.coordinates[1] += 1
                if self.direction == EAST:
                    self.coordinates[0] += 1
                if self.direction == SOUTH:
                    self.coordinates[1] -= 1
                if self.direction == WEST:
                    self.coordinates[0] -= 1

        self.coordinates = tuple(self.coordinates)
        return actions

if __name__ == "__main__":
    robot = Robot(WEST, 0, 0)
    print(robot.coordinates)
    print(robot.move("L"))
    print(robot.coordinates)



