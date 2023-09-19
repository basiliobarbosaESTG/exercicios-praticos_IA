# inicializar uma lista vazia para guardar a informacao dos voos
flights = []


def add_flight():  # funcao para adicionar um novo voo á lista
    # informacoes do voo introduzidas pelo utilizador
    number = input("Introduza o número do voo: ")
    origin = input("Introduza a origem: ")
    destination = input("Introduza o destino: ")
    date_time = input("Introduza a hora de partida: ")

    # cria uma tupla com as informações do voo e adiciona à lista
    flights.append((number, origin, destination, date_time))
    print("Voo adicionado com sucesso!")


def search_flight():  # função para pesquisar pelo numero do voo
    # utilizador dá informacao pelo numero de voo
    number = input("Introduza o número do voo: ")

    # percorre a lista de voos e pesquisa o voo correspondente
    for flight in flights:
        if flight[0] == number:
            print(f"Número do voo: {flight[0]}")
            print(f"Origem: {flight[1]}")
            print(f"Destino: {flight[2]}")
            print(f"Hora de partida: {flight[3]}")
            break
    else:
        print("Voo não encontrado.")


# Menu para introduzir opcao
while True:
    print("\n1. Adicionar um novo voo\n2. Pesquisar por voo\n3. Sair")
    choice = int(input("Introduza a opcao: "))

    if choice == 1:
        add_flight()
    elif choice == 2:
        search_flight()
    elif choice == 3:
        break
    else:
        print("Escolha não é valida. Introduza novamente.")
