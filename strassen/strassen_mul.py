import time
import numpy as np

cnt = 0

def strassen_div(mat):

    global cnt
    lenth = int(len(mat)/2)
    div_mat1, div_mat2, div_mat3, div_mat4 = [[0]*lenth for i in range(lenth)], [[0]*lenth for i in range(lenth)], [[0]*lenth for i in range(lenth)], [[0]*lenth for i in range(lenth)]

    for i in range(0, lenth):
        for j in range(0, lenth):
            div_mat1[i][j] += mat[i][j]
            div_mat2[i][j] += mat[i][lenth+j]
            div_mat3[i][j] += mat[lenth+i][j]
            div_mat4[i][j] += mat[lenth+i][lenth+j]

    return div_mat1, div_mat2, div_mat3, div_mat4

def standard_mul(arr1, arr2):

    global cnt
    newarr = []

    for i in range(0, len(arr1)):
        newarr_v = []
        for j in range(0, len(arr1)):
            num = 0
            for k in range(0, len(arr1)):
                cnt += 1
                num += arr1[i][k] * arr2[k][j]
            # cnt += len(arr1) - 1
            newarr_v.append(num)
        newarr.append(newarr_v)

    return newarr

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

def strassen(arr1, arr2):
    """
    :param n: 행렬의 길이 2, 4, 8, 16, 32 ...
    :param arr1: 곱하고자 하는 행렬1
    :param arr2: 곱하고자 하는 행렬2
    :param arr3: 곱한 결과를 저장하는행렬
    :return: 없음
    """
    global cnt
    n = len(arr1)
    # print(n)
    if(n <= 2):
        cnt += n**3
        return np.dot(arr1,arr2)
    else:
        newlen = int(len(arr1) / 2)

        a11 = [[0 for i in range(0, newlen)] for j in range(0, newlen)]
        a12 = [[0 for i in range(0, newlen)] for j in range(0, newlen)]
        a21 = [[0 for i in range(0, newlen)] for j in range(0, newlen)]
        a22 = [[0 for i in range(0, newlen)] for j in range(0, newlen)]

        b11 = [[0 for i in range(0, newlen)] for j in range(0, newlen)]
        b12 = [[0 for i in range(0, newlen)] for j in range(0, newlen)]
        b21 = [[0 for i in range(0, newlen)] for j in range(0, newlen)]
        b22 = [[0 for i in range(0, newlen)] for j in range(0, newlen)]

        #divide array
        for i in range(0,newlen):
            for j in range(0,newlen):
                a11[i][j] = arr1[i][j] #A칸
                a12[i][j] = arr1[i][j+newlen] #B칸
                a21[i][j] = arr1[i+newlen][j] #C칸
                a22[i][j] = arr1[i+newlen][j+newlen] #D

                b11[i][j] = arr2[i][j] #A칸
                b12[i][j] = arr2[i][j+newlen] #B칸
                b21[i][j] = arr2[i+newlen][j] #C칸
                b22[i][j] = arr2[i+newlen][j+newlen] #D


        #슈트라센 연산
        M1 = strassen(a11, b11)
        # cnt += 2*len(a11)**2
        M2 = strassen(a11, b11)
        # cnt += len(a11)**2
        M3 = strassen(a11, b22)
        # cnt += len(a11)**2
        M4 = strassen(a22, b11)
        # cnt += len(a11)**2
        M5 = strassen(a11, b22)
        # cnt += len(a11)**2
        M6 = strassen(a11, b11)
        # cnt += 2*len(a11)**2
        M7 = strassen(a11, b11)
        # cnt += 2*len(a11)**2

        c11 = a11#standard_cal(standard_cal(M1,M4,"add"),standard_cal(M5,M7,"add"),"sub")
        c12 = a11#standard_cal(M3,M5,"add")
        c21 = a11#standard_cal(M2,M4,"add")
        c22 = a11#standard_cal(standard_cal(M1,M3,"add"),standard_cal(M2,M6,"sub"),"sub")

        C = [[0 for j in range(0, n)] for i in range(0, n)] #저장할 배열 C 생성-병
        for i in range(0,newlen):
            for j in range(0,newlen):
                C[i][j] = c11[i][j]
                C[i][j+newlen] = c12[i][j]
                C[i+newlen][j] = c21[i][j]
                C[i+newlen][j+newlen] = c22[i][j]
        # print(C)
        cnt += 7
        return C


def make_array(size):
    arr1 = []
    for i in range(0, size):
        arr2 = []
        for j in range(0, size):
            arr2.append(1)
        arr1.append(arr2)
    return(arr1)

def main():

    n=32

    while(n<=2**10):

        print("n by n = ", n)

        global cnt
        arr1 = make_array(n)
        arr2 = make_array(n)

        cnt = 0
        strassen(arr1,arr2)
        comp1 = cnt

        cnt = 0
        standard_mul(arr1,arr2)
        comp2 = cnt

        print("comp1 =", comp1)
        print("comp2 =", comp2)

        # break
        if comp1<comp2:
            break
        # print(cnt)
        n = n * 2
main()
