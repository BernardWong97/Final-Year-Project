import numpy as np


class KalmanFilter:
    def __init__(self):
        self.dt = 0.0005
        self.A = np.array([[1, 0], [0, 1]])
        self.u = np.zeros((2, 1))

        self.b = np.array([[0], [255]])
        self.P = np.diag((3.0, 3.0))
        self.Q = np.eye(self.u.shape[0])
        self.R = np.eye(self.b.shape)
        self.lastResult = np.array([0], [255])
