n= int(input("Enter an integer:"))
eqvl = []
for base in [2,8,16]:
    result = ""
    temp = n
    while temp >0:
        rem = temp & (base - 1)
        temp = temp >> (3 if base == 8 else 4 if base == 16 else 1)
        result = (chr(55 + rem) if rem >= 10 else str(rem)) + result
    eqvl.append(result)

print(f"Binary equivalent of {n} is : {eqvl[0]}")
print(f"Octal equivalent of {n} is : {eqvl[1]}")
print(f"Hexadecimal equivalent of {n} is : {eqvl[2]}")