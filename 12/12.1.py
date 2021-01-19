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
        # degrees
        self.angle = 0
        # coordinates
        self.location = [0, 0]

    def move_forward(self, distance):
        self.move_at_angle(distance, self.angle)

    def move_compass_direction(self, distance, direction):
        angle = self.DIRECTIONS[direction]
        self.move_at_angle(distance, angle)

    def move_at_angle(self, distance, angle):
        horizontal = math.cos(math.radians(angle)) * distance
        vertical = math.sin(math.radians(angle)) * distance
        self.location[0] += int(horizontal)
        self.location[1] += int(vertical)

    def rotate(self, direction, degrees):
        if direction == "R":
            degrees *= -1
        self.angle += degrees
        self.angle = self.angle % 360

    def execute_instruction(self, line):
        instruction_regex = re.compile(r"([A-Z])(-?\d+)")
        letter, number = instruction_regex.match(line).groups()
        number = int(number)
        if letter in self.DIRECTIONS:
            self.move_compass_direction(number, letter)
        elif letter in ['L', 'R']:
            self.rotate(letter, number)
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
