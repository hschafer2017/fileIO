import random 
import pprint

def printMenu():
    print("Enter an Option:")
    print("1. Ask Questions")
    print("2. Add a Question")
    print("3. Exit Game")




    options = input("Please choose and option (1-3): ")
    
    score = 0
    
    if options == "1":
        f = open('questions.txt', 'r')
        lines = f.read().split('\n')
        f.close()
        for line in lines:
            question, answer = line.split('|')
            newQ = random.sample(question,len(question))
            print(newQ)
            guess = input(question + ': ').lower()
            if answer == guess:
                score += 1
            else:
                print("You Lost!")
                print(score)
                return None
        print(score)
            
    
    elif options == "2": 
        print("Add your question")
        f = open('questions.txt', 'a')
        questions = str(input("Enter the question: "))
        question = f.write(questions + '|')
        answers = str(input("Enter the answer: "))
        question = f.write(answers +'\n')
        f.close()
    
    elif options == "3": 
        print("So you're done playing?")
        return None 
    
    else: 
        print("That's not an option. Please try again.")
        printMenu()
    
        
printMenu()

#  Asking is read only 
# Adding is appending 