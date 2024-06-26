import numpy as np


####################仅仅是一个示例###################################


# 双目相机参数
class stereoCamera(object):
    def __init__(self):
        # 左相机内参
        self.cam_matrix_left = np.array([[1060.3700, 0, 1124.9100],
                                         [0, 1059.7600, 623.3810],
                                         [0, 0, 1]
                                         ])
        # 右相机内参
        self.cam_matrix_right = np.array([[1049.2200, 0, 1124.6899],
                                          [0, 1049.0800, 619.5950],
                                          [0, 0, 1]
                                          ])

        # 左右相机畸变系数:[k1, k2, p1, p2, k3]
        self.distortion_l = np.array([[-0.0424, 0.0126, -0.0002, 0.0003, -0.0060]])
        self.distortion_r = np.array([[-0.0411, 0.0089, -0.0002, 0.0003, -0.0060]])

        # 旋转矩阵
        self.R = np.array([[1.0000, -0.0006, 0.0028],
                           [0.0006, 1.0000, -0.0003],
                           [-0.0028, 0.0003, 1.0000]
                           ])

        # 平移矩阵
        self.T = np.array([[119.7550], [-0.1684], [0.4651]])

        # 焦距
        self.focal_length = 859.367  # 默认值，一般取立体校正后的重投影矩阵Q中的 Q[2,3]

        # 基线距离
        self.baseline = 119.9578  # 单位：mm， 为平移向量的第一个参数（取绝对值）




