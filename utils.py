import random

class Question():

    def __init__(self, max_n: int = 10) -> None:
        self.man_n = max_n
        self.first_num = random.randint(0, max_n)
        self.second_num = random.randint(0, max_n)
        self.answer = self.first_num + self.second_num
        self.score = 0

    def show(self, with_answer: bool = True) -> None:
        base_string = f"{self.first_num} + {self.second_num}"
        output_string = base_string + f" = {self.answer}" if with_answer else base_string
        print(output_string)

    def score_answer(self, guess: int) -> int:
        result = guess == self.answer
        if result:
            print("Correct")
            print()
            return 1
        else:
            print("Incorrect")
            print()
            return -1
        
    def take_answer(self) -> int:
        while True:
            try:
                input_guess = input("Answer: ")
                if input_guess == "q":
                    return 0
                guess = int(input_guess)
                return self.score_answer(guess)
            except ValueError:
                continue

class Game():

    def __init__(self, max_n: int = 10) -> None:
        self.max_n = max_n
        self.total_score = 0
        self.individual_scores = []

    def longest_streak(self) -> int:
        streaks = []
        on_streak = False
        current_streak = 0
        for idx, score in enumerate(self.individual_scores):
            if score == "i" or idx == len(self.individual_scores):
                streaks.append(current_streak)
            else:
                current_streak += 1
        return max(streaks)

    def play(self, max_questions: int = 5) -> None:
        for question in range(max_questions):
            q = Question(max_n=self.max_n)
            q.show(with_answer=False)
            result = q.take_answer()
            if not result:
                break
            self.total_score += result
            if result == 1:
                self.individual_scores.append("c")
            else:
                self.individual_scores.append("i")
        print()
        print(f"Final score: {self.total_score}. Most consecutive right answers: {self.longest_streak()}")



