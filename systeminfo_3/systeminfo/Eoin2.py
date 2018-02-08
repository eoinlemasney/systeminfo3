from certifi import __main__

def factorial(n):
      
    if n == 1:
            return 1
    else:
        return n*factorial(n-1)
    
    def main():
        n = 3
        f = factorial(n)
        print(f)
    
    if __main__ == "__main__":
        main()
        
print (factorial(3))