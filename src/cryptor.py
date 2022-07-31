from re import A
from cryptography.fernet import Fernet
import secrets

# Get random key totp
def get_random_key():
    return secrets.token_hex(32).encode('utf-8')

# Get random master password
def get_random_pass():
    return Fernet.generate_key().decode('utf-8')

# Set ft_otp.key master encrypt password
def set_master_pass(old, new):
    decrypt = decrypt_file("ft_otp.key", old.encode('utf-8'))
    if decrypt:
        try:
            with open("ft_master.key","wb") as w_master:
                w_master.write(new.encode('utf-8'))
            status = encrypt_file("ft_otp.key",new.encode('utf-8'))
            return status
        except:
            print("ERROR KEY -> The key must be 32 characters")
            return False
    else:
        print("FATAL ERROR DECRYPTION!!")
        return False

# Get key from 'ft_otp.key' 
def get_key(file,passwd):
    try:
        fern = Fernet(passwd.encode('utf-8'))
        with open(file,"rb") as r_otp:
            encrypt_data = r_otp.read()
        decrypt_data = fern.decrypt(encrypt_data)
        return decrypt_data
    except FileNotFoundError:
        print("ERROR FILE.KEY -> Try with another file.")
    except ValueError:
        print("ERROR PASSWORD FILE.KEY -> Try with another password.")

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