#a qr code generator
################################
#Made by steven Foltz

import qrcode
import sys
import os

def main():
    print("Welcome to the QR code generator!")
    print("What would you like to name the file?>>>: ")
    #just an example
    text = "https://www.linkedin.com/in/steven-foltz-14b250207/"
    print("Please enter the name of the file you would like to save to: ")
    filename = input()
    print("What type of file would you like your QR code to be?:>>> ")
    filetype = input()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename + "." + filetype)
    print("QR code saved to " + filename + "." + filetype)
    print("Would you like to create another QR code? (y/n)>>>")
    answer = input()
    if answer == "y":
        main()
    else:
        print("Goodbye!")
        sys.exit()
    
if __name__ == "__main__":
    main()