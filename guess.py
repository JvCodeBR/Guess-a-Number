import random

def guess(max_range):
    random_number = random.randint(1, max_range)
    user_guess = int(0)
    while user_guess != random_number:
        user_guess = int(input(f'Chute um número entre 1 e {max_range}: '))
        if user_guess < random_number:
            print(f'O número aleatório é maior que {user_guess}')
        elif user_guess > random_number:
            print(f'O número aleatório é menor que {user_guess}')
    
    print(f'Parabéns, você adivinhou o número {random_number}')

range = int(input('Insira o valor máximo do range: '))
guess(range)


    