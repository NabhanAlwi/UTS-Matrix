#Kelompok 3
#M. dias rizky maulana, M. ihsan adzikra, Nabhan alwi ar-rifqi, Yahya ayyasy  
#Tiga fungsi : penjumlahan, pengurangan, perkalian (memakai matrix)

# Input Matriks A
print("== Input Matriks A ==")
baris_a = int(input('Masukkan jumlah baris untuk Matriks A : '))
kolom_a = int(input('Masukkan jumlah kolom untuk Matriks A : '))

A = []
for i in range(baris_a):
    baris = []
    for j in range(kolom_a):
        elemen = int(input(f"Masukkan elemen A[{i}][{j}]: "))
        baris.append(elemen)
    A.append(baris)

# Input Matriks B
print("\n== Input Matriks B ==")
baris_b = int(input('Masukkan jumlah baris untuk Matriks B : '))
kolom_b = int(input('Masukkan jumlah kolom untuk Matriks B : '))

B = []
for i in range(baris_b):
    baris = []
    for j in range(kolom_b):
        elemen = int(input(f"Masukkan elemen B[{i}][{j}]: "))
        baris.append(elemen)
    B.append(baris)

#fungsi pengurangan
def kurang (A,B):
    print('Hasil pengurangan matrix A dan B : \t')
    hasil1 = []
    for i in range (len(A)):
        hasil = []
        for j in range (len(B[0])):
            hasil.append(A[i][j] - B[i][j])
        hasil1.append(hasil)
    return(hasil1)


#fungsi penjumlahan
def tambah (A, B):
    print('Hasil penjumlahan matrix A dan B : \t')
    hasil2 = []
    for i in range (len(A)):
        hasil = []
        for j in range (len(B[0])):
            hasil.append(A[i][j] + B[i][j])
        hasil2.append(hasil)
    return(hasil2)


#fungsi perkalian
def kali (A, B):
    print('Hasil perkalian matrix A dan B: \t')
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    hasil3 = []
    for i in range(m):
        hasil = []
        for j in range(p):
            total = 0
            for k in range(n):
                total += A[i][k] * B[k][j]
            hasil.append(total)
        hasil3.append(hasil)
    return hasil3

print('~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=')

#tampilan
print('Matrix A: ')
for r in A:
    print(r)
    
print('Matrix B: ')
for r in B:
    print(r)

print('~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=')

#hasil operasi matrix
if len(A) != len(B) or len(A[0]) != len(B[0]):
    print('pengurangan gagal: Kedua matrix harus memiliki ukuran yang sama. \t')
else:
    min_result = kurang(A, B)
    for p in min_result:
        print(p)

print('~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=')

if len(A) != len(B) or len(A[0]) != len(B[0]):
    print('penjumlahan gagal: Kedua matrix harus memiliki ukuran yang sama. \t')
else:
    plus_result = tambah(A, B)
    for t in plus_result:
        print(t)

print('~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=')

if kolom_a != baris_b:
    print('perkalian gagal: Jumlah kolom A harus sama dengan jumlah baris B. \t')
else:
    k_result = kali(A, B)
    for m in k_result:
        print(m)