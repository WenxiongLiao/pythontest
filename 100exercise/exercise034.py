def print_hello():
    print('hello ')

def print_world():
    print_hello()
    print('world')

if __name__ == '__main__':
    print_world()