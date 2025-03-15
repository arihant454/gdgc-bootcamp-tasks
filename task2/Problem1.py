import sys
import os
os.system('cls')




    


def main():
    a = [[1,2],[2,4]]
    b = [1,2]

    if(len(a[0]) != len(b)):
        print(-1)
    c = [0] * len(b)

    for i in range(len(c)):
        sum = 0 
        for j in range(len(a[i])):
            sum += b[j] * a[i][j]
        c[i] = sum

    print(f"Answer is {c}")
     



if __name__ == '__main__':
    main()