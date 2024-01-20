import random

def gameloop(number: int):
    
    while True:
        
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess == number:
            print("You guessed it!")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
    

def main():
    
    number = random.randint(1, 100)
    
    gameloop(number)
    
    
if __name__ == "__main__":
    main()