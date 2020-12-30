#Packages
import os
import glob
import time
import socket

Banner_Text = """
        ██████╗  ██████╗  ██████╗ ████████╗██╗  ██╗██╗████████╗
        ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝██║ ██╔╝██║╚══██╔══╝
        ██████╔╝██║   ██║██║   ██║   ██║   █████╔╝ ██║   ██║   
        ██╔══██╗██║   ██║██║   ██║   ██║   ██╔═██╗ ██║   ██║   
        ██║  ██║╚██████╔╝╚██████╔╝   ██║   ██║  ██╗██║   ██║   
        ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝   ╚═╝ 
        """
print(Banner_Text)
#Variables
SignedUp = False
LoggedIn = False
#Sign Up/Log In Function
def AccountCreation():
  print('(-)To use RootKit please sign up!')
  #Username input
  UsernameInput = input('(-)Username: ')
  print('Succesfully added username!')
  #Password input
  PasswordInput = input('(-)Password: ')
  print('Succesfully added password!')
  time.sleep(2)
  SignedUp = True
  #Log In Function
  os.system('clear')
  print(Banner_Text)
  print('(-)Log in to start using RootKit!')
  LogUsernameInput = input('(-)Username: ')
  if LogUsernameInput == UsernameInput:
    print('Succesfully added username!')
    LogPasswordInput = input('(-)Password: ')
    if LogPasswordInput == PasswordInput:
      print('Succesfully added password!')
      print('Welcome ',UsernameInput)
      LoggedIn = True
      time.sleep(2)
      os.system('clear')
      print(Banner_Text)
#File Locator Function
def FileLocator():
  dir_scripts = glob.glob('*.py') +  glob.glob('*.pyw') +  glob.glob('*.exe') +  glob.glob('*.doc') +  glob.glob('*.docx')
  print('(-)Files Located: ',dir_scripts)
#Encryption/Decryption Function
def EncryptDecrypt():
  #Variables
  Running = True
  result = ''
  choice = ''
  message = ''

  while Running:
    choice = input("\n(-)Encrypt\n(-)Decrypt\nCommand:  ")
    #Encryption
    if choice == '1':
        message = input('\nEnter message for encryption: ')
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - 2)

        print(result + '\n\n')
        result = ''
    #Decryption
    if choice == '2':
        message = input('\nEnter message to decrypt: ')
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + 2)

        print(result + '\n\n')
        result = ''
    elif choice != '0':
        print('You have entered an invalid input, please try again. \n\n')
#Host To Ip
def HostToIp():
  HostInput = str(input('Enter a host: '))
  Host = socket.gethostname()
  IpAddr = socket.gethostbyname(HostInput)
  print('Host:',Host,'\n','Ip:',IpAddr)
  svInput = str(input('Do you want to save the data? '))
  if svInput == "Yes":
    data = open('Data.txt', 'w')
    data.write(IpAddr)
    data.close
#RootKit Main
AccountCreation()
#Options
OptionInput = input('(-)File Locator\n(-)Command Prompt\n(-)Encryption/Decryption\n(-)Exit\nCommand: ')
#File Locator
if OptionInput == "1":
  FileLocator()
#Command Prompt
if OptionInput == "2":
  while True:
    CommandInput = input('rootkit@ubuntu:~$ ')
    os.system(CommandInput)
#Encryption/Decryption
if OptionInput == "3":
  os.system('clear')
  print(Banner_Text)
  EncryptDecrypt()
#Host to Ip
if OptionInput =="4":
  HostToIp()
#Exit 
if OptionInput == "5":
  os.system('clear')
  print(Banner_Text)
  print('(-)Connection Lost . . .')
  #015793eab130
