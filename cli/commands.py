import os

def ls():
    return os.listdir()

def touch(filename):
    with open(filename, 'a'):
        pass

def vi(filename):
    os.system(f'vi {filename}')

def nano(filename):
    os.system(f'nano {filename}')

def cd(directory):
    os.chdir(directory)

def cat(filename):
    with open(filename, 'r') as file:
        return file.read()

def mkdir(directory):
    os.makedirs(directory)
