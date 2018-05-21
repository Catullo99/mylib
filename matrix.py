Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def form_matrix(lines,columns,coefficients):
    matrice = []
    count = 0
    for i in range(1,lines+1):
        new_line = []
        for j in range(1,columns+1):
            new_line.append(coefficients[count])
            count += 1
        matrice.append(new_line)
    return matrice

        
>>> def add_matrix(mat1,mat2):
    lines_1 = len(mat1)
    lines_2 = len(mat2)
    columns_1 = len(mat1[0])
    columns_2 = len(mat2[0])
    if lines_1 != lines_2:
        return 'not same size boi - lines'
    if columns_1 != columns_2:
        return 'not same size boi - columns'
    summ = []
    for i in range(lines_1):
        new_line = []
        for j in range(columns_1):
            new_line.append(mat1[i][j]+mat2[i][j])
        summ.append(new_line)
    return summ

>>> def product_matrix(mat1,mat2):
    lines_1 = len(mat1)
    lines_2 = len(mat2)
    columns_1 = len(mat1[0])
    columns_2 = len(mat2[0])
    if columns_1 != lines_2:
        return 'product not defined boi'
    out = []
    for i in range(lines_1):
        new_line = []
        for j in range(columns_2):
            new_term = 0
            for k in range(columns_1):
                new_term += (mat1[i][k]*mat2[k][j])
            new_line.append(new_term)
        out.append(new_line)
    return out

>>> def transp_matrix(mat):
    lines = len(mat)
    columns = len(mat[0])
    out = []
    for j in range(columns):
        new_line = []
        for i in range(lines):
            new_line.append(mat[i][j])
        out.append(new_line)
    return out

>>> 
