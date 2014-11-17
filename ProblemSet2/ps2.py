# -*- coding: utf-8 -*-
# 6.00.2x Problem Set 2: Simulating robots

import math
import random

# import ps2_visualize
# import pylab

#For Python 2.7:
#from ps2_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using
# Python 2.7 and using most likely Python 2.6:



# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.cleaned_tiles = []
        self.dirty_tiles = []

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        tile_coordinates = (int(pos.x), int(pos.y))
        print 'Cleaned tile: ', tile_coordinates
        if (tile_coordinates in self.cleaned_tiles):
            return
        else:
            self.cleaned_tiles.append(tile_coordinates)

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        result = False

        for tile in self.cleaned_tiles:
            if (tile[0] == m) & (tile[1] == n):
                result = True
                break
        return result

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.cleaned_tiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        return Position(int(x), int(y))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if (pos.x >= self.width) | (pos.y >= self.height):
            return False
        elif (pos.x < 0) | (pos.y < 0):
            return False
        else:
            return True

class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.choice([0, 90, 180, 270])

        # clean tile that Robot is initialized on
        #room class object
        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #angle: number representing angle in degrees, 0 <= angle < 360
        #speed: positive float representing speed

        # Generate a new position
        # random_position = self.room.getRandomPosition()
        new_position = self.position.getNewPosition(self.direction, self.speed)
        self.setRobotPosition(new_position)
        #print "\n======================="
        #print 'Speed: ', self.speed
        #print 'Direction: ', self.direction
        #print 'Position x: ', self.position.x
        #print 'Position y: ', self.position.y
        #print 'Room width: ', self.room.width
        #print 'Room height: ', self.room.height

        #isPositionInRoom is a room method
        while not(self.room.isPositionInRoom(self.position)):
            # If the position is not valid, turn the robot
            #print "\n----------"
            #print 'Position not in room, re-generating...'
            current_direction = self.direction
            #print 'Changed direction: ', self.direction

            if (self.position.x < 0):
                self.position.x = 0
                if current_direction == 270:
                    self.direction = 0
                else:
                    self.direction += 90
            elif (self.position.y < 0):
                self.position.y = 0
                if current_direction == 270:
                    self.direction = 0
                else:
                    self.direction += 90
            elif (self.position.x >= self.room.width):
                self.position.x -= 1
                if current_direction == 270:
                    self.direction = 0
                else:
                    self.direction += 90
            elif (self.position.y >= self.room.height):
                self.position.y -= 1
                if current_direction == 270:
                    self.direction = 0
                else:
                    self.direction += 90

            # getNewPosition returns a Position object
            #print "\n----------"
            #print 'Re-generated position x: ', self.position.x
            #print 'Re-generated position y: ', self.position.y

        # If the position is valid, move the robot and clean the tile
        if self.room.isPositionInRoom(self.position):
            self.setRobotPosition(self.position)
            self.room.cleanTileAtPosition(self.position)

        #print 'New speed (?): ', self.speed
        #print 'New position x: ', self.position.x
        #print 'New position y: ', self.position.y
        #print 'cleaned tiles: ', self.room.cleaned_tiles
        #print "=======================\n"


# Uncomment this line to see your implementation of StandardRobot in action!
#print testRobotMovement(StandardRobot, RectangularRoom)

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    robots = createRobots(num_robots, robot_type, RectangularRoom(width, height), speed)
    total_tiles = float(width * height)
    
    print "\n============="
    print 'Total trials: ', num_trials
    print 'Num robots: ', num_robots
    print 'Min coverage: ', min_coverage, 'Robot type: ', robot_type
    print 'Width: ', width, 'Height: ', height, 'Speed: ', speed
        
    # for num_trials (iterate until num_trials is hit)
    for trial in range(num_trials):
        print 'This is trial number: ', trial 
                   
        # for a particular robot
        for robot in robots:
            print 'This is robot number: ', robot
        
            # keep track of total # of tiles vs. # of tiles cleaned
            # stop cleaning when hit the min_coverage
            percent_coverage = len(robot.room.cleaned_tiles) / total_tiles
            print 'This is percent coverage: ', percent_coverage
                
            while (percent_coverage < min_coverage):
            
                # generate a random starting position
                starting_position = robot.room.getRandomPosition()
        
                # clean starting tile
                robot.room.cleanTileAtPosition(starting_position)
            
                # move to different tile and clean
                robot.updatePositionAndClean()
                
                # update the percentage of cleaned tiles
                percent_coverage = len(robot.room.cleaned_tiles) / total_tiles
                print 'This is percent coverage: ', percent_coverage
                print "\n"
                        
                    
    
def createRobots(num_robots, robot_type, room_object, speed):
    robots = []
    for robot in range(num_robots):
        robots.append(robot_type(room_object, speed))
    return robots
    
# Uncomment this line to see how much your simulation takes on average
print  runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot)
