def ai_guess_number(low, high):
    print("Think of a number between 1 and 100, and I'll guess it!")
    input("Press Enter when you're ready...")

    attempts = 0
    while low <= high:
        # AI's guess: mid-point of the range
        guess = (low + high) // 2
        attempts += 1

        print(f"My guess is {guess}. Is it correct?")
        response = input("Type 'higher', 'lower', or 'correct': ").lower()

        if response == 'correct':
            print(f"Yay! I guessed it in {attempts} attempts.")
            break
        elif response == 'higher':
            low = guess + 1
        elif response == 'lower':
            high = guess - 1
        else:
            print("Invalid input. Please type 'higher', 'lower', or 'correct'.")

    if low > high:
        print("Hmm... Are you sure your answers were correct?")

# Run the game
ai_guess_number(1, 100)
