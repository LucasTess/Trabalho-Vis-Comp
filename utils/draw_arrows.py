import numpy as np
import matplotlib.axes

def draw_arrows(
        point: np.ndarray,
        base: np.ndarray,
        axis: 'matplotlib.axes.Axes',
        length: float = 25
    ) -> 'matplotlib.axes.Axes':
    """Draws vectors representing axes from a specific point in 3D space.

    Args:
        point (np.ndarray): Coordinates of the origin point of the vectors (shape (3,)).
        base (np.ndarray): 3x3 matrix representing the base vectors (columns are the vectors).
        axis (matplotlib.axes.Axes): Matplotlib object to draw the vectors.
        length (float, optional): Length of the vectors. Default is 25.

    Returns:
        matplotlib.axes.Axes: The axis with the vectors added.
    """

    axis.quiver(point[0],point[1],point[2],base[0,0],base[1,0],base[2,0],color='red',pivot='tail',  length=length)
    axis.quiver(point[0],point[1],point[2],base[0,1],base[1,1],base[2,1],color='green',pivot='tail',  length=length)
    axis.quiver(point[0],point[1],point[2],base[0,2],base[1,2],base[2,2],color='blue',pivot='tail',  length=length)

    return axis
