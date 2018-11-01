import re

#def read_file():
#    with open("words.txt") as file:
#        count_the = 0
#        for line in file:
#            for word in line.strip().split():           
#                count_the +=1                      
#        print(count_the)

def at_least():
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if len(word) >= 20:
                    print(word)
                    
def has_no_e(word):
    with open("words.txt") as file:
        for line in file:
            for letter in word:
                if 'e' not in word.lower():
                    return True
                else:
                    return False
def no_e():
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                count = 0
                if has_no_e() == True:
                    count += 1
        pass
            
            
        

    
    
        
                    
                    
                
            
            
    
            
        
    

if __name__ == "__main__":
    
    pass