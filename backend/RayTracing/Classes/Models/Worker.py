import numpy

class Worker:
    """Class to be used in multiprocessing, it is the object that is shared between processes"""

    def __init__(self, fromY = 0, toY = 0, fromX = 0, toX = 0, height = 0, width = 0):
        self.fromY = int(fromY)
        self.toY = int(toY)
        self.fromX = int(fromX)
        self.toX = int(toX)
        self.img = numpy.zeros((toY - fromY, width, 3))
        self.width = width
        self.height = height

    def setColor(self, y, x, rgb):
        y = y - self.fromY
        self.img[y][x] = rgb

    def setColorAntialiasing(self, y, x, rgbV, rgb0, rgb1, rgb2, rgb3):
        y = y - self.fromY

        rgbAntialiasing = [rgb0, rgb1, rgb2, rgb3]
        self.img[y][x] = rgbV.averageColors(rgbAntialiasing).getArray()

    def getHeight(self):
        return self.height


    def getWidth(self):
        return self.width


    def getImg(self):
        return self.img


    def getYRange(self):
        return list(range(self.fromY, self.toY))


    def getXRange(self):
        return list(range(self.fromX, self.toX))