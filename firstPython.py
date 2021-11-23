if __name__ =='__main__':
    
    inrange_1=range(2,5)
    
    n = int(input("Enter your number "))
    
    if n%2 != 0:
        print("Weird")
    
    if n in inrange_1 and n%2 == 0:
        print("Not Weird")
            
    if n in range(6,21) and n%2 == 0:
        print("Weird")
            
    if n > 20 and n%2 == 0:
        print("Not Weird")