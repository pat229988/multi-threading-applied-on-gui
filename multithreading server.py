import PySimpleGUI as sg
sg.theme('DarkAmber')
import threading
from _thread import *
import socket
ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
layout = [
    [sg.Text("A sample UI for servers sending and receiving messages.",size=(80, 2),font=(20)),],
    [sg.Button('REFRESH',size=(80, 2),enable_events=True, key="-RF-",font=(40)),],
    [sg.Text('messages form Client side : ',size=(40, 2),font=(20),enable_events=True, key="-RSV-",)],
    [sg.Multiline(size=(80, 20),key="-TB-",font=(20),enable_events=True)]
]

def main():
    window = sg.Window("This is server", layout,enable_close_attempted_event=True,finalize=True)
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    ServerSocket.listen()
    def s_changes():
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        data = Client.recv(2048)
        dt = str(values["-TB-"]) + "\n" + data.decode('utf-8')
        window.Element('-TB-').update(value = dt)
        print(data.decode('utf-8'))
        Client.close()
        

    while True:
        event, values = window.read()
        thread = threading.Thread(target=s_changes)
        thread.daemon = True
        thread.start()
        if event == '-RF-':
            print('refresh')
        elif (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
            break
    ServerSocket.close()
    window.close()

if __name__=="__main__":
    main()