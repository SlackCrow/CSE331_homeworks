class Solution:
    def __init__(self, points):
        self.points = points
    
    def findDistance(self,point1,point2):
        x1 = point1[0]
        x2 = point2[0]
        y1 = point1[1]
        y2 = point2[1]
        return (((x1-x2)**2)+((y1-y2)**2))**0.5

    def bruteforceShortestDistance(self,points):
        iter1 = 0
        min = 999999999999999999999999999
        while iter1 < len(points):
            iter2 = iter1 + 1
            currentBase = points[iter1]
            while iter2 < len(points):
                currentTest = points[iter2]
                currentDistance = self.findDistance(currentBase,currentTest)
                if currentDistance < min:
                    min = currentDistance
                iter2 = iter2 + 1
            iter1 = iter1 + 1
        return min

    def recursivelyFind(self, points):
        if(len(points) <=3):
            return self.bruteforceShortestDistance(points)
        middlePoints = len(points)//2
        pointsA = points[:middlePoints]
        pointsB = points[-middlePoints:]
        left = self.recursivelyFind(pointsA)
        right = self.recursivelyFind(pointsB)
        minD = min(left,right)
        
        closePoints = list()
        for point in points:
            x = point[0]
            middleX = points[middlePoints][0]
            if abs(x - middleX) < minD:
                closePoints.append(point)
        closePoints = sorted(closePoints, key=lambda x: x[1])
        minCP = minD
        iter1 = 0
        while iter1 < len(closePoints):
            tempBase = closePoints[iter1]
            iter2 = iter1 + 1
            while iter2 < len(closePoints) and (closePoints[iter2][1] - tempBase[1]) < minCP:
                dist = self.findDistance(tempBase,closePoints[iter2])
                if dist < minCP:
                    minCP = dist 
                iter2 = iter2 + 1
            iter1 = iter1 + 1
        return min(minD,minCP)

    def findClosestPair(self):
        self.points = sorted(self.points, key=lambda x: x[0])
        return self.recursivelyFind(self.points)
