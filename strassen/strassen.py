#일반적인 행렬의 곱
def standard_mul(arr1, arr2):

    newarr = []

    for i in range(0, len(arr1)):
        newarr_v = []
        for j in range(0, len(arr1)):
            num = 0
            for k in range(0, len(arr1)):
                num += arr1[i][k] * arr2[k][j]
            newarr_v.append(num)
        newarr.append(newarr_v)

    return newarr

#일반적인 행렬의 합과 차
def standard_cal(arr1, arr2, calc):

    newarr = []
    if(calc == "add"):
        cal = 1
    elif(calc == "sub"):
        cal = -1

    for i in range(0, len(arr1)):
        newarr_v = []
        for j in range(0, len(arr1)):
            newarr_v.append(arr1[i][j] + cal * arr2[i][j])
        newarr.append(newarr_v)

    return newarr

#슈트라젠 행렬 나누기
def strassen_div(mat):

    lenth = int(len(mat)/2)
    div_mat1, div_mat2, div_mat3, div_mat4 = [[0]*lenth for i in range(lenth)], [[0]*lenth for i in range(lenth)], [[0]*lenth for i in range(lenth)], [[0]*lenth for i in range(lenth)]

    for i in range(0, lenth):
        for j in range(0, lenth):
            div_mat1[i][j] += mat[i][j]
            div_mat2[i][j] += mat[i][lenth+j]
            div_mat3[i][j] += mat[lenth+i][j]
            div_mat4[i][j] += mat[lenth+i][lenth+j]

    return div_mat1, div_mat2, div_mat3, div_mat4

#슈트라젠 행렬 합치기
def strassen_merge(arr1, arr2, arr3, arr4):

    lenth=len(arr1)
    newarr = []

    for i in range(0, lenth):
        newarr_v = []
        for j in range(0, lenth):
            newarr_v.append(arr1[i][j])
        for j in range(0, lenth):
            newarr_v.append(arr2[i][j])
        newarr.append(newarr_v)
    for i in range(0, lenth):
        newarr_v = []
        for j in range(0, lenth):
            newarr_v.append(arr3[i][j])
        for j in range(0, lenth):
            newarr_v.append(arr4[i][j])
        newarr.append(newarr_v)

    return newarr

#슈트라젠 행렬의 곱 계산
def strassen_mul(a, b):

    c = [[0]*2 for i in range(2)]

    m1 = (a[0][0] + a[1][1]) * (b[0][0] + b[1][1])
    m2 = (a[1][0] + a[1][1]) * b[0][0]
    m3 = a[0][0] * (b[0][1] - b[1][1])
    m4 = a[1][1] * (b[1][0] - b[0][0])
    m5 = (a[0][0] + a[0][1]) * b[1][1]
    m6 = (a[1][0] - a[0][0]) * (b[0][0] + b[0][1])
    m7 = (a[0][1] - a[1][1]) * (b[1][0] + b[1][1])

    c[0][0] = m1+m4-m5+m7
    c[0][1] = m3+m5
    c[1][0] = m2+m4
    c[1][1] = m1+m3-m2+m6

    return c

#슈트라젠 함수 컨트롤러
def strassen(arr1, arr2):

    if len(arr1) == 2:
        return(strassen_mul(arr1, arr2))
    else:
        a1,a2,a3,a4 = strassen_div(arr1)
        b1,b2,b3,b4 = strassen_div(arr2)
        return strassen_merge(strassen(a1, b1), strassen(a2, b2), strassen(a3, b3), strassen(a4, b4))

#n by n 배열 만들기
def make_array(size):
    arr1 = []
    for i in range(0, size):
        arr2 = []
        for j in range(0, size):
            arr2.append(1)
        arr1.append(arr2)
    return(arr1)

def main():

    c = []
    n=2

    while(n<=pow(2, 5)):

        arr1 = make_array(n)
        arr2 = make_array(n)
        c.append(strassen(arr1, arr2))

        n = n * 2

    print(c)

#print(standard_mul([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
main()
