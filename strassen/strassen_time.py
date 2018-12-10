import math
import timeit
import numpy as np

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

def standard_add(arr1, arr2):

    newarr = []

    for i in range(0, len(arr1)):
        newarr_v = []
        for j in range(0, len(arr1)):
            newarr_v.append(arr1[i][j] + arr2[i][j])
        newarr.append(newarr_v)

    return newarr

def standard_sub(arr1, arr2):

    newarr = []

    for i in range(0, len(arr1)):
        newarr_v = []
        for j in range(0, len(arr1)):
            newarr_v.append(arr1[i][j] - arr2[i][j])
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
    n = len(arr1)
    # print(n)
    if(n <= 2):

        c = [[0]*2 for i in range(2)]

        m1 = (arr1[0][0] + arr1[1][1]) * (arr2[0][0] + arr2[1][1])
        m2 = (arr1[1][0] + arr1[1][1]) * arr2[0][0]
        m3 = arr1[0][0] * (arr2[0][1] - arr2[1][1])
        m4 = arr1[1][1] * (arr2[1][0] - arr2[0][0])
        m5 = (arr1[0][0] + arr1[0][1]) * arr2[1][1]
        m6 = (arr1[1][0] - arr1[0][0]) * (arr2[0][0] + arr2[0][1])
        m7 = (arr1[0][1] - arr1[1][1]) * (arr2[1][0] + arr2[1][1])

        c[0][0] = m1+m4-m5+m7
        c[0][1] = m3+m5
        c[1][0] = m2+m4
        c[1][1] = m1+m3-m2+m6

        return c

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
        M1 = strassen(standard_add(a11, a22), standard_add(b11, b22))
        M2 = strassen(standard_add(a21, a22), b11)
        M3 = strassen(a11, standard_sub(b12,b22))
        M4 = strassen(a22, standard_sub(b21,b11))
        M5 = strassen(standard_add(a11,a12),b22)
        M6 = strassen(standard_sub(a21,a11),standard_add(b11,b12))
        M7 = strassen(standard_sub(a12,a22),standard_add(b21,b22))

        c11 = standard_add(standard_sub(standard_add(M1,M4),M5),M7)
        c12 = standard_add(M3,M5)
        c21 = standard_add(M2,M4)
        c22 = standard_add(standard_sub(standard_add(M1,M3),M2),M6)

        C = [[0 for j in range(0, n)] for i in range(0, n)] #저장할 배열 C 생성-병
        for i in range(0,newlen):
            for j in range(0,newlen):
                C[i][j] = c11[i][j]
                C[i][j+newlen] = c12[i][j]
                C[i+newlen][j] = c21[i][j]
                C[i+newlen][j+newlen] = c22[i][j]
        # print(C)

        return C


def make_array(size):
    arr1 = []
    for i in range(0, size):
        arr2 = []
        for j in range(0, size):
            arr2.append(0)
        arr1.append(arr2)
    return(arr1)

def main():

    n=2

    while(True):

        print("n by n = ", n)

        arr1 = make_array(n)
        arr2 = make_array(n)

        start = timeit.default_timer()
        strassen(arr1,arr2)
        stop = timeit.default_timer()
        time1 = (stop - start)

        start = timeit.default_timer()
        standard_mul(arr1,arr2)
        stop = timeit.default_timer()
        time2 = (stop - start)

        print("time1 =", time1)
        print("time2 =", time2)

        if time1<time2:
            break
        # print(cnt)

        n = n * 2
main()
