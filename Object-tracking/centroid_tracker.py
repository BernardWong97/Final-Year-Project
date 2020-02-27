from scipy.spatial import distance as dist
import numpy as np
from collections import OrderedDict


class CentroidTracker:
    # Constructor
    def __init__(self, maxDisappeared=20):
        self.nextObjectID = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()
        self.maxDisappeared = maxDisappeared

    def register(self, centroid, name):
        self.objects[self.nextObjectID] = [centroid, name]
        self.disappeared[self.nextObjectID] = 0
        self.nextObjectID += 1

    def deregister(self, objectID):
        del self.objects[objectID]
        del self.disappeared[objectID]

    def update(self, rects, names):
        if len(rects) == 0:
            for objectID in list(self.disappeared.keys()):
                self.disappeared[objectID] += 1

                if self.disappeared[objectID] > self.maxDisappeared:
                    self.deregister(objectID)

            # if no centroids or updates, return
            return self.objects

        # np array for centroids
        inputCentroids = np.zeros((len(rects), 2), dtype="int")

        for (i, (startX, startY, endX, endY)) in enumerate(rects):
            # get centroid for bounding box
            cX = int((startX + endX) / 2.0)
            cY = int((startY + endY) / 2.0)
            inputCentroids[i] = (cX, cY)

        if len(self.objects) == 0:
            for i in range(0, len(inputCentroids)):
                self.register(inputCentroids[i], names[i])
        else:
            objectIDs = []
            objectCentroids = []
            objectNames = []
            for k, v in self.objects.items():
                objectIDs.append(k)
                objectCentroids.append(v[0])
                objectNames.append(v[1])

            # compute distance between each pair of existing centroids and the new input centroids
            D = dist.cdist(np.array(objectCentroids), inputCentroids)

            # find smallest value and sort the row indexes based on min values, for column, sort based on ordered rows
            rows = D.min(axis=1).argsort()
            cols = D.argmin(axis=1)[rows]

            # sets for saving used row and column indexes
            usedRows = set()
            usedCols = set()

            for (row, col) in zip(rows, cols):
                # if row and col used before, continue
                if row in usedRows or col in usedCols:
                    continue

                # found a match of smallest distance to an existing centroid
                objectID = objectIDs[row]
                self.objects[objectID] = [inputCentroids[col], names[col]]
                self.disappeared[objectID] = 0
                usedRows.add(row)
                usedCols.add(col)

            # compute unexamined row and col indexes
            unusedRows = set(range(0, D.shape[0])).difference(usedRows)
            unusedCols = set(range(0, D.shape[1])).difference(usedCols)

            # check for objects that may have disappeared, otherwise register centroid
            if D.shape[0] >= D.shape[1]:
                for row in unusedRows:
                    objectID = objectIDs[row]
                    self.disappeared[objectID] += 1

                    if self.disappeared[objectID] > self.maxDisappeared:
                        self.deregister(objectID)
            else:
                for col in unusedCols:
                    self.register(inputCentroids[col], names[col])

        return self.objects
