# interactive_bot.py

def interactive_bot():
    print("Welcome! Choose a question by typing the corresponding number:")
    print("1: Who are you?")
    print("2: Where are you from?")
    print("3: What do you do?")
    print("4: What is your specialization?")
    print("5: What do you like?")
    print("Type '0' to exit.")
    
    # Define responses for each question number
    responses = {
        1: "My name is Hashem Raed.",
        2: "I am from Lahij, Yemen.",
        3: "I am a cybersecurity student interested in ethical hacking and programming.",
        4: "I specialize in cybersecurity.",
        5: "I enjoy learning about software, especially cybersecurity."
    }
    
    while True:
        try:
            # Prompt user to enter a number for their question
            question_number = int(input("Enter the question number: "))
            
            # Exit condition
            if question_number == 0:
                print("Goodbye!")
                break
            
            # Get response based on question number or fallback if invalid
            response = responses.get(question_number, "Invalid choice. Please select a number between 1 and 5.")
            print(response)
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the interactive bot function
interactive_bot()
