from cryptography.fernet import Fernet
import secrets
from os.path import exists
from getpass import getpass

# Default Variables
default_file = "ft_otp.key"

# Encrypt file 
def encrypt_file(file, key):
    try:
        fern = Fernet(key)
        with open(file,"rb") as target_r:
            target_data = target_r.read()
        data_encrypt = fern.encrypt(target_data)
        with open(file, "wb") as target_w:
            target_w.write(data_encrypt)
        return True
    except Exception as a:
        return False

# Decrypt file
def decrypt_file(file, key):
    try:
        fern = Fernet(key)
        with open(file,"rb") as target_r: 
            encrypted_data = target_r.read()
        decrypt_data = fern.decrypt(encrypted_data)
        with open(file,"wb") as target_w:
            target_w.write(decrypt_data)
        return True
    except Exception:
        return False

# Get key from 'ft_otp.key' 
def get_key(file,passwd):
    try:
        fern = Fernet(passwd.encode('utf-8'))
        with open(file,"rb") as r_otp:
            encrypt_data = r_otp.read()
        decrypt_data = fern.decrypt(encrypt_data)
        return decrypt_data
    except Exception:
        print("ERROR PASSWORD FILE.KEY -> Try with another password.")
    return None

# Verify string if hex of 64 characters
def check_hex_key(key):
    try:
        if len(key) >= 64:
            int(key, 16)
            return True
        else:
            return False
    except Exception:
        return False

# Change 'ft_otp.key' hex key
def change_totp_key(password, new_key):
    if check_hex_key(new_key):
        if decrypt_file(default_file, password.encode('utf-8')):
            with open(default_file, "wb") as w_key:
                w_key.write(new_key)
            if encrypt_file(default_file, password.encode('utf-8')):
                return True
        else:
            print("ERROR IN KEY TO DECRYPT OR IN FILE.KEY -> Try again.")
    else:
        print("ERROR NEW KEY HEX -> Try another key.")
    return False

# Change 'ft_otp.key' Base64 master encrypt password
def change_encrypt_pass(old_pass, new_pass):
    if decrypt_file(default_file, old_pass.encode('utf-8')):
        if encrypt_file(default_file,new_pass.encode('utf-8')):
            with open("ft_master.key","wb") as w_master:
                w_master.write(new_pass.encode('utf-8'))
            return True
        else:
            encrypt_file(default_file,old_pass.encode('utf-8'))
            print("ERROR NEW KEY -> The key must be 32 characters Base64.")
    else:
        print("ERROR IN OLD KEY TO DECRYPT -> Try again.")
    return False

# Verify file 'ft_otp.key'
def verify_file(file):
    if file == default_file:
        if exists(default_file) == False:
            print("ERROR NOT FOUND FILE.KEY!")
            new_key = get_random_key()
            passwd = getpass("Enter the new encryption key of the ft_otp file [Base64]: \n")
            with open(default_file,"wb") as w_file:
                w_file.write(new_key)
            if encrypt_file(default_file, passwd):
                print("File 'Ft_otp.key successfull created.")
                print("A password has been saved in the file 'ft_master.key'")
            else:
                passwd = get_random_pass()
                encrypt_file(default_file, passwd)
                print("File 'Ft_otp.key successfull created.")
                print("ERROR PASSWORD -> A new random key has been generated in the file 'ft_master.key'")
            with open("ft_master.key","wb") as w_master:
                w_master.write(passwd.encode('utf-8'))
        return True
    else:
        print("ERROR FILE.KEY -> Try with 'ft_otp.key'.")
        return False

# Get random key totp
def get_random_key():
    return secrets.token_hex(32).encode('utf-8')

# Get random master password
def get_random_pass():
    return Fernet.generate_key().decode('utf-8')