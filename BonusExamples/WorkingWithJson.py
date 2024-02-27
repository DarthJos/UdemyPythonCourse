import json

with open("Files/questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)
score = 0

for question in data:
    print(question["question_text"])

    for index, alternative in enumerate(question["alternatives"]):
        print("\t", index+1, "-", alternative)

    user_answer = int(input("Enter your answer: "))
    question["user_answer"] = user_answer       #Added new field to dictionary

    if question["user_answer"] == question["correct_answer"]:
        score += 1

print(data)
print(score, "/", len(data))