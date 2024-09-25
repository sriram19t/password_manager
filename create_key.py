from cryptography.fernet import Fernet

def write_key():
    Key=Fernet.generate_key()
    with open("key.key","wb") as file:
        file.write(Key)
write_key()
