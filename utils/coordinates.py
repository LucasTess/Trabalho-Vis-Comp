from dataclasses import dataclass

import numpy as np

@dataclass
class RotationMatrices:
    x: np.ndarray
    y: np.ndarray
    z: np.ndarray

    @staticmethod
    def from_theta(theta: float) -> 'RotationMatrices':
        """ Cria as matrizes de rotação a partir do ângulo theta em graus
        Args:
            theta (float): ângulo em graus
        Return:
            RotationMatrices: instância de RotationMatrices
        """
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

e1 = np.array([[1],[0],[0],[0]])
e2 = np.array([[0],[1],[0],[0]])
e3 = np.array([[0],[0],[1],[0]])

base_3d = np.hstack((e1,e2,e3))
origem_3d = np.array([[0],[0],[0],[1]])
cam_origem = np.array([[0],[-100],[100],[1]])
