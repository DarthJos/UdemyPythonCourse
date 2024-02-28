import json

with open("Files/questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)


for question in data:
    print(question["question_text"])

    for index, alternative in enumerate(question["alternatives"]):
        print("\t", index+1, "-", alternative)

    user_answer = int(input("Enter your answer: "))
    question["user_answer"] = user_answer       #Added new field to dictionary

score = 0
for index, question in enumerate(data):
    if question["user_answer"] == question["correct_answer"]:
        score += 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    message = (f"{result} {index + 1} - Your answer: {question['user_answer']}, "
               f"Correct answer: {question['correct_answer']}")
    print(message)

print(score, "/", len(data))
