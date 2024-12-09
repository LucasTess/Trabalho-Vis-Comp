import numpy as np
from stl import mesh

mesh_file = mesh.Mesh.from_file('utils/Aatrox.stl')

x = mesh_file.x.flatten()
y = mesh_file.y.flatten()
z = mesh_file.z.flatten()

Aatrox_vectors = mesh_file.vectors
Aatrox = np.array([x.T,y.T,z.T,np.ones(x.size)])
