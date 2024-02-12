import zipfile
from itertools import product

def brute_force_decrypt(file_path):
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    password_length = 8
    zip_file = zipfile.ZipFile(file_path)
    for combination in product(charset, repeat=password_length):
        password = ''.join(combination)
        try:
            zip_file.extractall(pwd=bytes(password, 'utf-8'))
            zip_file.close()
            return password  # Password found
        except:
            continue
    zip_file.close()
    return "Password not found."
