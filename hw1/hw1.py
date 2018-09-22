import random

def open_file(fname): #open file
    with open(fname, encoding = 'utf-8') as f:
        words = f.read()
    return words

def choose_topic(): #ask user to choose one of three topics
    topicname = input('Выберите одну из трех тем (птицы, животные, специи): ')
    if topicname == 'птицы':
        topicname = '1.txt'
    elif topicname == 'животные':
        topicname = '2.txt'
    else:
        topicname = '3.txt'
    return topicname

def getrandword(words): #get random word for game
    words = words.split('\n')
    randword = random.choice(words)
    return randword

def guess_letter(randword):
    i = len(randword)
    guessword = ('_' * i)
    return guessword


def main():
    topicname = choose_topic()
    words = open_file(topicname)
    randword = getrandword(words)
    guessword = guess_letter(randword)
    try_counter = 5
    print('У вас есть 5 попыток, чтобы отгадать слово.')
    print(guessword)
    while (try_counter >= 1) and (guessword != randword):
        guesslet = input('Введите букву: ')
        if guesslet in randword:
            for i in range(len(randword)):
                if guesslet == randword[i]:
                    guessword = guessword[:i] + guesslet + guessword[i + 1:]
            print(guessword)
        else:
            try_counter -= 1
            print('Такой буквы нет. Осталось попыток: ', try_counter)
    if guessword != randword:
        print('Не удалось угадать слово :(')
    else:
        print('Ура! Слово угадано!')

if __name__ == '__main__':
    main()
