'''
WAPP to print the pattern
*          *
  *     *
     *         
  *     *
*          *
'''

n=int(input("enter limit: "))
for i in range(n):
    for j in range(n):
     if j==i or j==n-i-1:
        print("*",end=" ")
     else:
        print(" ",end=" ")
        
    print()


#output:
'''
enter limit: 5
*       * 
  *   *   
    *     
  *   *   
*       * 


enter limit: 11
*                   * 
  *               *   
    *           *     
      *       *       
        *   *         
          *           
        *   *         
      *       *       
    *           *     
  *               *   
*                   * 
'''
