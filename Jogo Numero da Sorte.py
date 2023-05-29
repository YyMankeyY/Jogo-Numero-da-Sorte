import PySimpleGUI as sg
import random

def criar_janela():
    sg.theme('DarkBlue4')
    layout = [
        [sg.Text('Digite um número entre 0 e 10:'), sg.Input(key='entrada')],
        [sg.Button('Tentar'), sg.Button('Desistir')],
        [sg.Text('', key='resultado')],
        [sg.Text('Tentativas restantes: 5', key='tentativas')],
        [sg.Text('', key='pontuacao')]
    ]
    return sg.Window('Acerte o número!', layout, finalize=True)

def reiniciar_jogo():
    window['tentativas'].update('Tentativas restantes: 5')
    window['entrada'].update('')
    window['resultado'].update('')
    window['pontuacao'].update('')

jogando = True
tentativas_restantes = 5
pontuacao = 0
numero_aleatorio = random.randint(0, 10)

window = criar_janela()

while jogando:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == 'Tentar':
        
        entrada_str = values['entrada']
        if not entrada_str.isnumeric():
            window['resultado'].update('Digite um número válido!')
            continue
        entrada = int(entrada_str)
        if entrada < 0 or entrada > 10:
            window['resultado'].update('O número deve estar entre 0 e 10!')
            continue

        
        tentativas_restantes -= 1
        window['tentativas'].update('Tentativas restantes: {}'.format(tentativas_restantes))

        
        if entrada == numero_aleatorio:
            pontuacao = 100 - (5 - tentativas_restantes) * 20
            window['resultado'].update('Parabéns, você acertou o número!')
            window['pontuacao'].update('Sua pontuação foi: {}'.format(pontuacao))
            jogando = False
        else:
            if tentativas_restantes == 0:
                window['resultado'].update('Suas tentativas acabaram! O número era: {}'.format(numero_aleatorio))
                jogando = False
            elif entrada < numero_aleatorio:
                window['resultado'].update('O número é maior que {}'.format(entrada))
            else:
                window['resultado'].update('O número é menor que {}'.format(entrada))

    elif event == 'Desistir':
        jogando = False
        
if not jogando:
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Tentar':
            reiniciar_jogo()
            jogando = True
            tentativas_restantes = 5
            pontuacao = 0
            numero_aleatorio = random.randint(0, 10)
            break
        elif event == 'Desistir':
            break

window.close()