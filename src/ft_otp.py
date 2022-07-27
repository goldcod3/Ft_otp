import argparse

# Main
def main():
    args = config_args()

def config_args():
    parser = argparse.ArgumentParser(
        description="""*** Ft_otp *** This is a double factor of autentication tool based 
        in algorithm TOTP (Time One-Time Password)"""
    )
    # Save a new ft_otp.key
    parser.add_argument("-g","--gen-key-file",default=None,help="[-g + key.hex] Set a new key for for ft_otp.key")
    # Generate a new key/pin
    parser.add_argument("-k","--key-gen",default=None,help="[-k + ft_otp.key] Generate a new key autentication.")
    return parser.parse_args()

if __name__ == "__main__":
    main()
