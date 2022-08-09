import hmac, struct
from os import system
from base64 import b32encode
from time import time, sleep
from datetime import datetime
from encode import get_key

# Default Variables
banner = """
  __ _                _             
 / _| |              (_)            
| |_| |_   ___  _ __  _  ___  _ __  
|  _| __| / _ \| '_ \| |/ _ \| '_ \ 
| | | |_ | (_) | | | | | (_) | | | |
|_|  \__| \___/|_| |_|_|\___/|_| |_|
      ______                        
     |______| github.com/goldcod3
"""
format_date = '%Y-%m-%d %H:%M:%S UTC'
default_digest = 'SHA1'
default_counter = 30

# Get time counter
def get_time_key(sec_count):
    return int(time() / sec_count)

# Get HMAC [Bite Array]
def hmac_sha(key, msg, dig_type):
    key_bytes = bytearray.fromhex(key)
    msg_bytes = struct.pack(">Q", msg)
    mac = hmac.new(key_bytes, msg_bytes, dig_type)
    return mac.digest()

# Get TOTP pin [Decimal pin number]
def totp(hex_key, counter, digits=6, type_h='SHA1'):
    time_counter = get_time_key(counter)
    hmac_ = hmac_sha(hex_key, time_counter, type_h)
    lst_b = hmac_[-1] & 0x0f
    pin = struct.unpack('>L', hmac_[lst_b:lst_b+4])[0] & 0x7fffffff
    return str(pin)[-digits:]

# Get TOTP Pin from keyfile
def get_totp_pin(file, password, digits=6, type_='SHA1'):
    key_hex = get_key(file, password)
    if key_hex != None:
        cod_totp = totp(key_hex.decode('utf-8'), default_counter, digits, type_)
        print(cod_totp)

# Get Verbose mode TOTP
def verbose_totp(key, counter=default_counter, digits=6, type_h='SHA1'):
    print(banner)
    print("Hex secret:", key)
    print("Base32 secret:",b32encode(bytearray.fromhex(key)).decode('utf-8'))
    print("Digits:", digits)
    print("TOTP mode:", type_h)
    print("Step size (seconds):", counter)
    print("Start time: 1970-01-01 00:00:00 UTC (0)")
    time_ = datetime.utcfromtimestamp(time())
    time_str = datetime.strftime(time_, format_date)
    print("Current time: {} ({})".format(time_str,int(time())))
    time_counter = get_time_key(counter)
    print("Counter: {} ({})".format(hex(time_counter),time_counter))
    print("\n{}".format(totp(key, counter)))

# Interactive Mode TOTP
def interactive_totp(file, passwd, seconds):
    key_hex = get_key(file, passwd)
    if key_hex != None:
        while (seconds >= 1):
            system('clear')
            verbose_totp(key_hex.decode('utf-8'), default_counter)
            seconds -=1
            sleep(1)
        system('clear')

    
