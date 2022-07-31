import hmac
from datetime import datetime
from time import time
from cryptor import *

format_date = '%Y-%m-%d -> %H:%M:%S'
default_time_count = 30
default_digest = 'SHA1'

def get_time_key(time_count):
    time_ = datetime.utcfromtimestamp(time())
    timestr_ = datetime.strftime(time_, format_date)
    return str(int(time() / time_count)), timestr_

def gen_hash_totp(file):
    passwd = input('Enter the encryption key of the ft_otp file: ')
    time_, time_msg = get_time_key(default_time_count)
    key = get_key(file,passwd)
    if key != None:
        print(time_msg)
        hash_ = hmac.new(key, time_.encode('utf-8'), default_digest)
        return hash_.hexdigest()

def get_pin():
    print('-----------')
    #print(get_random_key())
    #print(get_random_pass())
    #encrypt_file("ft_otp.key", 'BOepxv8uKCV2spjcRQf8uOZcPJlaKPMkFkWLykmifQk=')
    #get_key('aMfPgI04l8pXvI7WVfof2X8Y6FCGzvh7_8Q0V0HEgz0=')
    
    #print(set_master_pass('aMfPgI04l8pXvI7WVfof2X8Y6FCGzvh7_8Q0V0HEgz0=',''))
    print('-----------')


#print(gen_hash_totp().hexdigest())