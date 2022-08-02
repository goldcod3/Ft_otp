from cryptography.fernet import Fernet
import secrets

# Get random key totp
def get_random_key():
    return secrets.token_hex(32).encode('utf-8')

# Get random master password
def get_random_pass():
    return Fernet.generate_key().decode('utf-8')

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

# Verify file 'ft_otp.key'
def verify_file(file):
    if file == "ft_otp.key":
        print("ERROR NOT FOUND FILE.KEY!")
        new_key = get_random_key()
        with open(file,"wb") as w_file:
            w_file.write(new_key)
        passwd = input("Enter the new encryption key of the ft_otp file [Base64]: \n")
        if encrypt_file(file, passwd):
            print("File 'Ft_otp.key created, retry command -k!'")
            with open("ft_master.key","wb") as w_master:
                w_master.write(passwd.encode('utf-8'))
            print("A password has been saved in the file 'ft_master.key'")
        else:
            passwd = get_random_pass()
            encrypt_file(file, passwd)
            print("File 'Ft_otp.key created, retry command -k!'")
            print("ERROR PASSWORD -> A new random key has been generated in the file 'ft_master.key'")
            return True
    else:
        print("ERROR FILE.KEY -> Try with ft_otp.key")
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
        verify_file(file)
    except Exception:
        print("ERROR PASSWORD FILE.KEY -> Try with another password.")
    return None
