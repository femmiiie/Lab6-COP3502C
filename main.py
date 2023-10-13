#Sandro Mocevic
#10/13/2023

from encode import encode
from decode import decode

def menu()->None:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit \n")

def main():
    num, encoded = 0, 0
    while True:
        menu()

        option = input("Please enter an option: ")
        if option == "1":
            num = int(input("Please enter your password to encode: "))
            encoded = encode(num)
            print("Your password has been encoded and stored!")
        
        elif option == "2":

            print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}")

        elif option == "3":
            exit()


if __name__ == "__main__":
    main()