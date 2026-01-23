# Question list - question, multiple choices, correct answer
questionList = [
    {
        "question": "What is the capital of Thailand?",
        "choices": ["1) Paris", "2) London", "3) Tokyo", "4) Bangkok"],
        "answer": 4
    },
    {
        "question": "What country is the Eiffel Tower in?",
        "choices": ["1) Scotland", "2) France", "3) Belgium", "4) Australia"],
        "answer": 2
    },
    {
        "question": "What movie did Michael J. Fox learn to skateboard for?",
        "choices": ["1) Back to the Future", "2) Batman", "3) Teen Wolf", "4) Family Ties"],
        "answer": 1
    },
    {
        "question": "In Norse mythology, what did Odin trade an eye for?",
        "choices": ["1) Wisdom", "2) Strength", "3) Influence", "4) G.O.A.T. status"],
        "answer": 1
    },
    {
        "question": "What year did the US issue a patent on the production of margarine?",
        "choices": ["1) 1913", "2) 1871", "3) 1849", "4) 1892"],
        "answer": 2
    },
    {
        "question": "What is an elver?",
        "choices": ["1) Young eel", "2) Young elk", "3) Derogatory term", "4) Term for young elves in Middle Earth"],
        "answer": 1
    },
    {
        "question": "What was the first Hot Wheels car?",
        "choices": ["1) Batmobile", "2) Mercedes-Benz 300SL Gullwing Coupe", "3) Camaro", "4) Ford F150"],
        "answer": 3
    },
    {
        "question": "Which element appears tenth on the periodic table?",
        "choices": ["1) Oxygen", "2) Argon", "3) Potassium", "4) Neon"],
        "answer": 4
    },
    {
        "question": "What part of the eye gives it colour?",
        "choices": ["1) Cornea", "2) Pupil", "3) Iris", "4) Lid"],
        "answer": 3
    },
    {
        "question": "Who said: 'I came, I saw, I conquered.'?",
        "choices": ["1) Marie Antoinette", "2) Jesus Christ", "3) Napoleon Bonaparte", "4) Julius Caesar"],
        "answer": 4
    }
]

# Initialising just the one variable
score = 0

# Runs through each question in the question list, asking for an input and checking the input
def runQuiz(score):
    questionNum = 0
    for question in questionList:
        questionNum += 1
        print(f"\n{questionNum}: {question["question"]}")
        for choices in question["choices"]:
            print(choices)
        while True:
            userInput = input("Please input your numerical answer: ")

            if userInput.isdigit() == False or 1 > int(userInput) or int(userInput) > 4:
                while True:
                     print("Invalid input. Answer must be an integer, and must range from 1-4.")
                     userInput = input("Please input your numerical answer: ")
                     if userInput.isdigit() == True and (1 <= int(userInput) <= 4):
                         break
            break
        TrueOrFalse = checkAnswer(userInput, question["answer"], score)
        if TrueOrFalse == True:
            score = score + 1
    return score

# Logic to check the input - is it right, wrong, or invalid?
def checkAnswer(userInput, answer, score):
    if int(userInput) == answer:
        print("Correct.")
        score = score + 1
        return True
    else:
        print("Incorrect.")
        return False

# Iterates through the questions using the function(s) and then outputs 2 messages
score = runQuiz(score)
print()
print(f"You scored {score} out of {len(questionList)}")
if score < 10:
    print("Better luck next time!")
else:
    print("Well played!")
