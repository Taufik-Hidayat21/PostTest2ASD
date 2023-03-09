#Nama : Taufik Hidayat
#NIM : 2209116097
#Kelas : Sistem Informasi B '22
import math
def jumpSearch1( arr , x , n ):
    step = math.sqrt(n)
    prev = 0
    for p in range(len(arr)):
        if type(arr[p]) == list:  
            hasil1 = jumpSearch1(arr[int(p)],x,len(arr[int(p)]))
            if hasil1 == -1:
                arr[int(p)] = 'zetemu'
                print()
            else:
                print(f'{x} is found at index {int(p)} column {hasil1}')
                exit()
    while arr[int(min(step, n)-1)] < x:
                prev = step
                step += math.sqrt(n)
                if prev >= n:
                    return -1
    while arr[int(prev)] < x:        
                prev += 1
                if prev == min(step, n):
                    return -1
    if arr[int(prev)] == x:
            return int(prev)
    return -1
def fib(n):
    if n < 1:
        return 1
    elif n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)
def fibonaccisearch(arr,x):
    n = 0
    while fib(n) < len(arr):
        n = n + 1
    offset = -1
    for f in range(len(arr)):
            if type(arr[f]) == list:
                qq = fibonaccisearch(arr[f],x)
                if qq == -1:
                    arr[f] = "zetemu"
                else:
                    print(f'{x} is found at index {f} column {qq}')
                    arr[f] = "zetemu"
                    exit()
    while (fib(n) > 1):
        i = min(offset + fib(n-2), len(arr) - 1)
        if (x > arr[i]):
            n = n-1
            offset = i
        elif (x < arr[i]):
            n = n-2
        else:
            return i
    if (fib(n-1) and arr[offset + 1] == x):
        return offset + 1
    return -1
def cari1(arr2,x2,n2):
    zz = jumpSearch1(arr2,x2,n2)
    if zz == -1:
        print(f'{x2} is not found')
    else:
        print(f'{x2} is found at index {zz}')
def cari2(arr3,x3):
    hasil1 = fibonaccisearch(arr3,x3)
    if hasil1 == -1:
        print(f'{x3} is not found')
    else:
        print(f'{x3} is found at index {hasil1}')
arr1 = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]



n1 = len(arr1)
while True:
    print(f'''
Data Yang tersedia
- Arsel
- Avivah
- Daiva
- Wahyu
- Wibi
''')
    print('''
    1. Jump Search
    2. Fibonacci Search
    ''')
    q1 = input("Masukan searching yang ingin digunakan: ")
    x1 = input("Masukan Elemen Data Yang Ingin Dicari: ")
    if q1 == '1':
        cari1(arr1,x1,n1)
        break
    elif q1 == '2':
        cari2(arr1,x1)
        break

    else:
        print("Masukan input dengan benar")