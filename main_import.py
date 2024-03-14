#main construct_library


def print_name():
    print(f'\nthis is the value of __name__ from this module: {__name__}')


def main():
    print_name()


if __name__ == '__main__':main()