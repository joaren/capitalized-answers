import json


def extract_correct_answer_choice(objects):
    capitalized_values = []
    for obj in objects:
        if "correctAnswerChoice" in obj and isinstance(obj["correctAnswerChoice"], str):
            capitalized_value = obj["correctAnswerChoice"].upper()
            capitalized_values.append(capitalized_value)
    return capitalized_values


with open('SACQMaster.json', 'r') as file:
    data = json.load(file)


capitalized_values = extract_correct_answer_choice(data)


json_string = json.dumps(capitalized_values, indent=2, separators=(',', ':'))


with open('capitalizedAnswers.json', 'w') as file:
    file.write(json_string)
