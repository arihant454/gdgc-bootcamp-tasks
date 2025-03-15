import sys
import os
os.system('cls')




    


def main():
    a = [[1,2,3,4],[5,6,7,8]]
    new_shape = (4, 2)
    old_shape = (len(a),len(a[0]))
    
    b = []
    count =0
    for i in a:
        
        for j in i:
            
            count+=1
    #special case    
    if(count != new_shape[0]*new_shape[1]):
        print("not possible")

    row =0
    col = 0
    for i in range(new_shape[0]):
        b.append([])
        for j in range(new_shape[1]):
            
            b[i].append(a[row][col])
            col+=1
            if(col==old_shape[1]):
                col=0
                row+=1
        





    print(b)



    
     



if __name__ == '__main__':
    main()