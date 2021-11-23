if __name__ =='__main__':
    
    inrange_1=range(2,5)
    
    n = int(input("Enter your number "))
    
    if n%2 == 0:
        
        if n in inrange_1:
            print("Not Weird")
            
        if n in range(6,20):
            print("Weird")
            
        if n > 20:
            print("Not Weird")
        
    else:
        print("Weird")
        