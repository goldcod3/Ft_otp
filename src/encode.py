import hmac
from datetime import datetime
from time import time
from cryptor import *

# Default Variables
format_date = '%Y-%m-%d -> %H:%M:%S'
default_time_count = 30
default_digest = 'SHA1'
default_len = 6
default_file = "ft_otp.key"

# Get time counter
def get_time_key(time_count):
    time_ = datetime.utcfromtimestamp(time())
    timestr_ = datetime.strftime(time_, format_date)
    return str(int(time() / time_count)), timestr_

# Get HOTP Hash
def get_hotp(file, passwd):
    time_, time_msg = get_time_key(default_time_count)
    key = get_key(file,passwd)
    if key != None:
        print(time_msg)
        hash_ = hmac.new(key, time_.encode('utf-8'), default_digest)
        return hash_.hexdigest()
    else:
        return None

# Get TOTP Pin
def get_totp(file):
    passwd = input("Enter the encryption key of the ft_otp file: \n")
    hotp_ = get_hotp(file, passwd)
    if hotp_ != None:
        decimal = str(int(hotp_, 16))
        rev_decimal = decimal[::-1]
        return rev_decimal[:6]
    else:
        return None

# Change 'ft_otp.key' Base64 master encrypt password
def change_encrypt_pass(old_pass, new_pass):
    try:
        decrypt = decrypt_file(default_file, old_pass.encode('utf-8'))
        if decrypt:
            encrypt = encrypt_file(default_file,new_pass.encode('utf-8'))
            if encrypt:
                with open("ft_master.key","wb") as w_master:
                    w_master.write(new_pass.encode('utf-8'))
            else:
                encrypt_file(default_file,old_pass.encode('utf-8'))
                print("ERROR NEW KEY -> The key must be 32 characters Base64.")
            return encrypt
        else:
            print("ERROR IN OLD KEY TO DECRYPT -> Try again.")
            return False
    except FileNotFoundError:
        verify_file(default_file)

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
    try:
        if check_hex_key(new_key):
            if decrypt_file(default_file, password.encode('utf-8')):
                with open(default_file, "wb") as w_key:
                    w_key.write(new_key)
                if encrypt_file(default_file, password.encode('utf-8')):
                    return True
            else:
                print("ERROR IN KEY TO DECRYPT -> Try again.")
        else:
            print("ERROR NEW KEY HEX -> Try another key.")
        return False
    except FileNotFoundError:
        verify_file(default_file)
