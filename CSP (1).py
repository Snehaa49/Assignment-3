import itertools

letters = ('S','E','N','D','M','O','R','Y')
digits = range(10)

for perm in itertools.permutations(digits, len(letters)):
    S,E,N,D,M,O,R,Y = perm

    if S == 0 or M == 0:
        continue

    send = S*1000 + E*100 + N*10 + D
    more = M*1000 + O*100 + R*10 + E
    money = M*10000 + O*1000 + N*100 + E*10 + Y

    if send + more == money:
        print("S =", S)
        print("E =", E)
        print("N =", N)
        print("D =", D)
        print("M =", M)
        print("O =", O)
        print("R =", R)
        print("Y =", Y)
        print("SEND =", send)
        print("MORE =", more)
        print("MONEY =", money)
        break
