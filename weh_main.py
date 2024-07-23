def encode(password):
    encoded = ""
    for char in password:
        num = int(char)
        new_num = (num + 3) % 10
        encoded += str(new_num)
    return encoded


def decode(password):
    new = []
    for char in password:
        number = int(char)
        new.append(number)

    decoded = ""
    for val in new:
        if val > 2:
            val -= 3
            decoded += str(val)
        else:
            if val == 2:
                val = "9"
            elif val == 1:
                val = "8"
            elif val == 0:
                val = "7"
            decoded += str(val)
    return "".join(decoded)


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
