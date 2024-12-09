from typing import Union
import numpy as np

def generate_intrinsic_params_matrix(
        px_base: Union[int, float], 
        px_altura: Union[int, float], 
        focal_length: Union[int, float], 
        stheta: Union[int, float],
        ccd: np.ndarray
    ) -> np.ndarray:
    """
    Generate the intrinsic parameters matrix
    Args:
        px_base (Union[int, float]): Base pixel
        px_altura (Union[int, float]): Height pixel
        focal_length (Union[int, float]): Focal length
        stheta (Union[int, float]): Theta
        ccd (np.ndarray): CCD matrix.
    Returns:
        np.ndarray: Intrinsic parameters matrix
    """
    fs_x = px_base * focal_length / ccd[0]
    fs_y = px_altura * focal_length / ccd[1]
    fs_theta = stheta * focal_length
    ox = px_base / 2
    oy = px_altura / 2

    print(f"fs_x: {fs_x}\nfs_y: {fs_y}\nfs_theta: {fs_theta}\nox: {ox}\noy: {oy}")

    MPI = np.array(
        [[fs_x, fs_theta, ox],
        [0, fs_y, oy],
        [0, 0, 1]]
    )

    return MPI

def projection_2d(
        camera: np.ndarray, 
        objeto: np.ndarray,
        projection_matrix: np.ndarray,
        px_base: Union[int, float],
        px_altura: Union[int, float],
        focal_length: Union[int, float],
        stheta: Union[int, float],
        ccd: np.ndarray
    ) -> np.ndarray:
    """
    Calculate the projection of a 3D object in a 2D plane
    Args:
        camera (np.ndarray): Camera matrix
        objeto (np.ndarray): Object matrix
        projection_matrix (np.ndarray): Projection matrix
        px_base (Union[int, float]): Base pixel
        px_altura (Union[int, float]): Height pixel
        focal_length (Union[int, float]): Focal length
        stheta (Union[int, float]): Theta
        ccd (np.ndarray): CCD matrix
    Returns:
        np.ndarray: Object in 2D
    """
    MPI = generate_intrinsic_params_matrix(px_base, px_altura, focal_length, stheta, ccd)
    Cam_inv = np.linalg.inv(camera)
    print(f"Camera:\n{camera}")
    print(f"inv(Camera):\n{Cam_inv}")
    object_2d = MPI @ projection_matrix @ Cam_inv @ objeto

    if object_2d[2, :].all() == 0:
        object_2d[2, :] = 1
    
    object_2d[0, :] = object_2d[0, :] / object_2d[2, :]
    object_2d[1, :] = object_2d[1, :] / object_2d[2, :]
    object_2d[2, :] = object_2d[2, :] / object_2d[2, :]
    
    print(f"Objeto 2D:\n{object_2d}")
    
    return object_2d


