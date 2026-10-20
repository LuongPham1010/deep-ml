def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    b = []
    for i in range(len(a[0])):
        new_row = []
        for j in range(len(a)):
            element = a[j][i]
            new_row.append(element)
        b.append(new_row)
    return b 