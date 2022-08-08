echo "OATHTOOL TOTP:"
oathtool --totp $(cat key.hex)
echo "MY TOTP"
python3 totp_functions.py