import random


class Question:
    def __init__(self, max_n: int = 10) -> None:
        self.man_n = max_n
        self.first_num = random.randint(0, max_n)
        self.second_num = random.randint(0, max_n)
        self.score = 0
        self.operand = random.choice(["+", "-", "x"])

    @property
    def answer(self) -> int:
        match self.operand:
            case "+":
                return self.first_num + self.second_num
            case "-":
                return self.first_num - self.second_num
            case "x":
                return self.first_num * self.second_num
            case _:
                raise ValueError("Invalid operand")

    def show(self, with_answer: bool = True) -> None:
        base_string = f"{self.first_num} {self.operand} {self.second_num}"
        output_string = (
            base_string + f" = {self.answer}" if with_answer else base_string
        )
        print(output_string)

    def score_answer(self, guess: int) -> int:
        result = guess == self.answer
        if result:
            print("Correct")
            print()
            return 1
        else:
            print(f"Incorrect. Correct answer was {self.answer}")
            print()
            return -1

    def take_answer(self) -> int | None:
        while True:
            try:
                input_guess = input("Answer: ")
                if input_guess == "q":
                    return None
                guess = int(input_guess)
                return self.score_answer(guess)
            except ValueError:
                continue


class Game:
    def __init__(self) -> None:
        self.max_n = 10
        self.total_score = 0
        self.individual_scores = []

    def introduce(self) -> None:
        intro = """
        Welcome to arithmetic.

        Answer questions correctly and the questions get harder.
        Answer questions incorrectly and the questions get easier.

        Enter `q` to quit.
        """
        print(intro)

    def longest_streak(self) -> int:
        if "i" not in self.individual_scores:
            return len(self.individual_scores)
        streaks = []
        current_streak = 0
        for idx, score in enumerate(self.individual_scores):
            if score == "i" or idx == len(self.individual_scores):
                streaks.append(current_streak)
            else:
                current_streak += 1
        return max(streaks)

    def form(self) -> float:
        last_ten = self.individual_scores[-10:]
        correct = len([score for score in last_ten if score == "c"])
        return correct / 10

    def adjust_difficulty(self) -> None:
        form = self.form()
        if form > 0.75:
            print("Increasing difficulty")
            self.max_n += 1
        if form < 0.25 and self.max_n > 1:
            print("Decreasing difficulty")
            self.max_n -= 1

    def play(self, max_questions: int = 10) -> None:
        self.introduce()
        for question in range(max_questions):
            if question > 0 and question % 10 == 0:
                self.adjust_difficulty()
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
        print(
            f"Final score: {self.total_score}. Most consecutive right answers: {self.longest_streak()}. Form: {self.form():.1%}. Questions answered: {len(self.individual_scores)}"
        )
