import math
import numpy as np

class Spline:
    def __init__(self):
        self.a: list = []
        self.b: list = []
        self.c: list = []
        self.d: list = []

        self.__x: list = []
        self.__y: list = []

    def calculateParameter(self, x: list, y: list) -> None:
        print("Calculating Spline Parameter...")
        # check if x and y are the same size
        assert(len(x) == len(y))
        assert(len(x) > 1)

        amountOfFunctions: int = len(x) - 1
        amountOfParameters: int = amountOfFunctions*4

        amountOfRows: int = 2*amountOfFunctions + 2*(len(x) - 2) + 2


        # Construct linear system
        A = np.zeros((amountOfRows, amountOfParameters))

        # Construct solution array
        s = np.zeros((amountOfRows, 1))
        for i in range(0, len(y)):
            # check if it's the first or the last element
            if i == 0:
                s[0] = y[0]
            elif i == (len(y)-1):
                s[2*(len(y)-2)+1] = y[i]
            else:
                s[2*i] = y[i]
                s[(2*i)-1] = y[i]
        
        print(s)

        # Construct matrix
        





