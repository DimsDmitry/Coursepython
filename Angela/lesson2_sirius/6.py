n = int(input())
rem = n % 100

# bochka: 1 21 31 41 ... 101 ... 1001 (кроме 11)
# bochek: 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 25 10 15 20 30 35 40 45
# bochki: 2 3 4 22 23 24

if rem <= 10 or rem >= 20:
    if (n != 11) and (n % 10 == 1):
        print(n, 'bochka')
    elif n % 10 == 0 or (n % 10 >= 5):
        print(n, 'bochek')
    else:
        print(n, 'bochki')

else:
    print(n, 'bochek')
