from utils import Question

def main():
    q = Question()
    q.show(with_answer=False)
    q.take_answer()
    q.show(True)

if __name__ == "__main__":
    main()
