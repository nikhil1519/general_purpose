import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def select_image():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("JPEG Image", "*.jpg *.jpeg"), ("All Files", "*.*")]
    )
    if file_path:
        entry_input_path.delete(0, tk.END)
        entry_input_path.insert(0, file_path)

def save_as():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".jpg",
        filetypes=[("JPEG Files", "*.jpg"), ("All Files", "*.*")]
    )
    if file_path:
        entry_output_path.delete(0, tk.END)
        entry_output_path.insert(0, file_path)

def resize_and_compress_image():
    input_path = entry_input_path.get()
    output_path = entry_output_path.get()
    width = entry_width.get()
    height = entry_height.get()
    target_size_kb = entry_size.get()

    if not input_path or not output_path or not width or not height or not target_size_kb:
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        width, height, target_size_kb = int(width), int(height), int(target_size_kb)

        img = Image.open(input_path)
        img = img.resize((width, height), Image.LANCZOS)

        quality = 95
        img.save(output_path, format="JPEG", quality=quality)

        while os.path.getsize(output_path) > target_size_kb * 1024 and quality > 10:
            quality -= 5
            img.save(output_path, format="JPEG", quality=quality)

        messagebox.showinfo("Success", f"Image saved successfully at {output_path}\nSize: {os.path.getsize(output_path) / 1024:.2f} KB")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong!\n{e}")

def go_back():
    entry_input_path.delete(0, tk.END)
    entry_output_path.delete(0, tk.END)
    entry_width.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    entry_size.delete(0, tk.END)

root = tk.Tk()
root.title("Image Resizer & Compressor")
root.geometry("500x450")
root.resizable(False, False)

tk.Label(root, text="Select Image:").pack(pady=5)
entry_input_path = tk.Entry(root, width=50)
entry_input_path.pack()
tk.Button(root, text="Browse", command=select_image).pack()

tk.Label(root, text="Save As:").pack(pady=5)
entry_output_path = tk.Entry(root, width=50)
entry_output_path.pack()
tk.Button(root, text="Choose Save Location", command=save_as).pack()

tk.Label(root, text="Width (px):").pack(pady=5)
entry_width = tk.Entry(root, width=10)
entry_width.pack()

tk.Label(root, text="Height (px):").pack(pady=5)
entry_height = tk.Entry(root, width=10)
entry_height.pack()

tk.Label(root, text="Target Size (KB):").pack(pady=5)
entry_size = tk.Entry(root, width=10)
entry_size.pack()

tk.Button(root, text="Resize & Compress", command=resize_and_compress_image, bg="blue", fg="white").pack(pady=10)
tk.Button(root, text="Back", command=go_back, bg="gray", fg="white").pack(pady=5)

root.mainloop()
