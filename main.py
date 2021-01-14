import os
import socket
import datetime
import shutil
import random
import pyautogui
from colorama import Fore, Back
import json
import sys
import gpiozero
import subprocess
import cv2

date = datetime.datetime.now()
print('\n' + 'STOSSE HOME SYSTEM' + '\n' + f'Real Time: {date}' + '\n')
with open('config.json') as file:
    config = json.load(file)
with open('user_data.json') as psd_file:
    user_data = json.load(psd_file)



def Security_Cam():
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret, frame = cam.read()
        if cv2.waitKey(10) == ord('c'):
            Terminal()
        cv2.imshow('Stosse cam', frame)

def Data(command, data_code, current_location):
    def Read_data(data_code):
        print('')
    def Add_data(current_location):
        file_code_file = open('permission_level.txt', 'w+')
        img_path = r'C:\Users\Julian\Documents\Stosse.system\data\img'
        txt_path = f''
        file_code = random.randint(0, 10000)
        file_code_file.write(f'{file_code} | {current_location}' + '\n')
        print(current_location)
        #shutil.copyfile(src=str(current_location), dst=img_path)
        shutil.move(current_location, img_path)

    if command == 'Read-data':
        Read_data(data_code=data_code)
    if command == 'Add-data':
        Add_data(current_location=current_location)

def Terminal():
    def Network(command):
        if command == 'net.show.user':
            print('\n' + f'Name: {socket.gethostname()} | IPv4: {socket.gethostbyname(socket.gethostname())}' + '\n')
        if 'net.ping' in command:
            ip_to_ping = command.replace('net.ping(', '')
            ip_to_ping = ip_to_ping.replace(')', '')
            os.system(f'ping {ip_to_ping}')
        if 'net.stat' == command:
            os.system('netstat')
    def Data_control(command):
        if 'data.add' in command:
            #current_location = ''.format(command.replace('data.add(', ')', ''))
            current_location = command.replace('data.add(', '')
            current_location = current_location.replace(')', '')
            Data(command='Add-data', data_code=False, current_location=current_location)
        if 'data.read' in command:
            data_code = ' '.format(command.replace('data.read~',''))
            Data(command='Read-data', data_code=data_code, current_location=False)
    def Profiles(command):
        if command == 'profile.show.username':
            print(os.getlogin())
    def System(command):
        if 'system.show.version' == command:
            print(config['System']['Version'])
        if 'system.shutdown' == command:
            date = datetime.datetime.now()
            backup = open(rf'C:\Users\Julian\Documents\Stosse.system\Backup\Backup{date}.txt', 'w+')
            backup.write(f'STOSSE HOME SYSTEM BACKUP | from {date}' + '\n')
            backup.write(f'Network: Name: {socket.gethostname()} | IPv4: {socket.gethostbyname(socket.gethostname())}' + '\n')
            backup.write(f'Profiles: User name: {os.getlogin()}' + '\n')
            backup.write(f'System: ' + '\n')
            sys.exit()
        if 'system.change.user' == command:
            Login()
        if 'system.show.user' == command:
            print()
            print('USER_NAME: ' + user_data[user_name]['user_name'])
            print('PASSWORD: ' + user_data[user_name]['password'])
            print('PIN: ' + user_data[user_name]['pin'])
            print('ADMIN: ' + user_data[user_name]['admin'])
            print()
        if 'system.run.remotecontrol' == command:
            Remotecontrol()
        if 'system.show.cam' == command:
            Security_Cam()
    def Gpio_control(command):
        if 'gpio.show.pinout' == command:
            gpio = ['3,3 V  [1]', ' | ', '[2]  5 V'
                    'GPIO2  [3]', ' | ', '[4]  GND'
                    'GPIO4  [7]', ' | ', '[8]  GPIO14'
                    'GND    [9]', ' | ', '[10] GPIO15'
                    'GPIO17 [11]',' | ', '[12] GPIO18'
                    'GPIO27 [13]',' | ', '[14] GND'
                    'GPIO22 [15]',' | ', '[16] GPIO23'
                    '3,3 V  [17]',' | ', '[18] GPIO24'
                    'GPIO10 [19]',' | ', '[20] GND'
                    'GPIO9  [21]',' | ', '[22] GPIO25'
                    'GPIO11 [23]',' | ', '[24] GPIO8'
                    'GND    [25]',' | ', '[26] GPIO7']
            print('3,3 V  [1] '+' | '+ '[2]  5 V')
            print('GPIO2  [3] '+' | '+ '[4]  GND')
            print('GPIO4  [7] '+' | '+ '[8]  GPIO14')
            print('GND    [9] '+' | '+ '[10] GPIO15')
            print('GPIO17 [11]'+' | '+ '[12] GPIO18')
            print('GPIO27 [13]'+' | '+ '[14] GND')
            print('GPIO22 [15]'+' | '+ '[16] GPIO23')
            print('3,3 V  [17]'+' | '+ '[18] GPIO24')
            print('GPIO10 [19]'+' | '+ '[20] GND')
            print('GPIO9  [21]'+' | '+ '[22] GPIO25')
            print('GPIO11 [23]'+' | '+ '[24] GPIO8')
            print('GND    [25]'+' | '+ '[26] GPIO7')
    while True:
        date = datetime.datetime.now()
        os.chdir(path='C:\\')

        command = input('STOSSE@SYSTEM> ')
        if 'net.' in command:
            Network(command=command)
        if 'data.' in command:
            Data_control(command=command)
        if 'profile' in command:
            Profiles(command=command)
        if 'system' in command:
            System(command=command)
        if 'gpio' in command:
            Gpio_control(command=command)

        if command == 'cls':
            os.system('cls')

def Login():
    if user_name == user_data[user_name]['user_name']:
        if password == user_data[user_name]['password']:
            if pin == user_data[user_name]['pin']:
                Terminal()
    else:
        sys.exit()

user_name = input('USER_NAME: ')
password = input('PASSWORD: ')
pin = input('PIN: ')

Login()