
def palindrome():
    for i in range(1000000):
        num = str(i).zfill(6)
        if num[2:] == num[5:1:-1]:
            if num[1:] == num[5:1:-1]:
                if num[0:] == num[5:1:-1]:
                    pass
                    



def main():
    palindrome()
    
if __name__ == "__main__":
    main()
