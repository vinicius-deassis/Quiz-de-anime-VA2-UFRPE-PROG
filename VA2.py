import random
import json
#ola git hub

file = open('question.json', 'r') #abre o arquivo que contem as perguntas
questions = json.load(file) #determina a variavel que sera usada para buscar as perguntas
file.close()

file = open('feedback.json', 'r') #abre o arquivo que contem o gabarito
feedback = json.load(file) #determina a variavel que sera usada para buscar as respostas corretas
file.close()

score = {} #utilizado para armazenar a pontuacao dos jogadores

while True:
# -----estrutura que gera 5 numeros aleatorios distintos------
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

    print('============================')
    print('Bem vindo ao quiz de anime! By Vini Jaeger')
    print('============================')
    print('O que deseja fazer?')
    escolha = input(' a) Jogar\n b) Recordes\n c) Sair\nSua resposta: ')
    print('============================')

    if escolha == 'a':
        print('Qual seu nome?')
        name = input('Seu nome: ')
        print(f'Então vamos lá {name}!\n')
        order = questions[str(x)]
        for i in order:
            print(i)  # printa a pergunta e as alternativas
        answer = input('Sua Resposta: ')
        right = feedback[str(x)]  # determina a alternativa certa
        if answer == right:  # condicional caso a alternativa escolhida pelo usuario seja a correta
            print('\nCorreto!')
            print('============================')
            points = points + 1
        else:
            print('\nIncorreto!')
            print('============================')
        order = questions[str(y)]
        for i in order:
            print(i)
        answer = input('Sua Resposta: ')
        right = feedback[str(y)]
        if answer == right:
            print('\nCorreto!')
            print('============================')
            points = points + 1
        else:
            print('\nIncorreto!')
            print('============================')
        order = questions[str(z)]
        for i in order:
            print(i)
        answer = input('Sua Resposta: ')
        right = feedback[str(z)]
        if answer == right:
            print('\nCorreto!')
            print('============================')
            points = points + 1
        else:
            print('\nIncorreto!')
            print('============================')
        order = questions[str(a)]
        for i in order:
            print(i)
        answer = input('Sua Resposta: ')
        right = feedback[str(a)]
        if answer == right:
            print('\nCorreto!')
            print('============================')
            points = points + 1
        else:
            print('\nIncorreto!')
            print('============================')
        order = questions[str(b)]
        for i in order:
            print(i)
        answer = input('Sua Resposta: ')
        right = feedback[str(b)]
        if answer == right:
            print('\nCorreto!')
            print('============================')
            points = points + 1
        else:
            print('\nIncorreto!')
            print('============================')

        print(f'Parabéns {name}, sua pontuação foi {points}, obrigado por jogar!')

        file = open('record.json', 'r')
        json_loaded = json.load(file)
        file.close()
        json_loaded.update({name: points})
        file = open('record.json', 'w')
        new_file = json.dumps(json_loaded)
        file.write(new_file)
        file.close()


    elif escolha == 'c':
        print('Ok, até a próxima!')
        print('============================')
        break

    elif escolha == 'b':
        file = open('record.json', 'r')
        json_loaded = json.load(file)
        for i in json_loaded:
            print(f'{i} fez {json_loaded.get(i)} pontos. ')


    else:
        continue