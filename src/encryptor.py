from cryptography.fernet import Fernet

def keygen():
    key = Fernet.generate_key()
    with open("totem.key","wb") as totem:
        totem.write(key)

def getkey():
    try:
        keyfile = open("totem.key","rb").read()
        return keyfile    
    except:
        return None

def encrypt_file(file, key):
    try:
        fern = Fernet(key)
        with open(file,"rb") as target_r:
            target_data = target_r.read()
        data_encrypt = fern.encrypt(target_data)
        with open(file, "wb") as target_w:
            target_w.write(data_encrypt)
    except:
        print("[X] -> ERROR ENCRIPTED FILE")