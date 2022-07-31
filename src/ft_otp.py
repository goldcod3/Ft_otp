import argparse
from encode import gen_hash_totp
from cryptor import *

# Main
def main():
    args = config_args()
    if args.key_gen != None:
        hash_ = gen_hash_totp(args.key_gen)
        if hash_ != None:
            print(hash_)
    if args.random_key == True:
        print(get_random_key().decode())
    if args.random_pass == True:
        print(get_random_pass())
    
    

def config_args():
    parser = argparse.ArgumentParser(
        description="""*** Ft_otp *** This is a double factor of autentication tool based 
        in algorithm TOTP (Time One-Time Password)"""
    )
    # Generate a new key/pin
    parser.add_argument("-k","--key-gen",default=None,help="[-k + ft_otp.key] Generate a new key autentication.")
    
    # Save a new ft_otp.key
    #parser.add_argument("-g","--change-key",default=None,help="[-g + key.hex] Set a new key for for ft_otp.key")
    #parser.add_argument("-p","--change-pass",default=None,help="[-p + ft_otp.key] Generate a new key autentication.")

    # Bonus options   
    parser.add_argument("-rk","--random-key",default=False,action='store_true',help="Generate a random key autentication.") 
    parser.add_argument("-rp","--random-pass",default=False,action='store_true',help="Generate a random password autentication.")
    return parser.parse_args()

if __name__ == "__main__":
    main()
