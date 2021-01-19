import math
import re

class Vehicle():
    DIRECTIONS = {
        "E": 0,
        "N": 90,
        "W": 180,
        "S": 270
    }

    def __init__(self):
        # coordinates
        self.location = [0, 0]
        self.waypoint = [10,1]

    def move_forward(self, distance):
        self.location[0] += self.waypoint[0] * distance
        self.location[1] += self.waypoint[1] * distance

    def move_waypoint_compass_direction(self, distance, direction):
        angle = self.DIRECTIONS[direction]
        self.move_waypoint_at_angle(distance, angle)

    def move_waypoint_at_angle(self, distance, angle):
        horizontal = math.cos(math.radians(angle)) * distance
        vertical = math.sin(math.radians(angle)) * distance
        self.waypoint[0] += int(horizontal)
        self.waypoint[1] += int(vertical)

    def rotate_waypoint(self, direction, degrees):
        if direction == "R":
            degrees *= -1
        radians = math.radians(degrees)
        new_x = self.waypoint[0] * math.cos(radians) - self.waypoint[1] * math.sin(radians)
        new_y = self.waypoint[0] * math.sin(radians) + self.waypoint[1] * math.cos(radians)
        self.waypoint = [round(new_x), round(new_y)]


    def execute_instruction(self, line):
        instruction_regex = re.compile(r"([A-Z])(-?\d+)")
        letter, number = instruction_regex.match(line).groups()
        number = int(number)
        if letter in self.DIRECTIONS:
            self.move_waypoint_compass_direction(number, letter)
        elif letter in ['L', 'R']:
            self.rotate_waypoint(letter, number)
        elif letter == 'F':
            self.move_forward(number)

    def manhattan_distance(self):
        return abs(self.location[0]) + abs(self.location[1])

if __name__ == "__main__":
    infile = open("input.txt", 'r')
    lines = infile.read().strip().split("\n")

    ship = Vehicle()

    for line in lines:
        ship.execute_instruction(line)
        
    print(ship.manhattan_distance())
