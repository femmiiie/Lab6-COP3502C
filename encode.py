#Sandro Mocevic
#10/13/2023

#shifts password by 3 in each position
def encode(password:str)->str:
    ret = ""
    for i in password:
        ret += str((int(i) + 3) % 10)
    return ret
    