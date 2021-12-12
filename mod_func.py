import random
import string
from mod_class import *

def id_generator(size = 6, chars = string.ascii_uppercase + string.digits) :
    return ''.join(random.choice(chars) for _ in range(size))

def daftar() :
    print("=== DAFTARKAN DIRI ANDA SEBAGAI ANGGOTA PERPUSTAKAAN ===")
    namaAng = input("Masukkan nama: ")
    telpAng = input("Masukkan nomor telepon: ")
    uid = id_generator()
    print("\nId anggota Anda: ", uid)
    print("\n=== TERIMA KASIH TELAH MENDAFTAR, SELAMAT MEMBACA ===")

def pinjam() :
    print("=== AYO PINJAM BUKU ===")
