import numpy as np


def Get_Element_Stiffness_Matrix(k: float, theta: float) -> np.ndarray:
    '''计算平面桁架杆件单元刚度矩阵

    输入参数：
    k: 刚度系数
    theta: 杆件方向与X轴夹角

    返回值：
    K_matrix: 杆件单元刚度矩阵
    '''
    sin = np.sin(theta)
    cos = np.cos(theta)
    csk = sin * cos * k
    esm = np.array([
        [k * cos ** 2, csk],
        [csk, k * sin ** 2]
    ])
    return esm

def lult_decomposition(A):
    """
    LULT 分解函数，将对称正定矩阵 A 分解为 L 和 L^T，满足 A = L L^T
    :param A: 对称正定矩阵 (n x n)
    :return: L (下三角矩阵)
    """
    n = A.shape[0]
    L = np.zeros_like(A)

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                # 对角线元素
                L[i, i] = np.sqrt(A[i, i] - np.sum(L[i, :i] ** 2))
            else:
                # 非对角线元素
                L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]

    return L

def forward_substitution(L, b):
    """
    前代法解 Ly = b
    :param L: 下三角矩阵
    :param b: 右端向量
    :return: 解 y
    """
    n = len(b)
    y = np.zeros_like(b, dtype=np.double)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    return y

def backward_substitution(LT, y):
    """
    回代法解 L^T x = y
    :param LT: 上三角矩阵 (L 的转置)
    :param y: 右端向量
    :return: 解 x
    """
    n = len(y)
    x = np.zeros_like(y, dtype=np.double)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(LT[i, i + 1:], x[i + 1:])) / LT[i, i]
    return x

def solve_lult(A, b):
    """
    用 LULT 分解法解线性方程组 Ax = b
    :param A: 对称正定矩阵 (n x n)
    :param b: 右端向量
    :return: 解 x
    """
    L = lult_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(L.T, y)
    return x
