import PySimpleGUI as sg
import json

details = {}
sg.theme('DarkAmber') 


def make_window1():
    layout = [[sg.Text('Name'), ],
              [sg.Input(k='name', enable_events=True)],
              [sg.Text('Amizone ID'), ],
              [sg.Input(k='id', enable_events=True)],
              [sg.Text('Password'), ],
              [sg.Input(k='password', enable_events=True)],
              [sg.Text(size=(20,1),  k='-OUTPUT-')],
              [sg.Button('Next ❯'), sg.Button('Exit')]]

    return sg.Window('Enter Details', layout, finalize=True)


def make_window2():
    layout = [[sg.Text('Select the path where your MSTeams is installed.')],
            [sg.Combo(sg.user_settings_get_entry('-filenames-', []), default_value=sg.user_settings_get_entry('-last filename-', ''), size=(50, 1), key='path'),
            sg.FileBrowse()],
            [sg.Button('❮ Prev'), sg.Button('Next ❯')],
            [sg.Text('⚠️ Be sure to add correct path otherwise the program may not work as intented')]]


    return sg.Window('Select Path', layout, finalize=True)


def make_window3():
    instructions = '''
    Thank you {}, for using Automated Schedule for Students(ASS)
    Here are few things that you should know before getting started.
    1. The application will create two files after registration.
        1.a. setting.json: this file will contain all the settings
             for this application.
        1.b. data.json: This contains all the info fetched by the
             application for Amizone.
    2. This application will help you in attending you online classes
       on time and automate boring task like checking for Time Table and 
       attendance etc..
    3. If you like this application please give it a ⭐ on github.com/iamHrithikRaj.
    '''.format(details["name"])

    layout = [[sg.Text(instructions)],
              [sg.Text(size=(50,1), key='-OUTPUT-')],
              [sg.Button('Got it')]]
    return sg.Window('Instructions', layout, finalize=True)



window1, window2, window3 = make_window1(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == window1 and event in (sg.WIN_CLOSED, 'Exit'):
        break

    if window == window1:
        if event == 'Next ❯':
            details.setdefault('name',values['name'])
            details.setdefault('id',values['id'])
            details.setdefault('password',values['password'])
            window1.hide()
            window2 = make_window2()
        elif event in (sg.WIN_CLOSED, 'Exit'):
            break

    if window == window2:
        details.setdefault('path',values['path'])
        if event == 'Next ❯':
            window2.hide()
            window3 = make_window3()
        elif event == '❮ Prev':
            window2.close()
            window1.un_hide()
        elif event is sg.WIN_CLOSED:
            break

    if window == window3 and event in (sg.WIN_CLOSED, 'Got it'):
            break

window.close()

filename = "settings.json"
with open(filename, 'w') as file:
    json.dump(details,file)