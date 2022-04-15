import matplotlib.pyplot as plt
import numpy as np
from splineParametrization.spline.parametricSpline import ParametricSpline
from splineParametrization.spline.spline import Spline

def main():
    spline = ParametricSpline()
    dataPointsX = [1, 2, 2, 3, 3, 4, 6]
    dataPointsY = [5, 6, 2, 6, 1, 5, 3]

    dataPointsX = [1, 2, 21, 5, 6, 8]
    dataPointsY = [5, 6, 0, 20, 9, 7]
    spline.setPoints(dataPointsX, dataPointsY)
    plt.figure(0)
    #spline.plotSpline(100)

    normalSpline = Spline()
    normalSpline.calculateParameter(dataPointsX, dataPointsY)
    plt.figure(0)
    normalSpline.plotSpline(100)

    plt.plot(dataPointsX, dataPointsY, 'o', color='red')

    print('after plot')
    plt.show()


if __name__ == '__main__':
    main()
