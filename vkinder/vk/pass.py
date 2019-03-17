
def get_pass():
    f = open('pass.txt', 'r')
    PASSWORD = f.read().rstrip()
    f.close()
    return PASSWORD

