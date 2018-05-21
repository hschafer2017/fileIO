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
            guess = input(question + ': ').lower()
            if answer == guess:
                score += 1
            else:
                return None
        print(score)
            
    
    elif options == "2": 
        print("Add your question")
        f = open('questions.txt', 'a')
        questions = input("Enter the question: ")
        question = str(f.write('\n' + questions + '|'))
        answers = input("Enter the answer: ")
        question = str(f.write(answers))
        f.close()
    
    elif options == "3": 
        print("So you're done playing?")
        return None 
    
    else: 
        print("That's not an option. Please try again.")
        printMenu()
    
        
printMenu()
