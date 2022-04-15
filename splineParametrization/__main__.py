import matplotlib.pyplot as plt
import numpy as np
from splineParametrization.spline.parametricSpline import ParametricSpline
from splineParametrization.spline.spline import Spline

def main():
    spline = ParametricSpline()
    dataPointsX = [1, 2, 2, 3, 3, 4, 6]
    dataPointsY = [5, 6, 2, 6, 1, 5, 3]

    dataPointsX = [1, 2, 3, 6, 8]
    dataPointsY = [5, 6, 31, 9, 7]
    spline.setPoints(dataPointsX, dataPointsY)

    normalSpline = Spline()
    normalSpline.calculateParameter(dataPointsX, dataPointsY)

    for i in range(0, len(dataPointsX)-1):
        t = np.linspace(dataPointsX[i], dataPointsX[i+1], 100)
        plt.plot(t, normalSpline.a[i]*t**3 + normalSpline.b[i]*t**2 + normalSpline.c[i]*t + normalSpline.d[i])

    plt.plot(dataPointsX, dataPointsY, 'o', color='red')

    print('after plot')
    plt.show()


if __name__ == '__main__':
    main()
