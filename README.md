# Ft_otp
Proyect Ft_otp [2FA-TOTP] developed in the cybersecurity bootcamp at 42Madrid.

<img src='https://media.giphy.com/media/IgLIVXrBcID9cExa6r/giphy.gif' width=330 heigth= 330/>

In this project, the objective is to implement a TOTP system (Time-based One-Time Password), which is able to generate ephemeral passwords from a master key.
It will be based on the [RFC](https://datatracker.ietf.org/doc/html/rfc6238)

In the **src** directory you can find the source code made in python and you will be able to modify the algorithm parameters.

The **ft_onion(debian).zip** file in the directory **out** contains a script with its dependencies for Linux systems which will run without the need of python3.

# Script Options
```
# Generate a new TOTP key/pin
./ft_otp -k ft_otp.key

# Save a new key [hexadecimal - 64 characters] ft_otp.key.
./ft_otp -g key.hex

# Change the encryption Base64 password of the 'ft_otp.key' file
./ft_otp -p P_l1F4g7hC5o3UWD273fcCmVJrfeCDVEG3D4aDCXaCI=

# Interactive mode TOTP
./ft_otp -k ft_otp.key -i SECONDS

# Generate a 64-character hexadecimal random key in a 'key.hex' file.
./ft_otp -rk

# Generate a Base64 random password.
./ft_otp -rp

# Print help message
./ft_otp -h
```

# Docker test
A Dockerfile has been configured that generates a docker container with the software dependencies, 
to speed up the deployment of the container a Makefile was configured.

- Install '[Docker Desktop](https://www.docker.com/products/docker-desktop/)' and run the app.
- Install 'make' and use the Makefile for buid a container and get a bash:
```
make && make exec
```
```
# Build image and container
->> make
# Get a bash from container
->> make exec
# Build a new container
->> make dock
# Build image
->> make image
# Remove image and container
->> make fclean
```

- When you are inside the container, two volumes will be created synchronizing the **src** and **out** with the user's **/home** directory, 
allowing code editing and execution. 

---
Finished project.

![lgomes-o's 42 ft_otp Score](https://badge42.vercel.app/api/v2/cl4osmqtg006109jvtxcd7k3u/project/2714212)
