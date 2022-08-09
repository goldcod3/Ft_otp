import argparse
from getpass import getpass
from encode import *
from totp_gen import *

# Main
def main():
    args = config_args()
    # [-k] Generate a new Totp pin autentication **
    if args.key_gen != None and args.interactive == None:
        if verify_file(args.key_gen):
            passwd = getpass("Enter the encryption key for the ft_otp file: \n")
            if args.verbose:
                key_hex = get_key(args.key_gen, passwd)
                if key_hex != None:
                    verbose_totp(key_hex.decode('utf-8'))
            else:    
                get_totp_pin(args.key_gen, passwd)
    # [-g] Change key for totp and save on file 'ft_otp.key'
    if args.new_key != None:
        try:
            with open(args.new_key, "rb") as hex_file:
                new_key = hex_file.read()
            if verify_file('ft_otp.key'):
                password = getpass("Enter the encryption key for the ft_otp file: \n")
                if change_totp_key(password, new_key):
                    print("SUCCESSFULL CHANGE THE KEY OF THE FILE 'ft_otp.key'.")
        except:
            print("ERROR OPEN FILE KEY.HEX -> Try with another file 'key.hex' [-rk].")

    # Bonus options
    ## Change password for encrypt file 'ft_otp.key'
    if args.new_pass != None:
        if verify_file('ft_otp.key'):
            old_pass = getpass("Enter the encryption key for the ft_otp file: \n")
            if change_encrypt_pass(old_pass, args.new_pass):
                print("SUCCESSFULL CHANGE THE ENCRYPTION KEY OF THE 'ft_otp.key'.")
    # Interactive Mode
    if args.interactive != None and args.key_gen != None:
        try:
            if int(args.interactive) > 1:
                if verify_file(args.key_gen):
                    passwd = getpass("Enter the encryption key for the ft_otp file: \n")
                    interactive_totp(args.key_gen, passwd, int(args.interactive))
            else:
                print("ERROR SECONDS -> Try with a number greater than 1")
        except ValueError:
                print("ERROR VALUE SECONDS -> Try again with a number greater than 1.")
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
    parser.add_argument("-i","--interactive", default=None, help="[-k + 'ft_otp.key' -i + seconds] Interactive mode.")
    parser.add_argument("-v","--verbose", default=False, action='store_true', help="[-k + 'ft_otp.key' -v] Verbose Mode.") 
    parser.add_argument("-rk","--random-key", default=False, action='store_true', help="Generate a random key autentication in file 'key.hex'.") 
    parser.add_argument("-rp","--random-pass", default=False, action='store_true', help="Generate a random password Base64 for encrypt 'ft_otp.key'.")
    
    return parser.parse_args()

if __name__ == "__main__":
    main()
