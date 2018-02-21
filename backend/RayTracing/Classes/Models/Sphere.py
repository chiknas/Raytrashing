import math

from RayTracing.Classes.Models.Color import Color
from RayTracing.Classes.Models.MathUtil import MathUtil
from RayTracing.Classes.Models.Intersection import Intersection
from RayTracing.Classes.Models.Object3D import Object3D
from RayTracing.Classes.Models.Vector import Vector


class Sphere(Object3D):

    def __init__(self, x=0, y=0, z=0, radius=0, color=Color(), specular=50, reflection=0.1):
        super().__init__(x, y, z, color, specular, reflection)
        self.radius = radius

    def __init__(self, v=Vector(0, 0, 0), radius=0, color=Color(), specular=50, reflection=0.1):
        super().__init__(v, color, specular, reflection)
        self.radius = radius

    def intersection(self, ray):
        startP=ray.getStartPoint()
        cameraToCenter = startP.sub(self.center)

        a = self.calculateA(ray.getDirection())
        b = self.calculateB(cameraToCenter, ray.getDirection())
        c = self.calculateC(cameraToCenter)

        t = None
        if a != 0:
            t = MathUtil.solveQuadraticFormula(a, b, c)

        if t is not None :
            distanceT = t.getSmallestPositive()
            point = ray.getPointOfRay(distanceT)
            intersect = Intersection(point, self, ray, distanceT)
        else:
            intersect = None

        return intersect


    def getCenter(self):
        return self.center

    def getRadius(self):
        return self.radius


    def calculateA(self, ray):
        return ray.dotProduct(ray)

    def calculateB(self, cameraToCenter, ray):
        return 2 * (cameraToCenter.dotProduct(ray))

    def calculateC(self, cameraToCenter):
        return cameraToCenter.dotProduct(cameraToCenter) - math.pow(self.radius, 2)
