import numpy as np

from transformations.world_transformations import (world_rotation,
                                                   world_translation)


def cam_translation(M_cam: np.ndarray, x: float, y: float, z: float) -> np.ndarray:
    """Calculate translation in relation to the camera
    Args:
        M_cam (np.ndarray): Camera matrix
        x (float): Translation in x
        y (float): Translation in y
        z (float): Translation in z
    Returns:
        np.ndarray: Translation matrix
    """

    M_inv = np.linalg.inv(M_cam)
    T = world_translation(x, y, z)
    translate_matrix = M_cam @ T @ M_inv

    return translate_matrix


def cam_rotation(M_cam: np.ndarray, eixo: str, theta: float) -> np.ndarray:
    """Calculate rotation in relation to the camera
    Args:
        M_cam (np.ndarray): Camera matrix
        eixo (str): Axis to rotate
        theta (float): Angle in degrees
    Returns:
        np.ndarray: Rotation matrix
    """

    M_inv = np.linalg.inv(M_cam)
    R = world_rotation(eixo, theta)
    rotation_matrix = M_cam @ R @ M_inv
    return rotation_matrix


def change_cam2world(M: np.ndarray, point_cam: np.ndarray) -> np.ndarray:
    """Convert from camera frame to world frame
    Args:
        M (np.ndarray): Camera matrix
        point_cam (np.ndarray): Point in camera frame
    Returns:
        np.ndarray: Point in world frame
    """

    p_world = np.dot(M, point_cam)
    return p_world


def change_world2cam(M: np.ndarray, point_world: np.ndarray) -> np.ndarray:
    """Convert from world frame to camera frame]
    Args:
        M (np.ndarray): Camera matrix
        point_world (np.ndarray): Point in world frame
    Returns:
        np.ndarray: Point in camera frame
    """

    M_inv = np.linalg.inv(M)
    p_cam = np.dot(M_inv, point_world)

    return p_cam
