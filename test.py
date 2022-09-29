import random
import json

file = open('question.json', 'r')
questions = json.load(file)
file.close()

file = open('feedback.json', 'r')
feedback = json.load(file)
file.close()

score = {}

while True:
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.randint(1, 10)
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    while x == y:
        y = random.randint(1, 10)
    while z == y or z == x:
        z = random.randint(1, 10)
    while a == y or a == x or a == z:
        a = random.randint(1, 10)
    while b == y or b == x or b == z or b == a:
        b = random.randint(1, 10)


    points = 0

    print(x, y, z, a, b)
    print('Bem vindo ao quiz de anime!')
    print('Qual seu nome?')
    name = input('Seu nome: ')
    print(f'Olá {name} o que deseja fazer?')
    escolha = input(' a) Jogar\n b) Recordes\n c) Sair\nSua resposta: ')
    if escolha == 'a':
        print('Entao vamos la!\n')
        order = questions[str(x)]
        for i in order:
            print(i)  # printa a pergunta e as alternativas
        answer = input('Sua Resposta: ')
        right = feedback[str(x)]  # determina a alternativa certa
        if answer == right:  # condicional caso a alternativa escolhida pelo usuario seja a correta
            print('\nCorreto!\n')
            points = points + 1
        else:
            print('\nIncorreto!\n')
        order = questions[str(y)]
        for i in order:
            print(i)
        answer = input('Sua Resposta: ')
        right = feedback[str(y)]
        if answer == right:
            print('\nCorreto!\n')
            points = points + 1
        else:
            print('\nIncorreto!\n')
        order = questions[str(z)]
        for i in order:
            print(i)
        answer = input('Sua Resposta: ')
        right = feedback[str(z)]
        if answer == right:
            print('\nCorreto!\n')
            points = points + 1
        else:
            print('\nIncorreto!\n')
        order = questions[str(a)]
        for i in order:
            print(i)
        answer = input('Sua Resposta: ')
        right = feedback[str(a)]
        if answer == right:
            print('\nCorreto!\n')
            points = points + 1
        else:
            print('\nIncorreto!\n')
        order = questions[str(b)]
        for i in order:
            print(i)
        answer = input('Sua Resposta: ')
        right = feedback[str(b)]
        if answer == right:
            print('\nCorreto!\n')
            points = points + 1
        else:
            print('\nIncorreto!\n')

        print(f'Parabéns {name}, sua pontuação foi {points}')

        file = open('record.json', 'r')
        json_loaded = json.load(file)
        print(json_loaded)
        file.close()
        json_loaded.update({name: points})
        file = open('record.json', 'w')
        new_file = json.dumps(json_loaded)
        print(new_file)
        file.write(new_file)
        file.close()


    elif escolha == 'c':
        print('Ok, até a próxima!')
        break

    elif escolha == 'b':
        file = open('record.json', 'r')
        json_loaded = json.load(file)
        x = json_loaded.enumerate()
        print(x)
        #for i in json_loaded:
            #print(i, i[json_loaded])

    else:
        continue