'''
WAPP to print the pattern
* * * * * *
*         *
*         *
*         *
* * * * * *
'''

n=int(input("enter limit: "))
for i in range(n):
    if i==0 or i==n-1:
     for j in range(n):
        print("*",end=" ")
    
     
    else:
        for k in range(n):
         if k==0 or k==n-1:   
          print("*",end=" ")
         else:
          print(" ",end=" ")
    
    print()



#output:
'''
enter limit: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 


enter limit: 10
* * * * * * * * * * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
* * * * * * * * * * 
'''
    
