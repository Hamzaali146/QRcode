import qrcode
count = 0
while True:
    ongo=input("want to add student:").upper()
    if ongo =="N":
        break
    name=input("Enter Student name: ")
    roll = int(input("Write student rollno: "))
    section = input("Write student section: ")
    msg = input("any message you want to type: ")
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    data =f"{name} \n{roll} \n{section}\n{msg}"
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"Qrcode/qr_Code_{name}.png")
