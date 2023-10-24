# Sara Fletcher
# 10 / 23 / 23

def decode(password):
    string = str(password)
    decoded_pass = ''

    for digit in string:
        if int(digit) >= 3:
            num = str(int(digit) - 3)
            decoded_pass += num
        elif int(digit) == 0:
            num = '7'
            decoded_pass += num
        elif int(digit) == 1:
            num ='8'
            decoded_pass += num
        elif int(digit) == 2:
            num = '9'
            decoded_pass += num
    return decoded_pass

