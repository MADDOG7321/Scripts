#Converts IP addresses to binary. NOTE: input must be formatted correctly and be a valid ip address eg. 0.0.0.0 -> 255.255.255.255

def addressToBinary(option = input("What is the address: ")):
    optiontable = option.split(".")
    
    binarytable = [128, 64, 32, 16, 8, 4, 2, 1]
    
    binarystring = ""
    
    for x in range(len(optiontable)):
        for binarynum in binarytable:
            if int(optiontable[x]) + 1 - binarynum > 0:
                binarystring += "1"
                optiontable[x] = str(int(optiontable[x]) - binarynum)
            else:
                binarystring += "0"
        binarystring += "."
    binarystring = binarystring[:-1]
    
    return binarystring

if __name__ == '__main__':
    print(addressToBinary())
    input("\nPress enter to exit . . .")
