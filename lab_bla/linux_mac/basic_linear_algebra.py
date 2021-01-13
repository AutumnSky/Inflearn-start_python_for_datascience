from functools import reduce


def vector_size_check(*vector_variables):
    return len(set(map(lambda x: len(x), vector_variables))) == 1


# print(vector_size_check([1, 2, 3], [2, 3, 4], [5, 6, 7])) # Expected value: True
# print(vector_size_check([1, 3], [2, 4], [6, 7]))  # Expected value: True
# print(vector_size_check([1, 3, 4], [4], [6, 7]))  # Expected value: False


def vector_addition(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    return list(map(sum, zip(*vector_variables)))


# print(vector_addition([1, 5], [10, 4], [4, 7]))  # Expected value: [15, 16]
# print(vector_addition([1, 3, 4], [4], [6, 7]))  # Expected value: ArithmeticError

def minus(*numbers):
    return reduce(lambda x, y: x - y, *numbers)


def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    return list(map(minus, zip(*vector_variables)))


# print(vector_subtraction([1, 3], [2, 4]))  # Expected value: [-1, -1]
# print(vector_subtraction([1, 5], [10, 4], [4, 7]))  # Expected value: [-13, -6]


def scalar_vector_product(alpha, vector_variable):
    return list(map(lambda variable: alpha * variable, vector_variable))


# print(scalar_vector_product(5, [1, 2, 3]))  # Expected value: [5, 10, 15]
# print(scalar_vector_product(3, [2, 2]))  # Expected value: [6, 6]
# print(scalar_vector_product(4, [1]))  # Expected value: [4]


def get_row_col(matrix):
    if not vector_size_check(*matrix):
        raise ArithmeticError
    row = len(matrix)
    col = len(list(zip(*matrix)))
    return (row, col)


# print(get_row_col([[1]]))  # (1, 1)
# print(get_row_col([[1, 2]]))  # (1, 2)
# print(get_row_col([[1, 2, 3]]))  # (1, 3)
# print(get_row_col([[1], [1]]))  # (2, 1)
# print(get_row_col([[1, 2], [1, 2]]))  # (2, 2)
# print(get_row_col([[1, 2, 3], [1, 2, 3]]))  # (2, 3)


def matrix_size_check(*matrix_variables):
    return len(set(map(lambda matrix: get_row_col(matrix), matrix_variables))) == 1


matrix_x = [[2, 2], [2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_w = [[2, 5], [1, 1], [2, 2]]

# print(matrix_size_check(matrix_x, matrix_y, matrix_z))  # Expected value: False
# print(matrix_size_check(matrix_y, matrix_z))  # Expected value: True
# print(matrix_size_check(matrix_x, matrix_w))  # Expected value: True


def is_matrix_equal(*matrix_variables):
    return all(elem == matrix_variables[0] for elem in matrix_variables)


# print(is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y)) # Expected value: False
# print(is_matrix_equal(matrix_x, matrix_x))  # Expected value: True


def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return [[sum(cols) for cols in zip(*rows)]
            for rows in list(zip(*matrix_variables))]


matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

# print(matrix_addition(matrix_x, matrix_y))  # Expected value: [[4, 7], [4, 3]]
# print(matrix_addition(matrix_x, matrix_y, matrix_z))# Expected value: [[6, 11], [9, 6]]


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return [[minus(cols) for cols in zip(*rows)]
            for rows in list(zip(*matrix_variables))]


# print(matrix_subtraction(matrix_x, matrix_y)) # Expected value: [[0, -3], [0, 1]]
# print(matrix_subtraction(matrix_x, matrix_y, matrix_z))# Expected value: [[-2, -7], [-5, -2]]


def matrix_transpose(matrix_variable):
    return [[element for element in rows] for rows in zip(*matrix_variable)]


matrix_w = [[2, 5], [1, 1], [2, 2]]
# print(matrix_transpose(matrix_w))


def scalar_matrix_product(alpha, matrix_variable):
    return [scalar_vector_product(alpha, rows) for rows in matrix_variable]


matrix_x = [[2, 2], [2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_w = [[2, 5], [1, 1], [2, 2]]

# print(scalar_matrix_product(3, matrix_x)) # Expected value: [[6, 6], [6, 6], [6, 6]]
# print(scalar_matrix_product(2, matrix_y))  # Expected value: [[4, 10], [4, 2]]
# print(scalar_matrix_product(4, matrix_z)) # Expected value: [[8, 16], [20, 12]]
# print(scalar_matrix_product(3, matrix_w)) # Expected value: [[6, 15], [3, 3], [6, 6]]


def is_product_availability_matrix(matrix_a, matrix_b):
    return get_row_col(matrix_a)[1] == get_row_col(matrix_b)[0]


matrix_x = [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]

# print(is_product_availability_matrix(matrix_y, matrix_z))  # Expected value: True
# print(is_product_availability_matrix(matrix_z, matrix_x))  # Expected value: True
# print(is_product_availability_matrix(matrix_z, matrix_w))   # Expected value: False //matrix_w가없습니다
# print(is_product_availability_matrix(matrix_x, matrix_x))  # Expected value: True


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        return False
        # raise ArithmeticError

    return [[sum([dot[0]*dot[1] for dot in zip(row_item, list(col_item))])
             for col_item in zip(*matrix_b)] for row_item in matrix_a]


matrix_x = [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]

# print(matrix_product(matrix_y, matrix_z))   # Expected value: [[9, 13], [10, 14]]
# print(matrix_product(matrix_z, matrix_x))   # Expected value: [[8, 14], [13, 28], [5, 8]]
# print(matrix_product(matrix_x, matrix_x))  # Expected value: [[9, 15], [3, 6]]
# print(matrix_product(matrix_z, matrix_w))  # Expected value: False
