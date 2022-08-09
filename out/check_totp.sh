while true; do  
    clear
    oathtool --totp $(cat key.hex) -v
    sleep 1
done    