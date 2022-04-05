def special(n):

    x = 197 + 232
    a = [-1]*(n+1)
    s = [-1]*(n+1)
    s[197] = 0
    s[232] = 0
    a[197] = 1
    a[232] = 1
    x = 0
    y = 0

    for i in range(233, n+1):
        a[i] = 1 + max(a[i-197], a[i-232])
        if a[i] == 0:
            a[i] = -1
        if a[i] == 1 + a[i-197]:
            s[i] =  i-197
        if a[i] == 1 + a[i-232]:
            s[i] = i-232



    while s[n] != -1:
        if(n-s[n] == 197):
            x+=1
        if(n-s[n] == 232):
            y+=1
        print(s[n])
        n = s[n]

    return x, y


def main():
    n = int(input("enter a number: "))
    print(special(n))
    # special(n)







if __name__ == "__main__":
    main()
