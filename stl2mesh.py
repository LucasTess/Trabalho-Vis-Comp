from stl import mesh
import numpy as np
# Load the STL files and add the vectors to the plot
your_mesh = mesh.Mesh.from_file('Aatrox.stl')

# Get the x, y, z coordinates contained in the mesh structure that are the
# vertices of the triangular faces of the object
x = your_mesh.x.flatten()
y = your_mesh.y.flatten()
z = your_mesh.z.flatten()

# Get the vectors that define the triangular faces that form the 3D object
Aatrox_vectors = your_mesh.vectors
# Create the 3D object from the x,y,z coordinates and add the additional array of ones to
# represent the object using homogeneous coordinates
Aatrox = np.array([x.T,y.T,z.T,np.ones(x.size)])

