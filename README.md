AI Number Guessing Game 🎲
This is a simple AI-powered number guessing game built in Python. The AI uses a binary search algorithm to guess a number that the user is thinking of within a specified range.

Features
The AI guesses numbers efficiently using binary search logic.
User-friendly prompts to guide the gameplay.
Easy to customize for different number ranges.
How It Works
The user thinks of a number within a predefined range (default: 1 to 100).
The AI makes a guess and asks the user if the guess is:
Correct
Higher
Lower
The AI adjusts its guesses based on the user's input and repeats the process until it finds the correct number.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/Dr0m0x/AI_Number_Guessing.git
Navigate to the project directory:
bash
Copy code
cd AI_Number_Guessing
Run the game using Python:
bash
Copy code
python AI_Number_Guessing.py
Requirements
Python 3.6 or higher
How to Play
Think of a number within the range (default is 1–100).
Follow the AI's prompts in the terminal.
Let the AI guess your number by responding with:
higher (if your number is greater than the AI's guess),
lower (if your number is less than the AI's guess), or
correct (if the AI guessed your number correctly).
Customization
To change the guessing range, modify the call to ai_guess_number() at the end of the script:

python
Copy code
ai_guess_number(low=1, high=1000)
Example Output
python
Copy code
Think of a number between 1 and 100, and I'll guess it!
Press Enter when you're ready...

My guess is 50. Is it correct?
Type 'higher', 'lower', or 'correct': higher

My guess is 75. Is it correct?
Type 'higher', 'lower', or 'correct': lower

My guess is 63. Is it correct?
Type 'higher', 'lower', or 'correct': correct

Yay! I guessed it in 3 attempts.
Contributing
Feel free to fork this repository and make your own improvements! Pull requests are welcome.
