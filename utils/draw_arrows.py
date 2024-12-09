import numpy as np
import matplotlib.axes

def draw_arrows(
        point: np.ndarray,
        base: np.ndarray,
        axis: 'matplotlib.axes.Axes',
        length: float = 25
    ) -> 'matplotlib.axes.Axes':
    """Desenha vetores que representam os eixos a partir de um ponto específico no espaço 3D.

    Args:
        point (np.ndarray): Coordenadas do ponto de origem dos vetores (shape (3,)).
        base (np.ndarray): Matriz 3x3 representando os vetores base (colunas são os vetores).
        axis (matplotlib.axes.Axes): Objeto do matplotlib para desenhar os vetores.
        length (float, optional): Comprimento dos vetores. Padrão é 25.

    Returns:
        matplotlib.axes.Axes: O eixo com os vetores adicionados.
    """

    axis.quiver(point[0],point[1],point[2],base[0,0],base[1,0],base[2,0],color='red',pivot='tail',  length=length)
    axis.quiver(point[0],point[1],point[2],base[0,1],base[1,1],base[2,1],color='green',pivot='tail',  length=length)
    axis.quiver(point[0],point[1],point[2],base[0,2],base[1,2],base[2,2],color='blue',pivot='tail',  length=length)

    return axis


# np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(float(x))})
# np.set_printoptions(precision=3,suppress=True)
