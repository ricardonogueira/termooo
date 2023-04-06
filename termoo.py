# API para verificação de palavra
# https://www.academia.org.br/ajax/abl/buscar-palavras?form=vocabulario&palavra=blah

from termcolor import colored
import requests

def verificar_palavra(a_palavra):
    resp = requests.get('https://www.academia.org.br/ajax/abl/buscar-palavras', {'form':'vocabulario', 'palavra': a_palavra})
    if len(resp.json().get('rows')) == 0:
        return False
    return True
    

palavra = 'agudo'
tentativas = 0

while tentativas < 5:
    print('_ ' * 5)
    digitado = input('Digite uma palavra: ')

    if len(digitado) == 5 and verificar_palavra(digitado):
        for pos, valor in enumerate(digitado):
            
            #mudar a logica
            if palavra[pos] == digitado[pos]:
                print(colored(digitado[pos], 'green'), end=" ")
            elif digitado[pos] in palavra:
                print(colored(digitado[pos], 'yellow'), end=" ")
            else:
                print(colored(digitado[pos], 'white'), end=" ")
        print('\n')
        
        if digitado == palavra:
            print('ACERTOU!!\n')
            break
    else:
        print('Digite novamente ...')