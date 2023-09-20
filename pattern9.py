'''
WAPP to print the pattern
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

n=int(input("enter limit: "))
for i in range(n):
    for j in range(n-i,0,-1):
        print(" ",end=" ")
    for k in range(0,2*i+1,1):   
        print("*",end=" ")
    print()



#output:
'''
enter limit: 5
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 


enter limit: 10
                    * 
                  * * * 
                * * * * * 
              * * * * * * * 
            * * * * * * * * * 
          * * * * * * * * * * * 
        * * * * * * * * * * * * * 
      * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * * * * * * 
'''
