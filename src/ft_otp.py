import argparse
from encode import *
from cryptor import *

# Main
def main():
    args = config_args()
    # [-k] Generate a new Totp pin autentication **
    if args.key_gen != None:
        hash_ = get_totp(args.key_gen)
        if hash_ != None:
            print(hash_)
    # [-g] Change key for totp and save on file 'ft_otp.key'
    if args.new_key != None:
        try:
            with open(args.new_key, "rb") as hex_file:
                new_key = hex_file.read()
            password = input("Enter the encryption key of the ft_otp file: \n")
            if change_totp_key(password, new_key):
                print("SUCCESSFULL CHANGE OF KEY OF THE FILE 'ft_otp.key'.")
        except:
            print("ERROR OPEN FILE KEY.HEX -> Try with another file 'key.hex' [-rk].")

    # Bonus options
    ## Change password for encrypt file 'ft_otp.key'
    if args.new_pass != None:
        old_pass = input("Enter the encryption key of the ft_otp file: \n")
        if change_encrypt_pass(old_pass,args.new_pass):
            print("SUCCESSFULL CHANGE OF ENCRYPTION KEY OF THE 'ft_otp.key'.")
    ## Random key.hex for ft_otp.key
    if args.random_key == True:
        random_totp_key = get_random_key()
        with open("key.hex","wb") as hex:
            hex.write(random_totp_key)
        print("RANDOM HEX KEY SUCCESSFULY GENERATED!!")
        print(random_totp_key.decode())
        print("The key has been stored in the file 'key.hex'.")
    ## Random pass for encrypt ft_otp.key
    if args.random_pass == True:
        print(get_random_pass())

def config_args():
    parser = argparse.ArgumentParser(
        description="""*** Ft_otp *** This is a double factor of autentication tool based 
        in algorithm TOTP (Time One-Time Password)"""
    )
    # Generate a new key/pin
    parser.add_argument("-k","--key-gen", default=None, help="[-k + 'ft_otp.key'] Generate a new totp autentication code.")
    # Save a new ft_otp.key
    parser.add_argument("-g","--new-key",default=None,help="[-g + 'key.hex'] Set a new key for for 'ft_otp.key'")
    
    # Bonus options   
    parser.add_argument("-p","--new-pass", default=None, help="[-p + 'new_pass_base64'] Set a new password Base64 for encrypt 'ft_otp.key'.")
    parser.add_argument("-rk","--random-key", default=False, action='store_true', help="Generate a random key autentication in file 'key.hex'.") 
    parser.add_argument("-rp","--random-pass", default=False, action='store_true', help="Generate a random password Base64 for encrypt 'ft_otp.key'.")
    
    return parser.parse_args()

if __name__ == "__main__":
    main()
