import customtkinter
import tkinter as tk  # untuk StringVar

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


# untuk object main window dimana bisa nambahin tombol, label, frame, dll
root = customtkinter.CTk()

root.title("Converter By Raja")  # title window

root.geometry("400x340")  # geomtetri dalam windowed mode

root.iconbitmap("icon.ico") # icon windowsnya
icon_image = tk.PhotoImage(file="icon.png")  # icon png window nya
root.iconphoto(True, icon_image)  # set icon window nya

current_choice = "Meter Ke Centimeter"  # pilihan default


def optionmenu_callback(choice):
    print("Option Menu Clicked:", choice)  # terprint di terminal
    if choice == "Meter Ke Centimeter":  # jika pilihan menu ini
        global current_choice
        current_choice = "Meter Ke Centimeter"  # set pilihan yang sekarang
        if entry1.get():
            try:
                meter = float(entry1.get())
                centimeter = meter * 100.0
                entry2.delete(0, customtkinter.END)  # hapus dulu isi entry2
                entry2.insert(0, f"{centimeter}cm")
            except ValueError:
                entry2.delete(0, customtkinter.END)
                entry2.insert(0, "Invalid Input")
        label.configure(text="Konversi m Ke cm")  # Label nya diubah
    elif choice == "Kilometer Ke Meter":  # else if
        label.configure(text="Konversi km Ke m")
        if entry1.get():
            try:
                kilometer = float(entry1.get())
                meter = kilometer * 1000.0
                entry2.delete(0, customtkinter.END)
                entry2.insert(0, f"{meter}m")
            except ValueError:
                entry2.delete(0, customtkinter.END)
                entry2.insert(0, "Invalid Input")
    elif choice == ("Hektometer Ke Dekameter"):
        label.configure(text="konversi hm Ke dam")
        if entry1.get():
            try:
                hektometer = float(entry1.get())
                dekameter = hektometer * 10.0
                entry2.delete(0, customtkinter.END)
                entry2.insert(0, f"{dekameter}dam")
            except ValueError:
                entry2.delete(0, customtkinter.END)
                entry2.insert(0, "Invalid Input")


def convert():
    # setelah masuk bakal muncul text ini di terminal
    print("Convert Successfully")
    button.configure(text="Converted")
    # Mengubah state menjadi normal untuk mengizinkan penulisan tek / mengganti text di entry2
    entry2.configure(state="normal")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


label = customtkinter.CTkLabel(
    # Tampilan menu utama
    master=frame, text="Konversi Satuan", font=("Roboto", 24))
label.pack(pady=12, padx=10)

# Tampilan menu yang mau di konversi
entry1 = customtkinter.CTkEntry(
    master=frame, placeholder_text="(Default Nya Meter)")
entry1.pack(pady=12, padx=10)
optionmenu = customtkinter.CTkOptionMenu(master=frame, values=["Meter Ke Centimeter", "Kilometer Ke Meter", "Hektometer Ke Dekameter", ],
                                         command=optionmenu_callback)
optionmenu.set("Pilih Konversi")
optionmenu.pack(pady=12, padx=10)

button = customtkinter.CTkButton(
    master=frame, text="Convert", command=convert)  # Tombol untuk konversi
button.pack(pady=12, padx=10)

output_var = tk.StringVar()  # vriabel untuk menyimpan output
output_var.set("Hasil Konversi")  # set nilai awal output_var

entry2 = customtkinter.CTkEntry(
    # Tampilan menu yang sudah di konversi
    master=frame,
    textvariable=output_var,
    state="readonly"  # Membuat entry2 hanya baca saja (readonly
)
entry2.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Mantap Jiwa")
button.pack(pady=12, padx=10)


print('Opening GUI')  # terprint


def convert_km_ke_cm(km):
    return km * 100000.0


def main():
    while True:  # Selamanya Loop Sebelum Break
        user_input = input(
            "ketik 'exit' untuk keluar atau masukkan jumlah km jika ingin melanjutkan:")
        if user_input.lower() == 'exit':
            print("keluar dari program")
            break

        try:
            km = float(user_input)   # 1 km = 100000cm
        except ValueError:
            print("masukan tidak valid, masukan angka")
            # lanjut ke code selanjutnya
            continue
        else:
            # 1 km = 100000cm
            centimeter = (convert_km_ke_cm(km))
            print(f"{km} centimeter sama dengan {centimeter} kilometer")


if __name__ == "__main__":
    root.mainloop()
