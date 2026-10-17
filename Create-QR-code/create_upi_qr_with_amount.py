# Create QR Code For UPI with specific Amount

import qrcode

upi_id = input("Enter UPI ID: ")
name = input("Enter Name: ")
amount = int(input("Enter Amount: "))

upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}"

# pa = Payee
# pn = Payee Name
# am = Amount
# cu = INR

qr = qrcode.make(upi_url)
qr.save("UPI_2.png")

print("UPI Ka QR Ban Gaya..!!")