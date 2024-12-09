from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from typing import Optional, List

def set_plot(
    ax: Optional[Axes] = None,
    figure: Optional[Figure] = None,
    lim: List[float] = [-2, 2]
) -> Axes:
    """
    Sets up the initial parameters for a 3D plot.

    Args:
        ax (Optional[Axes]): The 3D axis to configure. If None, a new axis is created.
        figure (Optional[Figure]): The figure to attach the axis. If None, a new figure is created.
        lim (List[float]): Limits for the x, y, and z axes. Defaults to [-2, 2].

    Returns:
        Axes: The configured 3D axis.
    """
    if figure is None:
        figure = plt.figure(figsize=(8, 8))
    if ax is None:
        ax = plt.axes(projection='3d')

    ax.set_xlim(lim)
    ax.set_xlabel('X Axis')
    ax.set_ylim(lim)
    ax.set_ylabel('Y Axis')
    ax.set_zlim(lim)
    ax.set_zlabel('Z Axis')

    return ax
