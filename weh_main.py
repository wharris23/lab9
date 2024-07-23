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
