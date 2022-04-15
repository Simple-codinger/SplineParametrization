import matplotlib.pyplot as plt
from splineParametrization.spline.parametricSpline import ParametricSpline
from splineParametrization.spline.spline import Spline

def main():
    spline = ParametricSpline()
    dataPointsX = [1, 2, 2, 3, 3, 4, 6]
    dataPointsY = [5, 6, 2, 6, 1, 5, 3]

    dataPointsX = [1, 2]
    dataPointsY = [5, 6]
    spline.setPoints(dataPointsX, dataPointsY)

    normalSpline = Spline()
    normalSpline.calculateParameter(dataPointsX, dataPointsY)

    plt.plot(dataPointsX, dataPointsY, 'o', color='red')

    print('after plot')
    plt.show()


if __name__ == '__main__':
    main()
