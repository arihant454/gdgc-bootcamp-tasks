import sys
import os
os.system('cls')




    


def main():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mode = 'row'
    b=[]

    if(mode=='column'):
        old_shape = (len(a),len(a[0]))
    else:
        old_shape = (len(a[0]),len(a))
    b_index=0
    if(mode=='column'):

        for i in range(old_shape[1]):
            sum = 0
            b.append(0)
            for j in range(old_shape[0]):
                sum += a[j][i]
            b[i]=sum/old_shape[0]
            b_index+=1
    else:
        for i in range(old_shape[1]):
            sum = 0
            b.append(0)
            for j in range(old_shape[0]):
                sum += a[i][j]
            b[i]=sum/old_shape[0]
            b_index+=1


        





    print(b)



    
     



if __name__ == '__main__':
    main()