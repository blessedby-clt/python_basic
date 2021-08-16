def vector_size_check(*vector_variables):
    # return len(set([len(vector) for vector in vector_variables])) == 1
    # 아래는 for loop문으로 수정.
    temp = []
    for i in vector_variables :
        temp.append(len(i))
    return len(set(temp)) == 1

def vector_addition(*vector_variables):
    # if vector_size_check(*vector_variables) == True :
    #     return [sum(vector) for vector in zip(*vector_variables)]
    # return "ArithmeticError"
    # 아래는 for loop 문으로 수정.
    temp = [0 for l in range(0, len(vector_variables[0]))]
    if vector_size_check(*vector_variables) == True :
        for i in range(0, len(vector_variables)) :
            for j in range(0, len(vector_variables[i])) :
                temp[j] += vector_variables[i][j]
        return temp
    return "ArithmeticError"

def vector_subtraction(*vector_variables):
    # if vector_size_check(*vector_variables) == False:
    #     raise ArithmeticError
    # return [sum([v for i, v in enumerate(vector) if i == 0]+[-1*v for i, v in enumerate(vector) if i > 0])
    #   for vector in zip(*vector_variables)]
    # 아래는 for loop문으로 수정
    temp = vector_variables[0]
    if vector_size_check(*vector_variables) == True:
        for i in range(1, len(vector_variables)):
            for j in range(0, len(vector_variables[i])):
                temp[j] -= vector_variables[i][j]
        return temp
    return "ArithmeticError"

def scalar_vector_product(alpha, vector_variable):
    # return [sum(alpha*vector) for vector in zip(vector_variable)]
    # 아래는 for loop문으로 수정.
    for i in range(len(vector_variable)) :
        vector_variable[i] = alpha*vector_variable[i]
    return vector_variable

def matrix_size_check(*matrix_variables):
    # return len(set([sum([len(vector) for vector in zip(matrix)]) for matrix in matrix_variables])) == 1
    # 아래는 for loop문으로 수정
    matrix_list = []
    vector_list = []
    for i in matrix_variables :
        matrix_list.append(len(i))
        for j in i :
            vector_list.append(len(j))

    return len(set(matrix_list)) == 1 & len(set(vector_list)) == 1



def is_matrix_equal(*matrix_variables):
    # return len(set(sum([[len(set(vector)) for vector in zip(*matrix)] for matrix in zip(*matrix_variables)], []))) == 1
    # 아래는 for loop문으로 수정
    term = 0
    for i in range(1, len(matrix_variables)) :
        for j in range(0, len(matrix_variables[i])) :
            if matrix_variables[0][j] != matrix_variables[i][j] :
                term += 1
    return term == 0

# matrix_x = [[2, 2], [2, 2]]
# matrix_y = [[2, 5], [2, 1]]
#
# print (is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y)) # Expected value: False
# print (is_matrix_equal(matrix_x, matrix_x)) # Expected value: True

def matrix_addition(*matrix_variables):
    # if not matrix_size_check(*matrix_variables):
    #     raise ArithmeticError
    # return [[sum(t) for t in zip(*matrix)] for matrix in zip(*matrix_variables)]
    # 아래는 for loop문으로 수정
    temp = [[element for element in l] for l in matrix_variables[0]] ## matrix_variables[0]으로 그냥 세팅하면 값 자체가 바뀌어버림. why?
    if matrix_size_check(*matrix_variables) == True:
        for i in range(1, len(matrix_variables)):
            for j in range(0, len(matrix_variables[i])):
                for k in range(0, len(matrix_variables[i][j])) :
                    print(matrix_variables[i][j][k])
                    print(temp[j][k])
                    temp[j][k] += matrix_variables[i][j][k]
        return temp
    return "ArithmeticError"
#
# matrix_x = [[2, 2], [2, 2]]
# matrix_y = [[2, 5], [2, 1]]
# matrix_z = [[2, 4], [5, 3]]
#
# print(matrix_addition(matrix_x, matrix_y)) # Expected value: [[4, 7], [4, 3]]
# print(matrix_addition(matrix_x, matrix_y, matrix_z)) # Expected value: [[6, 11], [9, 6]]

def matrix_subtraction(*matrix_variables):
    # if not matrix_size_check(*matrix_variables):
    #     raise ArithmeticError
    # return None
    temp = [[element for element in l] for l in matrix_variables[0]]
    if matrix_size_check(*matrix_variables) == True:
        for i in range(1, len(matrix_variables)):
            for j in range(0, len(matrix_variables[i])):
                for k in range(0, len(matrix_variables[i][j])) :
                    temp[j][k] -= matrix_variables[i][j][k]
        return temp
    else :
        return "ArithmeticError"

# matrix_x = [[2, 2], [2, 2]]
# matrix_y = [[2, 5], [2, 1]]
# matrix_z = [[2, 4], [5, 3]]
#
# print(matrix_subtraction(matrix_x, matrix_y)) # Expected value: [[0, -3], [0, 1]]
# print(matrix_subtraction(matrix_x, matrix_y, matrix_z)) # Expected value: [[-2, -7], [-5, -2]]

def matrix_transpose(matrix_variable):
    return [[element for element in m] for m in zip(*matrix_variable)]


def scalar_matrix_product(alpha, matrix_variable):
    for m in matrix_variable :
        for i in range(len(m)) :
            m[i] = alpha * m[i]
    return matrix_variable

# matrix_x = [[2, 2], [2, 2], [2, 2]]
# matrix_y = [[2, 5], [2, 1]]
# matrix_z = [[2, 4], [5, 3]]
# matrix_w = [[2, 5], [1, 1], [2, 2]]
#
# print(scalar_matrix_product(3, matrix_x))  # Expected value: [[6, 6], [6, 6], [6, 6]]
# print(scalar_matrix_product(2, matrix_y))  # Expected value: [[4, 10], [4, 2]]
# print(scalar_matrix_product(4, matrix_z))  # Expected value: [[8, 16], [20, 12]]
# print(scalar_matrix_product(3, matrix_w))  # Expected value: [[6, 15], [3, 3], [6, 6]]



def is_product_availability_matrix(matrix_a, matrix_b):
    return len(matrix_a) == len(matrix_b[0])

def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError
    return [[sum(a*b for a, b in zip(row_a, row_b)) for row_b in zip(*matrix_b)] for row_a in matrix_a]
#     temp = 0
#     for a in matrix_a :
#         for b in matrix_transpose(matrix_b) :
#             for m, n in zip(a, b) :
#                 temp += m * n
#                 print(temp)
#
#
# matrix_x= [[2, 5], [1, 1]]
# matrix_y = [[1, 1, 2], [2, 1, 1]]
# matrix_z = [[2, 4], [5, 3], [1, 3]]
#
# print(matrix_product(matrix_y, matrix_z)) # Expected value: [[9, 13], [10, 14]]
