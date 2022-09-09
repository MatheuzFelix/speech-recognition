import PySimpleGUI as sg

from recognizer import listen_mic, read_file

sg.theme('Reddit')
layout = [
    [sg.Text(('Selecione a opção desejada'), size=(22, 1), justification='center')],
    [sg.Checkbox('Traduzir por voz', key='audio'),
        sg.Checkbox('Traduzir por texto', key='text'),
    ],
    [sg.Button('enviar', size=(8, 0))]
]
window = sg.Window('Recognizer', layout, finalize=True)
#window['id'].bind('<Return>', '_Enter')

while True:
    event, value = window.read()
    if event == 'enviar' or event == '_Enter':
        print(event)
        if value['audio'] == True:
            listen_mic()
        elif value['text'] == True:
            read_file()
    break


