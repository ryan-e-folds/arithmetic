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

    def verify_answer(self, guess: int) -> bool:
        result = guess == self.answer
        if result:
            print("Correct")
            self.score += 1
        else:
            print("Incorrect")
            self.score -= 1
        print(f"Current score: {self.score}")
        return result
        
    def take_answer(self) -> int:
        while True:
            try:
                guess = int(input("Answer: "))
                return self.verify_answer(guess)
            except ValueError:
                continue
