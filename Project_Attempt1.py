questionList = [
    {
        "questionNumber": "1",
        "question": "What is the capital of Thailand?",
        "choices": ["1) Paris", "2) London", "3) Tokyo", "4) Bangkok"],
        "answer": 4
    },
    {
        "questionNumber": "2",
        "question": "What country is the Eiffel Tower in?",
        "choices": ["1) Scotland", "2) France", "3) Belgium", "4) Australia"],
        "answer": 2
    },
    {
        "questionNumber": "3",
        "question": "What movie did Michael J. Fox learn to skateboard for?",
        "choices": ["1) Back to the Future", "2) Batman", "3) Teen Wolf", "4) Family Ties"],
        "answer": 1
    },
    {
        "questionNumber": "4",
        "question": "In Norse mythology, what did Odin trade an eye for?",
        "choices": ["1) Wisdom", "2) Strength", "3) Influence", "4) G.O.A.T. status"],
        "answer": 1
    },
    {
        "questionNumber": "5",
        "question": "What year did the US issue a patent on the production of margarine?",
        "choices": ["1) 1913", "2) 1871", "3) 1849", "4) 1892"],
        "answer": 2
    },
    {
        "questionNumber": "6",
        "question": "What is an elver?",
        "choices": ["1) Young eel", "2) Young elk", "3) Derogatory term", "4) Term for young elves in Middle Earth"],
        "answer": 1
    },
    {
        "questionNumber": "7",
        "question": "What was the first Hot Wheels car?",
        "choices": ["1) Batmobile", "2) Mercedes-Benz 300SL Gullwing Coupe", "3) Camaro", "4) Ford F150"],
        "answer": 3
    },
    {
        "questionNumber": "8",
        "question": "Which element appears tenth on the periodic table?",
        "choices": ["1) Oxygen", "2) Argon", "3) Potassium", "4) Neon"],
        "answer": 4
    },
    {
        "questionNumber": "9",
        "question": "What part of the eye gives it colour?",
        "choices": ["1) Cornea", "2) Pupil", "3) Iris", "4) Lid"],
        "answer": 3
    },
    {
        "questionNumber": "10",
        "question": "Who said: 'I came, I saw, I conquered.'?",
        "choices": ["1) Marie Antoinette", "2) Jesus Christ", "3) Napoleon Bonaparte", "4) Julius Caesar"],
        "answer": 4
    }
]


score = 0

def runQuiz(score):
    questionNum = 0
    for question in questionList:
        questionNum += 1
        print(f"\n{questionNum}: {question["question"]}")
        for choices in question["choices"]:
            print(choices)
        while True:
            userInput = input("Please input your numerical answer: ")
            if check_answer(userInput, question["answer"]):
                score += 1
            break
    return score

def check_answer(userInput, answer):
    if userInput.isdigit() == True:
        userInput = int(userInput)
        if userInput == answer:
            print("Correct.")
            return True
        else:
            if userInput > 4 or userInput <= 0:
                print("Invalid input. Answer must range from 1-4.")
            else:
                print("Incorrect.")
                return False
    else:
        print("Invalid input. Must be an integer.")
    return score

score = runQuiz(score)
print()
print(f"You scored {score} out of {len(questionList)}")
if score < 10:
    print("Better luck next time, nerd!")
else:
    print("GG")