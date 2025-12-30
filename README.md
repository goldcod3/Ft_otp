## Ft_otp: Secure TOTP Password Generator

After projects like get_next_line, Ft_otp represents a more advanced step within the 42Madrid cursus. Here, it’s not just about manipulating files or memory, but about diving into security and authentication: implementing a TOTP (Time-based One-Time Password) system capable of generating ephemeral passwords based on a master key.

<img src='https://media.giphy.com/media/IgLIVXrBcID9cExa6r/giphy.gif' width=330 heigth= 330/>

---
### 🌐What is Ft_otp?

Ft_otp is a tool that generates temporary passwords following the TOTP standard. These passwords are useful for two-factor authentication and are created from a master key that you define and protect with encryption.
The project allows you to:
- Implement the TOTP algorithm following [RFC 6238](https://datatracker.ietf.org/doc/html/rfc6238).
- Generate and encrypt a master key (ft_otp.key).
- Produce temporary passwords verifiable from another client sharing the secret key.
- Explore security concepts such as HMAC and Base64 encryption.

---
### 🧩Project Objective

Create a TOTP generator that meets the following requirements:
- Receive a master key as a seed.
- Generate 6-digit time-based codes.
- Allow verification from another client application with the same key and timer.
- Ensure security by encrypting the master key and providing protected password options.

### ⭐ Bonus Part

Advanced options include:
- Choosing and password-protecting the ft_otp.key master key, requiring it each time a new temporary code is generated.
- Developing a graphical client that generates and validates master passwords.
- Adding any other useful functionality to enhance security or usability.

---
### 📚Key Concepts

To implement Ft_otp correctly, you need to understand:
- [TOTP](https://datatracker.ietf.org/doc/html/rfc6238#section-4) (Time-based One-Time Password): Time-dependent one-time passwords.
- [HOTP](https://datatracker.ietf.org/doc/html/rfc4226) (HMAC-based One-Time Password): Base algorithm for TOTP, replacing the counter with the current time.
- [HMAC](https://datatracker.ietf.org/doc/html/rfc2104): Keyed-hash function used to ensure data integrity and authenticity.

The TOTP formula is defined as:
`TOTP value(K) = trunc(HOTP value(K, CT))`
Where K is the secret key and CT is a counter derived from the current time. The result is a 6-digit PIN that can be validated from another client sharing the same secret key and timer.

#### 🔐 Security and Encryption
The TOTP key can be encrypted using Base64, and useful options were added (as indicated in the bonus) to protect the master key and control its usage.

---
### 💻Execution and Usage

In the repository:
- The src folder contains the source code in Python, allowing modification of algorithm parameters.
- The ft_otp(debian).zip file in out includes a script with dependencies for Linux, running without the need to install Python 3.

Script usage options:
```
# Generar nueva clave/pin TOTP
./ft_otp -k ft_otp.key
# Guardar una nueva clave hexadecimal de 64 caracteres
./ft_otp -g key.hex
# Cambiar la contraseña de cifrado de ft_otp.key
./ft_otp -p <key.hex_value>
# Modo interactivo TOTP
./ft_otp -k ft_otp.key -i SECONDS
# Generar clave aleatoria hexadecimal de 64 caracteres
./ft_otp -rk
# Generar contraseña aleatoria Base64
./ft_otp -rp
# Mostrar ayuda
./ft_otp -h
```

---
### 🐳Docker Testing

A Dockerfile has been set up to create a container with all dependencies:
- Clone the repository
- Install Docker Desktop
- Use the Makefile to build and run the container: make && make exec

Inside the container, the src and out directories are synchronized with your /home folder, allowing you to edit and run the code conveniently.

---
🚀 Conclusion

Ft_otp not only teaches TOTP and HMAC, but also combines:
- Security and encryption
- Secret key management
- Development of interactive scripts and automation
- Docker containers for fast deployment

It’s a perfect project to consolidate knowledge in security, Python, and programming best practices before tackling more complex systems at 42Madrid.
