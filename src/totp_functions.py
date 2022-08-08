import hmac, struct
from os import system
from base64 import b32encode
from time import time, sleep
from datetime import datetime

format_date = '%Y-%m-%d %H:%M:%S UTC'
default_digest = 'SHA1'
default_counter = 30

# This function convert het to byte[]
def get_time_key(sec_count):
    return int(time() / sec_count)

def hmac_sha(key, msg, dig_type):
    key_bytes = bytearray.fromhex(key)
    msg_bytes = struct.pack(">Q", msg)
    mac = hmac.new(key_bytes, msg_bytes, dig_type)
    return mac.digest()

def totp(hex_key, counter):
    time_counter = get_time_key(counter)
    hmac_ = hmac_sha(hex_key, time_counter, default_digest)
    lst_b = hmac_[-1] & 0x0f
    pin = struct.unpack('>L', hmac_[lst_b:lst_b+4])[0] & 0x7fffffff
    return str(pin)[-6:]

def verbose_totp(key, counter):
    print("Hex secret:",key)
    print("Base32 secret:",b32encode(bytearray.fromhex(key)).decode('utf-8'))
    print("Digits:",6)
    print("TOTP mode:",default_digest)
    print("Step size (seconds):",counter)
    print("Start time: 1970-01-01 00:00:00 UTC (0)")
    time_ = datetime.utcfromtimestamp(time())
    time_str = datetime.strftime(time_, format_date)
    print("Current time: {} ({})".format(time_str,int(time())))
    time_counter = get_time_key(counter)
    print("Counter: {} ({})".format(hex(time_counter),time_counter))
    print("\n{}".format(totp(key,counter)))

def run():
    k_hex = 'a6367b2ad9d0c3b83f8d63ebdb0eb9ef9595cb798d87623d034bdebcf9065afb'
    #print(totp(k_hex, time_))
    timer = 120
    count = 0
    while (count<=timer):
        system('clear')
        time_ = datetime.utcfromtimestamp(time())
        time_str = datetime.strftime(time_, format_date)
        print("Current time: {} ({})".format(time_str,int(time())))
        print("OATHTOOL TOTP CODE:")
        system('oathtool --totp $(cat key.hex)')
        print("MY TOTP CODE:")
        print(totp(k_hex, default_counter))
        sleep(1)

run()
