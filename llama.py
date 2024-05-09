import os
from groq import Groq
import sys 
import time 
from colorama import Fore 
import json 
import socket 



with open('api.json') as f:
    api=json.load(f)
api_key = api['apikey']
client = Groq(api_key=api_key)


art = """
 ██████╗██╗     ██╗    ███╗   ███╗ ██████╗ ██████╗ ███████╗██╗     ███████╗    
██╔════╝██║     ██║    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██║     ██╔════╝    
██║      ██║     ██║    ██╔████╔██║██║   ██║██║  ██║█████╗  ██║     ███████╗    
██║      ██║     ██║    ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  ██║     ╚════██║    
╚██████╗███████╗██║    ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗███████╗███████║    
 ╚═════╝╚══════╝╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝                                                                                   
"""
def chat_loop():
    models = {
        1: 'mixtral-8x7b-32768',
        2: 'llama3-70b-8192',
        3: 'llama3-8b-8192',
        4: 'gemma-7b-it'
    }
    print(Fore.GREEN,'Currently supported these models:')
    print(Fore.BLUE,', '.join(f'{k}: {v}' for k, v in models.items()))
    try:
        aino=int(input('Please enter the model no:'))
        ai = models[aino]
    except Exception:
        print(Fore.RED,'Default model is being loaded due to input [not in options]')
        ai='llama3-8b-8192'
    print(f"loading {ai} model, Please wait")
    loading_bar()
    while True:
        try:
            print(Fore.BLUE,'for closing type exit or quit')
            user_input = input("~$> ")
            if user_input.lower().lstrip().rstrip()  in ['bye','quit','exit']:
                print(Fore.RED,"Flushing model")
                Fore.WHITE
                loading_bar()
                break
            if user_input.lstrip().rstrip()== '':
                continue
            elif user_input.lower().lstrip().rstrip().startswith('/change'):
                chat_loop() 
            elif user_input in ['clear','cls']:
                if os.name() == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
            else:
                try:
                    output = send_message(user_input,ai)
                    print(Fore.WHITE,f"{ai}:", output)
                except:
                    print('Error  occurred')
        except KeyboardInterrupt:
            print('BYE!')
            break
def send_message(message,ai):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model= ai,
    )
    return chat_completion.choices[0].message.content


def chkint():
    try:
        socket.create_connection(('www.googe.com',80))
        return True
    except socket.gaierror:
        return False
        

def loading_bar():
    try:
        print("\rLoading...", end="\r")
        for i in range(5):
            sys.stdout.write("\rLoading")  
            sys.stdout.write("." * (i + 1))  
            sys.stdout.flush()
            time.sleep(0.5)
        print(" ")
    except KeyboardInterrupt:
        print('Exiting the program')


loading_bar()
if chkint():
    print(art)
    chat_loop()
else:
    print('Please connect yourself to internet')
    print('exiting after 10s, for you to connect to internet before that!')
    for i in range(0,10):
        time.sleep(1)
        if chkint():
            print(art)
            chat_loop()
            break
        else:
            if chkint() != False:
                print('exiting now :-(')
                
            continue
        
    
