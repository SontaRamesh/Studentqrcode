import qrcode

def generate_qr_code(roll_no, name, branch, cgpa):
    # Format the data as a string
    data = f"Roll No: {roll_no}\nName: {name}\nBranch: {branch}\nCGPA: {cgpa}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code as an image
    qr_img.save("student_qr.png")
    print("QR code generated successfully.")

# Example usage
roll_no = input("Enter Roll No: ")
name = input("Enter Name: ")
branch = input("Enter Branch: ")
cgpa = input("Enter CGPA: ")

generate_qr_code(roll_no, name, branch, cgpa)
