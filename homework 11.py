def get_matrix(n=3, m=12, value=89):
    matrix = []
    for i in range(n):
        v = []
        matrix.append(v)
        for j in range(m):
            v.append(value)
    return matrix
print(get_matrix())
