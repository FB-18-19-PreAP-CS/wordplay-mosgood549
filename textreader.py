import re

#def read_file():
#    with open("words.txt") as file:
#        count_the = 0
#        for line in file:
#            for word in line.strip().split():           
#                count_the +=1                      
#        print(count_the)

def at_least():
    '''
    reads word.text and prints the words with at least 20
    characters
    '''
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if len(word) >= 20:
                    print(word)
                    
def has_no_e(word):
    '''
    returns True if the word doesn't have the letter 'e' in it
    
    >>> has_no_e("Texas")
    False
    
    >>> has_no_e("pacific")
    True
    
    >>> has_no_e("eek")
    False
    '''
    for letter in word:
        if 'e' not in word.lower():
            return True
        else:
            return False
        
def no_e():
    '''
    counts the words that don't have an "e" in words.txt
    and prints the percentage of the words that don't have e
    '''
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
    '''
    returns True if the word given doesn't use the string of
    forbidden letters
    
    >>> avoids("apple","cbx")
    True
    
    >>> avoids("zebra", "xfe")
    False
    
    >>> avoids("annihilation", "zila")
    False
    '''
    for letter in word:
        for ele in no_no_letters:
            if ele in word.lower():
                return False
        else:
            return True
            
def count_avoids():
    '''
    counts the number of words in word.txt that don't contain any the
    forbidden letters that the user inputs
    '''
    count_av = 0
    no_no_letter = input("Enter a string of forbidden letters: ")
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if avoids(line, no_no_letter) == True:
                    count_av += 1
        print(count_av)
        
        
        
def uses_only(word,string):
    '''
    returns True if all of the letters in the string are the only letters used in the word
    
    >>> uses_only("pig", "igp")
    True

    >>> uses_only("babababa","abc")
    True

    >>> uses_only("reproachful", "acefhlo")
    False
    
    '''
    for letter in word:
        for ele in string:
            if letter not in string and word not in string:
                return False
    else:
        return True
        
def words_with_only():
    '''
    prints the words that only use the letters from the input
    '''
    let = input("Enter a string of letters: ")
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_only(word,let) == True:
                    print(word)
                    
    
def uses_all(word,string):
    '''
    returns true if all of the words in "string" are used in the word at least once
    
    >>> uses_all("bad","adb")
    True
    
    >>> uses_all("restriction","stoinrf")
    False
    
    >>> uses_all("africa","arfcai")
    True
    '''
    for letter in word:
        for ele in string:
            if letter not in string or ele not in word.lower():
                return False
        else:
            return True
        
def how_many_uses_all():
    '''
    counts and prints the number of words that have only the required letters in them
    '''
    count = 0
    let = input("Enter a string of required letters: ")
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_all(word,let) == True:
                    count +=1
        print(count)
        

def is_abecedarian(word):
    '''
    returns True if the letters in "word" appear in alphabetical order 
    
    >>> is_abecedarian("hijklm")
    True
    
    >>> is_abecedarian("fgco")
    False
    
    >>> is_abecedarian("qrrrs")
    True
    '''
    
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            i +=1
            return False
    else:
        return True
                    
def count_abecedarian():
    '''
    counts and prints the number of words in words.txt that are abecedarian
    '''
    count = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if is_abecedarian(word) == True:
                    count +=1
        print(count)

    
            
            
    
            
        
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #no_e()
