import numpy as np

def angle_features(angles: list) -> np.ndarray:
    """
    Returns a (3, n) float64 array with sine, cosine, and tangent rows.
    """
    angles = np.array(angles, dtype=np.float64)
    sine_angles = np.sin(angles)
    cos_angles= np.cos(angles)
    tan_angles= np.tan(angles)
    return np.stack([sine_angles,cos_angles,tan_angles])