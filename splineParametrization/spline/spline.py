import math
import matplotlib.pyplot as plt
import numpy as np

class Spline:
    def __init__(self):
        self.a: list = []
        self.b: list = []
        self.c: list = []
        self.d: list = []

        self.__x: list = []
        self.__y: list = []

    def getSegment(self, x: float) -> int:
        for i in range(1, len(self.__x)):
            if x <= self.__x[i]:
                return i

        return len(self.__x)-1

    def calculateParameter(self, x: list, y: list) -> None:
        print("Calculating Spline Parameter...")
        # check if x and y are the same size
        assert(len(x) == len(y))
        assert(len(x) > 1)

        self.__x = x
        self.__y = y

        amountOfFunctions: int = len(x) - 1
        amountOfParameters: int = amountOfFunctions*4

        amountOfRows: int = 2*amountOfFunctions + 2*(len(x) - 2) + 2


        # Construct linear system
        A = np.zeros((amountOfRows, amountOfParameters))

        # Construct solution array
        b = np.zeros((amountOfRows, 1))
        for i in range(0, len(y)):
            # check if it's the first or the last element
            if i == 0:
                b[0] = y[0]
            elif i == (len(y)-1):
                b[2*(len(y)-2)+1] = y[i]
            else:
                b[2*i] = y[i]
                b[(2*i)-1] = y[i]

        # Construct matrix


        # Interpolation at datapoints
        for i in range(0, amountOfFunctions):
            # use shifting blocks
            print(i)
            A[2*i][i*4:(i*4)+4] = [math.pow(x[i], 3), math.pow(x[i], 2), x[i], 1]
            A[(2*i)+1][i*4:(i*4)+4] = [math.pow(x[i+1], 3), math.pow(x[i+1], 2), x[i+1], 1]

        # Continuity of functions 
        for i in range(1, len(x)-1):
            offset: int = 2*amountOfFunctions
            # first order
            A[offset + 2*(i-1)][(i-1)*4:(i*4)+4] = [3*math.pow(x[i], 2), 2*x[i], 1, 0, -3*math.pow(x[i], 2), -2*x[i], -1, 0]
            # second order
            A[offset + 2*(i-1)+1][(i-1)*4:(i*4)+4] = [6*x[i], 2, 0, 0, -6*x[i], -2, 0, 0]

        # natural boundary condition
        # first datapoint
        A[amountOfRows-2][0:4] = [6*x[0], 2, 0, 0]
        A[amountOfRows-1][amountOfParameters-4:amountOfParameters] = [6*x[len(x)-1], 2, 0, 0]


        print('--------------------------------')
        print(A)
        print('--------------------------------')

        solution = np.linalg.solve(A, b)
        # solution to parameters
        for i in range(0, amountOfFunctions):
            self.a.append(solution[(i*4)])
            self.b.append(solution[(i*4)+1])
            self.c.append(solution[(i*4)+2])
            self.d.append(solution[(i*4)+3])

        
        
    def plotSpline(self, amountOfPoints: int) -> None:
        for i in range(0, len(self.__x)-1):
            points: np.ndarray = np.linspace(self.__x[i], self.__x[i+1], amountOfPoints)
            plt.plot(
                points,
                self.a[i]*points**3 + self.b[i]*points**2 + self.c[i]*points + self.d[i]
            )





