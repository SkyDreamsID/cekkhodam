import os
import random

KHODAM = ("Naga Putih",
          "Ular Tangga",
          "Pocong Kota",
          "Ban Sepur",
          "Trenggiling",
          "Tikus Got",
          "Anjing",
          "Ban Dalam",
          "Macan",
          "Kadal",
          "Ambatron",
          "Aspal tol Cipularang",
          "Roti O stasiun Lempuyangan",
          "Ambatukam",
          "Pace Yunus",
          "Si Imut",
          "Rusdi",
          "Martabak Jagung",
          "Teh Poci",
          "Gedhang Goreng",
          "Bagas Dribble",
          "Mister Niko",
          "Rohmat Ambatukam",
          "Rifki Bejir",
          "Tegar Hengker",
          "Roger Sumatra",
          "Sendirian")

def header():
    """header"""
    os.system("cls") if os.name == "nt" else os.system("clear")
    print(f"{'CEK KHODAM V.0.0.1':^40}")
    print(f"{'Developed by SkyDreamsID':^40}")
    print(f"{'-'*40:^40}")


def input_user():
    """input nama"""
    while True:
        nama = input("Masukkan Nama \t: ")
        if nama.strip():
            return nama
        else:
            print("Nama tidak boleh kosong!")


def display(nama, value):
    """Menampilkankhodam."""
    if khodam == "Sendirian":
        print(f"{nama} kamu sendirian")
    else:
        print(f"{nama} ditemani oleh {value}")


def find_khodam(nama):
    khodam = random.choice(KHODAM)
    return khodam


# Program utama
while True:
    header()
    nama = input_user()
    khodam = find_khodam(nama)
    display(nama, khodam)
    print(f"{'-'*40:^40}")
    is_continue = input("\nMau lagi? (y/n) ")
    if is_continue.lower() != "y":
        break

print(f"{'---- Program selesai, terima kasih ----':^40}")
