import random

# Lista das perguntas e respostas
questions = [
    {
        "question": "Qual é a capital de França?",
        "options": ["A. Paris", "B. Madrid", "C. Berlin", "D. Roma"],
        "answer": "A"
    },
    {
        "question": "Qual é o equivalente em Celsius de 77 graus Fahrenheit?",
        "options": ["A. 15", "B. 25", "C. 55", "D. 0"],
        "answer": "B"
    },
    {
        "question": "Que planeta não orbita o Sol?",
        "options": ["A. Terra", "B. Venus", "C. Marte", "D. Lua"],
        "answer": "D"
    },
    {
        "question": "Qual é o símbolo químico do ouro?",
        "options": ["A. Au", "B. Ag", "C. Cu", "D. Fe"],
        "answer": "A"
    },
    {
        "question": "Qual é a moeda do Japão?",
        "options": ["A. Yen", "B. Dollar", "C. Euro", "D. Pound"],
        "answer": "A"
    },
    {
        "question": "Qual é a montanha mais alta do mundo?",
        "options": ["A. Monte Kilimanjaro", "B. Monte Everest", "C. Monte Fuji", "D. Monte McKinley"],
        "answer": "B"
    },
    {
        "question": "Qual era o nome do meio de Walt Disney?",
        "options": ["A. James", "B. Elias", "C. Winston", "D. Benjamin"],
        "answer": "B"
    },
    {
        "question": "Em que ano Martin Luther King Jr. ganhou o Prêmio Nobel da Paz?",
        "options": ["A. 1957", "B. 1963", "C. 1964", "D. 1968"],
        "answer": "C"
    },
    {
        "question": "O cantor Elton John foi presidente de que clube de futebol inglês?",
        "options": ["A. Watford", "B. Aston Villa", "C. Everton", "D. Newcastle"],
        "answer": "A"
    },
    {
        "question": "Antes de se tornar a rainha do pop, de que banda fez parte a cantora Madonna?",
        "options": ["A. Culture Club", "B. Tom Tom Club", "C. The Gun Club", "D. Breakfast Club"],
        "answer": "D"
    }
]


def display_question(question):  # imprime a questao
    print(question["question"])
    for option in question["options"]:
        print(option)
    print()


def fifty_fifty(question):  # opcao 50/50
    options = question["options"]
    correct_answer = question["answer"]
    # options.remove(correct_answer)
    incorrect_answer = random.choice(options)
    return [correct_answer, incorrect_answer]


def play_game():
    correct_answers = 0
    total_prize = 0
    help_used = False
    skip_used = False

    for i in range(len(questions)):
        display_question(questions[i])

        while True:
            choice = input(
                "Digite a sua opcao (A/B/C/D) ou digite 'help' para obter ajuda 50/50, ou 'skip' para saltar a pergunta: ").upper()

            if choice == "HELP":
                if not help_used:
                    help_used = True
                    options = fifty_fifty(questions[i])
                    print(
                        f"As opções 50/50 são: {options[0]} ou {options[1]}")
                else:
                    print(
                        "Você já usou a ajuda 50/50. Escolha uma opção ou digite 'skip' para saltar a pergunta.")
                continue

            if choice == "SKIP":
                if not skip_used:
                    skip_used = True
                    print("A saltar a pergunta...")
                    break
                else:
                    print(
                        "Já saltou esta pergunta. Escolha uma opção ou digite 'help' para obter ajuda 50/50.")
                continue

            if choice not in ["A", "B", "C", "D"]:
                print(
                    "Escolha inválida. Por favor, escolha A, B, C, D, 'help' ou 'skip'.")
                continue

            if choice == questions[i]["answer"]:
                print("Correto!")
                correct_answers += 1
                total_prize += 1000
            else:
                print("Errado.")
            break

    print(f"Número de respostas corretas: {correct_answers}")
    print(f"Prêmio total ganho: €{total_prize}")


play_game()
