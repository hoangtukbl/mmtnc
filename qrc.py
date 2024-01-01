import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
import qrcode

def create_qr_code():
    website_url = website_entry.get()
    image_name = image_name_entry.get()

    if not website_url or not image_name:
        messagebox.showerror("Error", "Please enter both website URL and image name")
        return

    # Tạo mã QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(website_url)
    qr.make(fit=True)



    # Tạo hình ảnh QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Lưu hình ảnh QR Code với tên đã nhập
    img.save(f"{image_name}.png")

    messagebox.showinfo("Success", f"QR Code has been created and saved as {image_name}.png")

# Tạo giao diện người dùng
root = tk.Tk()
root.title("QR Code Generator")

# Label và Entry cho đường link website
website_label = Label(root, text="Website URL:")
website_label.pack(pady=10)
website_entry = Entry(root, width=30)
website_entry.pack(pady=10)

# Label và Entry cho tên hình ảnh
image_name_label = Label(root, text="Image Name:")
image_name_label.pack(pady=10)
image_name_entry = Entry(root, width=30)
image_name_entry.pack(pady=10)

# Button để tạo QR Code
generate_button = Button(root, text="Generate QR Code", command=create_qr_code)
generate_button.pack(pady=20)

# Main loop của giao diện người dùng
root.mainloop()
