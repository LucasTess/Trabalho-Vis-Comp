from dataclasses import dataclass

import numpy as np

@dataclass
class RotationMatrices:
    x: np.ndarray
    y: np.ndarray
    z: np.ndarray

    @staticmethod
    def from_theta(theta: float) -> 'RotationMatrices':
        """Cria as matrizes de rotação a partir do ângulo theta em graus"""
        theta_rad = theta * np.pi / 180
        
        x = np.array([
            [1, 0, 0, 0],
            [0, np.cos(theta_rad), -np.sin(theta_rad), 0],
            [0, np.sin(theta_rad), np.cos(theta_rad), 0],
            [0, 0, 0, 1]
        ])
        
        y = np.array([
            [np.cos(theta_rad), 0, np.sin(theta_rad), 0],
            [0, 1, 0, 0],
            [-np.sin(theta_rad), 0, np.cos(theta_rad), 0],
            [0, 0, 0, 1]
        ])
        
        z = np.array([
            [np.cos(theta_rad), -np.sin(theta_rad), 0, 0],
            [np.sin(theta_rad), np.cos(theta_rad), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        
        return RotationMatrices(x=x, y=y, z=z)
    

def world_rotation(eixo: str, theta: float) -> np.ndarray:
    """Calcula rotação em relação ao mundo com theta dado em graus"""
    
    theta = theta * np.pi / 180
    
    rotation_matrices = RotationMatrices.from_theta(theta)
    
    rotation_matrix = getattr(rotation_matrices, eixo, None)
    
    if rotation_matrix is None:
        print('Eixo inexistente ou incorreto.')
        return np.array([])
    
    return rotation_matrix


if __name__ == '__main__':
    print(world_rotation('x', 90))
    print(world_rotation('y', 90))
    print(world_rotation('z', 90))
    print(world_rotation('w', 90))
