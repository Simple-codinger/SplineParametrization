import math
from splineParametrization.spline.spline import Spline
import numpy as np

class ParametricSpline(Spline):
    def __init__(self) -> None:
        self.__d: list = []
        self.__s: list = []
        self.__splineOne: Spline()
        self.__splineTwo: Spline()


    def setPoints(self, x: list, y:list) -> None:
        self.__x = x
        self.__y = y
        self.__calculateDistances()

    def __calculateDistances(self) -> None:
        self.__d = [0] * len(self.__x)
        self.__s = [0] * len(self.__x)

        print("calculate distances...")
        for i in range(0, len(self.__x) - 1):
            self.__d[i] = math.sqrt(math.pow(self.__x[i+1] - self.__x[i], 2) + math.pow(self.__y[i+1] - self.__y[i], 2))
            self.__s[i+1] = np.sum(self.__d[0:i+1])

        print(self.__d)
        print('_______________________')
        print(self.__s)
        print('_______________________')
        print(self.__x)
        print('_______________________')
        print(self.__y)
    
