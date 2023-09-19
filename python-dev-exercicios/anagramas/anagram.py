# Retorna True se word1 e word2 forem anagramas uma da outra, e False caso contrário.
def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())


# Lê um ficheiro de texto contendo uma lista de palavras e imprime todas as palavras no arquivo que são anagramas de user_word.
def find_anagrams(file_name, user_word):
    with open(file_name, 'r') as f:
        for line in f:
            word = line.strip()
            if is_anagram(word, user_word):
                print(word)


if __name__ == '__main__':
    file_name = input('Introduza o nome do ficheiro: ')
    user_word = input('Introduza a palavra a procurar: ')
    find_anagrams(file_name, user_word)
