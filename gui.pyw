from main import *
import PySimpleGUI as sg
from PIL import Image

#Setting up window
sg.theme('Light Brown 2')
layout = [[sg.Text("")],
          [sg.Output(size=(50, 30), key='-OUTPUT-')],
          [sg.Button('>', font='Georgia 10')]]

window = sg.Window('Lord of The Rings', layout, element_justification='r')
chapter = 0


#Event Loop
while True:
    event, values = window.read()
    if event == '>':
        #Cover
        if chapter == 0:
            window['-OUTPUT-'].update('')
            print()
            print()
            print()
            print('\t\tThe Lord of The Rings')
            print()
            print()
            print()
            print("\t❉⊱•═•⊰❉⊱•═•⊰❉⊱•═•⊰❉⊱•═•⊰❉⊱•═•⊰❉")
            print()
            print("""\t⠀⠀⠀⠀⠀⠀⢀⣀⣀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            \t⢰⡄⠀⠀⣠⣾⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            \t⢸⡇⠐⠾⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            \t⠀⡇⠀⢠⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            \t⠐⣿⣾⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
            \t⠀⢹⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⣄⠀⢻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
            \t⠀⢸⠈⠉⣿⣿⣿⣿⣿⣿⡄⠀⢸⣤⣼⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀
            \t⠀⠸⡆⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⢏⠙⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀
            \t⠀⠀⠇⢀⣿⣿⣿⣿⣿⣿⣿⣧⡀⠸⡀⣿⣿⣿⢆⠀⠀⠀⠀⠀⠀
            \t⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⢣⠻⣟⠉⢻⣆⠀⠀⠀⠀⠀
            \t⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣷⣿⣶⣾⣷⣶⣦⡀⠀⠀
            \t⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡄""")
            #I did not make this I found it on Google
            print()
            print()
            print("\t❉⊱•═•⊰❉⊱•═•⊰❉⊱•═•⊰❉⊱•═•⊰❉⊱•═•⊰❉")
            print()
            print()
            print()
            print()
            print('\t\t      J.A.A. Davis')
            chapter += 1
        #General page
        else:
            window['-OUTPUT-'].update('')
            print()
            print()
            print()
            print(f'\t\t        Chapter {chapter}')
            print()
            print()
            print('\t', generate_text(1400, 0.6))
            chapter += 1

    #Close
    if event in (sg.WIN_CLOSED, 'EXIT'):
        break
window.close()
