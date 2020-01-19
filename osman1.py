for i in range (1,5):
    for k in range (5,i,-1):
        print(' ', end='')
    print(i,end=' ')
    for j in range(1, i):
        print(i,end=' ')
    print()