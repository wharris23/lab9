# Name: Wyatt Harris
# Date: 7/23/24

def encode(password):
    encoded = ""
    for char in password:
        num = int(char)
        new_num = (num + 3) % 10
        encoded += str(new_num)
    return encoded


def decode(password):
    decoded = ""
    for char in password:
        num = int(char)
        new_num = (num - 3) % 10
        decoded += str(new_num)
    return decoded


def main():
    encoded = ''
    decoded = ''

    while True:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')

        choice = int(input('Please enter an option: '))

        if choice == 1:
            password = input('Please enter the password to encode: ')
            encoded = encode(password)
            print('Your password has been encoded and stored!\n')

        if choice == 2:
            decoded = decode(encoded)
            print(f'The encoded password is {encoded}, and the original password is {decoded}.\n')

        if choice == 3:
            break


if __name__ == '__main__':
    main()
