import PySimpleGUI as sg
import socket

sg.theme('DarkAmber')
layout_c = [
    [
        sg.Text("A sample UI for Client sending and receiving messages.",size=(80, 2),font=(20)),
    ],
    [
        sg.Button('SEND',size=(80, 2),enable_events=True, key="-SNDC-",font=(40)),
    ],
    [
        sg.Text('Enter message for Server : ',size=(40, 2),font=(20)), 
        sg.InputText(size=(40, 2),enable_events=True, key="-MSGC-",font=(20))
    ]
]

def main():
    window = sg.Window("This is client", layout_c,enable_close_attempted_event=True,finalize=True)
    def send_msg():
        ClientSocket = socket.socket()
        host = '127.0.0.1'
        port = 1233
        try:
            ClientSocket.connect((host, port))
            print('tried connecting')
        except socket.error as e:
            print(str(e))
        msg = str(values["-MSGC-"])
        ClientSocket.send(str.encode(msg))
        print('done from client')
        ClientSocket.close()
        
    while True:
        event, values = window.read()
        if event == "-SNDC-" :
            send_msg()
        elif (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
            break
    
    window.close()

if __name__=="__main__":
    main()