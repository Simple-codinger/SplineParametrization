import math
import matplotlib.pyplot as plt

from matplotlib.pyplot import plot
from splineParametrization.spline.spline import Spline
import numpy as np

class ParametricSpline(Spline):
    def __init__(self) -> None:
        self.__d: list = []
        self.__s: list = []
        self.__splineOne: Spline = Spline()
        self.__splineTwo: Spline = Spline()
        self.maxLength: float


    def setPoints(self, x: list, y:list) -> None:
        self.__x = x
        self.__y = y
        self.__calculateDistances()

        self.__splineOne.calculateParameter(self.__s, x)
        self.__splineTwo.calculateParameter(self.__s, y)


    def __calculateDistances(self) -> None:
        self.__d = [0] * len(self.__x)
        self.__s = [0] * len(self.__x)

        print("calculate distances...")
        for i in range(0, len(self.__x) - 1):
            self.__d[i] = math.sqrt(math.pow(self.__x[i+1] - self.__x[i], 2) + math.pow(self.__y[i+1] - self.__y[i], 2))
            self.__s[i+1] = np.sum(self.__d[0:i+1])
        print(self.__s)
        print('test')
        self.maxLength = self.__s[len(self.__s)-1]

    def plotSpline(self, amountOfPoints: int) -> None:
        for i in range(0, len(self.__s)-1):
            distances: np.ndarray = np.linspace(self.__s[i], self.__s[i+1], amountOfPoints)
            plt.plot(
                self.__splineOne.a[i]*distances**3 + self.__splineOne.b[i]*distances**2 + self.__splineOne.c[i]*distances + self.__splineOne.d[i], 
                self.__splineTwo.a[i]*distances**3 + self.__splineTwo.b[i]*distances**2 + self.__splineTwo.c[i]*distances + self.__splineTwo.d[i]
            )
        
        plt.figure(1)
        self.__splineOne.plotSpline(100)
        plt.figure(2)
        self.__splineTwo.plotSpline(100)

            
