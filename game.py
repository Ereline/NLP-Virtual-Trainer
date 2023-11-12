import csv
import random


def load_questions(filename='question.csv'):
    questions = []
    with open(filename, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # пропустим заголовок
        for row in csv_reader:
            question_data = {
                'number': row[0],
                'question': row[1],
                'correct_answer': row[2]
            }
            questions.append(question_data)
    return questions

def lore(filename='lore.txt'):
    filelore = open(filename, "r", encoding='utf-8')
    lines = filelore.readlines()
    rand_line_lore = random.randrange(1, len(lines) - 1)
    return lines[rand_line_lore]


def achivment(Score, filenameach='achivment.csv'):
    achivments = []
    with open(filenameach, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # пропустим заголовок
        for row in csv_reader:
            if float(Score) == float(row[0]):
                print(f"\n-ВЫ-ПОЛУЧИЛИ-ДОСТИЖЕНИЕ-")
                print(row[1])
                print("-------------")
                break

def get_other_answers(questions, current_question):
    other_answers = []
    for question in questions:
        if question != current_question:
            other_answers.append(question['correct_answer'])
    return random.sample(other_answers, 2)


def main():
    print("----------------------------------------------------")
    print("|Добро пожаловать в игру 'Машинисты против Ящеров'!|")
    print("\--------------------------------------------------/")

    while True:
        play_game()
        restart()

def restart():
    restart = input("Хотите начать заново? (да/нет): ")
    if restart.lower() in ['y', 'yes', 'да', 'д']:
        play_game()
    elif restart.lower() in ['n', 'no', 'нет', 'н']:
        print("До свидания!")
        exit()

def play_game():
    print("Вы - машинист. Ваша задача - победить ящеров.\n")
    questions = load_questions()


    while True:
        print("Выберите действие:")
        print("1. Напасть на ящеров")
        print("2. Попытаться убежать")
        print("3. Закончить игру")

        choice = input("Ваш выбор: ")

        if choice == "1":
            ask_question(questions)
        elif choice == "2":
            if try_to_escape():
                print("Вы смогли убежать от ящеров!")
            else:
                print("Увы, ящеры догнали вас. Игра окончена.")
                break
        elif choice == "3":
            print("Вы завершили игру.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")

def ask_question(questions, Score = 1):
    current_question = random.choice(questions)
    print(f"\n------------------------------")
    print("Приключение на 5-ю точку №", Score)
    print("------------------------------")

    print(f"\n{lore()}") #Описание лора

    print(f"\nВопрос #{current_question['number']}: {current_question['question']}")
    
    
    other_answers = get_other_answers(questions, current_question) # Получаем два неправильных ответа из других вопросов
    
    answer_options = [current_question['correct_answer']] + other_answers# Создаем список из трех вариантов ответа + fortune
    
    # Перемешиваем варианты ответов
    random.shuffle(answer_options)
    answer_options.append("Пронесёт")

    for i, answer in enumerate(answer_options, start=1):
        print(f"{i}. {answer}")

    user_answer = input("Выберите номер верного ответа: ")

    if int(user_answer) == 4:
        fortune()
        achivment(Score)
        ask_question(questions, Score = Score + 1)
    elif user_answer.isdigit() and 1 <= int(user_answer) <= len(answer_options):
        if answer_options[int(user_answer) - 1] == current_question['correct_answer']:
            print("Поздравляем! Вы правильно ответили. Ящеры отступают.")
            achivment(Score)
            ask_question(questions, Score = Score + 1)
            
            
# achivment after win


        else:
            if random.random() <= 0.1: # 10% шанс промахнуться
                print("Вы ошиблись. Ящер атакует в ответ. Но вы чертовски везучи, ящер промахивается.")
            else:
                print("Увы, вы ошиблись. Ящеры сильны, и они атакуют в ответ.")
                print("----------------------------------------------------")
                print("|---------------ВЫ БЫЛИ ПОВЕРЖЕНЫ!-----------------|")
                print("\--------------------------------------------------/")


                restart()
    else:
        print("Некорректный ввод. Пожалуйста, выберите номер верного ответа от 1 до ", len(answer_options))

def try_to_escape():
    print("Вы пытаетесь убежать от ящеров...")
    return random.choice([True, False, False, False])

def fortune():
    dice = random.random()
    if dice <= 0.01:  # 1% шанс успешного побега
        print(f"\nКритический успех! В попытке ударить вас ящер промахивается и попадает по своему собрату")
        
    else:
        print(f"\nКритическая неудача! Вы подскальзываетесь и падаете лицом в лужу. Ящеры смеються над вами")
        print("----------------------------------------------------")
        print("|----------------ВЫ БЫЛИ СРАЖЕНЫ!------------------|")
        print("\--------------------------------------------------/")
        restart()

if __name__ == "__main__":
    main()
