import requests
import os
import platform
import html

def quiz(amount):
    url = f"https://opentdb.com/api.php?amount={amount}&category=9&type=boolean"
    data = requests.get(url)
    return data.json()

class QuizGame:
    def __init__(self, trivia):
        self.questions = trivia["results"]
        self.totals = len(self.questions)
        self.score = 0
        self.current = 0

    def update(self):
        """Clear screen for every game"""
        os.system("cls" if platform.system() == "Windows" else "clear")

    def check_answer(self, correct_ans, usr_ans ):
        """Check answer given by user with correct answer in the trivia quiz"""
        return correct_ans.lower() == usr_ans.lower()

    def show_score(self):
        """Show score of correct answer from user"""
        print("Game Completed! Congratulations")
        print(f"Your final score is {self.score}/{self.totals}")


    def play(self):
        """Start the game"""
        for i, q in enumerate(self.questions, start=1):
            self.update()
            question = html.unescape(q["question"])
            correct = q["correct_answer"]

            print(f"Q{i}: {question}?")
            input_user = ""
            while input_user not in ["true", "false"]:
                input_user = input("Your asnwer (True/False): ").lower()

            if self.check_answer(correct, input_user):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")

            input("Press enter to continue...")

        self.show_score() 

    def __str__(self):
        """Show Welcome to the User"""
        return f"WELCOME to the QuizGame. \nTotal questions {self.totals}. Good Luck!\n"

def main():
    amount = 5
    trivia = quiz(amount=amount)
    game = QuizGame(trivia=trivia)
    print(game)
    input("Press Enter or Any button to start...")
    game.play()


if __name__ == "__main__":
    app = main()
