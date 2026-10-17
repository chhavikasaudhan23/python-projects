# Create QR Code For UPI

import qrcode

upi_id = input("Enter UPI ID: ")
name = input("Enter Name: ")

upi_url = f"upi://pay?pa={upi_id}&pn={name}"

qr = qrcode.make(upi_url)
qr.save("UPI.png")

print("UPI Ka QR Ban Gaya..!!")