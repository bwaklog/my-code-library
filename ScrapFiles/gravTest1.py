# Planetary Object
import numpy as np
# import pygame


class celestialObject(object):

    def __init__(self, type, name, mass, radius):
        self.type = type
        self.name = name
        self.mass = mass
        self.radius = radius

    def celestialDensity(self):
        mass, radius = self.mass, self.radius
        return (3 * mass) / (4*np.pi*(radius**3))

    def newtonsGravitationForce(self, celestialObject, celestialDistance):
        gConstant = 6.67430E-11
        m1, r1 = self.mass, self.radius
        m2, r2 = celestialObject.mass, celestialObject.radius

        newtonGravitationalForce = (gConstant * m1 * m2) / celestialDistance**2
        return newtonGravitationalForce

    def orbitalVelocity(self, celestialObject, celestialDistance):
        gConstant = 6.67430E-11
        mc, rc = celestialObject.mass, celestialObject.radius
        mo, ro = self.mass, self.radius

        orbitalVelocity = ((gConstant * mc)/celestialDistance)**0.5
        return orbitalVelocity


class starLuminous(object):
    def __init__(self, type, name, mass, radius):
        self.type = type
        self.name = name
        self.mass = mass
        self.radius = radius

    def starLuminousDensity(self):
        mass, radius = self.mass, self.radius
        return (3 * mass) / (4*np.pi*(radius**3))

    def newtonsGravitationForce(self, celestialObject, celestialDistance):
        gConstant = 6.67430E-11
        m1, r1 = self.mass, self.radius
        m2, r2 = celestialObject.mass, celestialObject.radius
        newtonGravitationalForce = (gConstant * m1 * m2) / celestialDistance**2
        return newtonGravitationalForce


Earth = celestialObject('planet', 'Earth', 5.972E24, 6.371E6)
Sol = starLuminous('star', 'Sol', 1.989E30, 6.9634E8)

# 1.1509E11
print(Sol.newtonsGravitationForce(Earth, 1.5109E11))
print(Earth.orbitalVelocity(Sol, 1.5109E11))

# Creating new celestial objects and calculating force of attraction between them

object1 = celestialObject('object', 'Object_1', 10, 5)
print(object1.newtonsGravitationForce(Earth, 15E3))
