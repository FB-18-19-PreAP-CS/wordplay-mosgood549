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
    for letter in word:
        if 'e' not in word.lower():
            return True
        else:
            return False
def no_e():
    word_count = 0
    no_e = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                word_count += 1
                if has_no_e(word) == True:
                    no_e += 1
                pct = float(no_e/word_count)
        print(f"{pct*100:.3f}%")
        
        
        
def avoids(word, no_no_letters):
    for letter in word:
        for ele in no_no_letters:
            if ele in word.lower():
                return False
        else:
            return True
            
def count_avoids():
    count_av = 0
    no_no_letter = input("Enter a string of forbidden letters: ")
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if avoids(line, no_no_letter) == True:
                    count_av += 1
        print(count_av)
        
        
        
def uses_only(word,string):
    for letter in word:
        for ele in string:
            if ele in word.lower() and letter in ele:
                return True
        else:
            return False
        
def words_with_only():
    count_uo = 0
    string = input("Enter a string of required letters: ")
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_only(word,string) == True:
                    count_uo += 1
        print(count_uo)
                    
    
    
            
                
    
    

            
            
        

    
    
        
                    
                    
                
            
            
    
            
        
    

if __name__ == "__main__":
    pass
    #no_e()
