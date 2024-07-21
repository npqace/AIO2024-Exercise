import numpy as np

# a. độ dài của vector
def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector

# b. phép tích vô hướng
def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result

# c. nhân vector với ma trận
def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result

# d. nhân ma trận với ma trận
def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

# e. ma trận nghịch đảo
def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result
