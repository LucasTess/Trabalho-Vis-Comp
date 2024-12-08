import numpy as np

e1 = np.array([[1],[0],[0],[0]]) # X
e2 = np.array([[0],[1],[0],[0]]) # Y
e3 = np.array([[0],[0],[1],[0]]) # Z
base3d = np.hstack((e1,e2,e3))
origem3d = np.array([[0],[0],[0],[1]])
start_cam = np.array([[0],[-100],[100],[1]])
cam_origem = np.hstack([base3d,start_cam])