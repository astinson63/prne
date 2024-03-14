# main construct - main file
import main_import 


def print_base_name():
    print(f'this is the value of __name__ from the base module: {__name__}')
    

def main():
    main_import.print_name()
    print_base_name()


if __name__ == '__main__':main()