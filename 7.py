
def three_consec():
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                for i in range(len(word)-5):
                    if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
                        print(word)
                        
                        
def main():
    three_consec()
    
if __name__ == "__main__":
    main()
    
                