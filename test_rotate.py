from functions import function_to_test as ft

A = [3, 8, 9, 7, 6]

for K in range(1,20):
    print('K = {} : {}'.format(K,ft.rotate_array(A, K)))

A = []

for K in range(1,5):
    print('K = {} : {}'.format(K,ft.rotate_array(A, K)))