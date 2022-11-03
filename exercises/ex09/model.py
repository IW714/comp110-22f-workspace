"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730614632"  


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Returns the distance between two points."""
        return sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Reassign the object's location attribute the result of adding the self object's location with its direction."""
        self.location = self.location.add(self.direction)
        if self.is_infected() is True: 
            self.sickness += 1
            if self.sickness > constants.RECOVERY_PERIOD:
                self.immunize()
    
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable() is True:
            return "gray"
        elif self.is_infected() is True:
            return "lime"
        elif self.is_immune() is True:
            return "magenta"
        return "black"

    def contract_disease(self) -> None: 
        """Changes cell sickness attribute to infected."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Returns True if cell is vulnerable to infection."""
        if self.sickness == constants.VULNERABLE:
            return True
        else: 
            return False 
    
    def is_infected(self) -> bool:
        """Returns True if cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else: 
            return False 

    def contact_with(self, other: Cell) -> None:
        """Checks if infection is spread from one cell to another on contact."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        if self.is_vulnerable() and other.is_infected():
            self.contract_disease()

    def immunize(self) -> None:
        """Turns cell immune."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Returns True if cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else: 
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected >= cells or infected <= 0:
            raise ValueError("Some number of cells must begin infected and not all cells can begin in an infected state.")
        if immune >= cells or immune < 0: 
            raise ValueError("Total number of immune cells cannot exceed total number of cells.")
        self.population = []
        i: int = 0
        j: int = 0
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if i < infected:
                cell.contract_disease()
                i += 1
            if j < immune:
                cell.immunize()
                j += 1
            self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population: 
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random() 
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed 
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Compare the distance between every two Cell objects' location attributes in the population."""
        for i in range(len(self.population)):
            for j in range(i + 1, len(self.population)):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
            
    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False 
        return True