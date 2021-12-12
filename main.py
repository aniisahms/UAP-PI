"""
Nama program    :
Dibuat oleh     :
Dibuat pada     :
Selesai pada    : 13 Desember 2021
Revisi pada     :
"""

from mod_class import *
from mod_func import *
import os


def main():
    addPustakawan()

    os.system("cls")
    pustakawanSekarang = loginPustakawan()

    while(True):
        os.system("cls")
        print("=== SELAMAT DATANG ===")
        print("Halo, " + pustakawanSekarang)
        print("1 Daftarkan Anggota Baru")
        print("2 Daftarkan Buku Baru")
        print("3 Peminjaman Buku")
        print("0 Keluar")
        pilihan = input("Masukkan Pilihan : ")

        if pilihan == "1":
            anggotaBaru = daftar()
            os.system("cls")
            print("======================================================")
            print("Anda Berhasil Mendaftarkan Anggota Baru!")
            print("Pustakawan   : " + pustakawanSekarang)
            print("ID Anggota   : " + str(anggotaBaru.get_id_ang()))
            print("Nama Anggota : " + anggotaBaru.get_nama_ang())
            print("======================================================")
        elif pilihan == "2":
            bukuBaru = addBuku()
            os.system("cls")
            print("======================================================")
            print("Anda Berhasil Mendaftarkan Buku Baru!")
            print("Pustakawan   : " + pustakawanSekarang)
            print("ID Buku      : " + str(bukuBaru.get_id_buku()))
            print("Judul        : " + bukuBaru.get_judul())
            print("Penulis      : " + bukuBaru.get_penulis())
            print("Penerbit     : " + bukuBaru.get_penerbit())
            print("Tahun Terbit : " + bukuBaru.get_tahun_terbit())
            print("======================================================")
        elif pilihan == "3":
            peminjamanBaru = pinjam()
            os.system("cls")
            print("======================================================")
            print("Peminjaman Baru Dibuat!")
            print("Peminjam        : " + peminjamanBaru.get_id_peminjam().get_nama_ang())
            print("Judul           : " + peminjamanBaru.get_id_buku().get_judul())
            print("Lama Peminjaman : " + str((peminjamanBaru.get_tgl_kembali() - peminjamanBaru.get_tgl_pinjam()).days) + " hari")
            print("Total Denda     : " + str(peminjamanBaru.get_denda()))
            print("======================================================")
        elif pilihan == "0":
            break
        else:
            print("Masukan Salah!")

        input()

while __name__ == "__main__":
    main()