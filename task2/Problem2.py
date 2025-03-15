import sys
import os
os.system('cls')




    


def main():
    a = [[1,2],[3,4],[5,6]]

    b = [[0]*len(a)]*len(a[0])
    

    for i in range(len(b)):
        c = [0] * len(a)
        for j in range(len(c)):
            c[j] = a[j][i]
        b[i] = c

    print(b)



    
     



if __name__ == '__main__':
    main()