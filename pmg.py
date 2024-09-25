from cryptography.fernet import Fernet
import pandas as pd
import numpy as np


def load_key():
    file=open('key.key',"rb")
    return file.read()


key=load_key()
fer=Fernet(key)

def add():
    user=input("Enter your Account name:")
    password=input("Enter Your password")
    with open("password.txt",'a') as f:
        f.write(user+"->"+fer.encrypt(password.encode()).decode()+"\n")
    print("Successfully added!")

def view():
    try:
        with open("password.txt",'r') as f:
            print("format is in user:password mode")
            print({i.rsplit()[0].split('->')[0]:fer.decrypt(i.rsplit()[0].split('->')[1]).decode() for i in f.readlines()})
    except Exception as e:
        print(f"An error occurred: {e}")
while True:
    manage=input("Do you wanna manage your passwords (Y/N)")


    if manage.upper()=='Y':
        action=input("Do you wanna add or view password (ADD/VIEW)")

        if action.upper()=='ADD':
            add()
            pass
        if action.upper()=='VIEW':
            view()
            pass
    else:
        quit()
