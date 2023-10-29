import numpy as np

def find_rpy_angles(point_A, point_B):
    '''
    :param point_A: np.array([0, 1, 2])
    :param point_B: np.array([3, 4, 5])
    :return: list:[alpha, beta, gamma]
    '''

    # 计算向量AB
    vector_AB = point_B - point_A

    # 生成一个垂直于向量AB的向量
    # 首先找到一个与AB不平行的向量，例如(1, 0, 0)
    # 然后通过叉乘计算与AB垂直的向量
    vector_perpendicular = np.cross(vector_AB, np.array([1, 0, 0]))

    # 创建一个以点A为原点，以vector_perpendicular为法向量的平面
    # 平面方程为 Ax + By + Cz = 0，其中 (A, B, C) 为 vector_perpendicular
    A, B, C = vector_perpendicular
    D = -(A * point_A[0] + B * point_A[1] + C * point_A[2])

    # 输出平面方程
    print(f"垂直于向量AB的平面方程为: {A}x + {B}y + {C}z + {D} = 0")

    # 找出一对过点A且互相垂直的线AC和AD
    # 可以将线AC看作是平面上的两个点，其中一个点为A，另一个点在平面上
    # 线AD可以通过向量叉乘计算得到，即AD = AB × AC
    # 注意：AC和AD的长度不唯一，只需要方向正确即可

    # 随机选择一个与vector_perpendicular不平行的向量作为AC的向量
    vector_AC = np.array([1, 1, -(A + B)])  # 这里假设了一个与vector_perpendicular不平行的向量

    # 计算向量AD
    vector_AD = np.cross(vector_AB, vector_AC)

    # 输出线AC和线AD的方向向量
    print(f"线AC的方向向量为: {vector_AC}")
    print(f"线AD的方向向量为: {vector_AD}")

    ### 对向量进行归一化
    # 计算向量的长度（模）
    length_AB = np.linalg.norm(vector_AB)
    length_AC = np.linalg.norm(vector_AC)
    length_AD = np.linalg.norm(vector_AD)

    # 归一化向量
    normalized_vector_AB = vector_AB / length_AB
    normalized_vector_AC = vector_AC / length_AC
    normalized_vector_AD = vector_AD / length_AD

    # 输出归一化后的向量
    print(f"归一化后的向量AB: {normalized_vector_AB}")
    print(f"归一化后的向量AC: {normalized_vector_AC}")
    print(f"归一化后的向量AD: {normalized_vector_AD}")

    ### 把归一化后的AB，AC，AD三个向量按顺序作为三个列向量，排成一个3x3的矩阵
    # 组合成3x3矩阵
    matrix = np.column_stack((normalized_vector_AB, normalized_vector_AC, normalized_vector_AD))

    # 输出矩阵
    print("3x3矩阵：")
    print(matrix)

    print(matrix[0][2])

    tg_beta = (-matrix[2][0])/(np.sqrt(np.square(matrix[0][0])+np.square(matrix[1][0])))
    tg_alpha = (matrix[0][1])/(matrix[0][0])
    tg_gamma = (matrix[1][2])/(matrix[2][2])

    beta = np.arctan(tg_beta)
    alpha = np.arctan(tg_alpha)
    gamma = np.arctan(tg_gamma)

    print("beta, alpha, gamma", beta, alpha, gamma)

    return [alpha, beta, gamma]


point_A = np.array([0,0,0.1])
point_B = np.array([0.2,0.25, 0.2])
[alpha, beta ,gamma] = find_rpy_angles(point_A, point_B)

