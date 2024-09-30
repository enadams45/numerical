from numpy import*

def transform(mat):
    n = mat.shape[0]
    for i in range (n):
        if (mat[i, i] == 0):
            for j in range (i+1, n):
                if (mat[j, i]!=0):
                    mat[i], mat [j] = mat[j], mat[i]
                    break
        for j in range (n):
            if (i==j):
                continue
            print (f"R{j+1} = {mat[i, i]} * R{j+1} - {mat[j, i]} * R{i+1}")
            print()
            mat[j] = mat[i, i] * mat[j] - mat[i] * mat[j, i]
            print(mat, end = "\n\n")
    

mat = array(
    [
        [4, 3, 2, 1, 0, 0],
        [3, 5, 1, 0, 1, 0],
        [2, 1, 3, 0, 0, 1]
        ], dtype = int)
transform(mat)

            