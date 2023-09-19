from termcolor import cprint

def print_hi(name):
    cprint(f"Hi, {name}!", "green", "on_red")

if __name__ == '__main__':
    print_hi('world')
