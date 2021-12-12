import random
import string
import datetime
from typing import final
from mod_class import *

dataBuku = list()
dataPustakawan = list()
dataAnggota = list()
dataPeminjaman = list()

def id_generator(size = 6, chars = string.ascii_uppercase + string.digits) :
    return ''.join(random.choice(chars) for _ in range(size))

def daftar() :
    print("===              MASUKKAN DATA DIRI               ===")
    namaAng = input("Masukkan nama: ")
    telpAng = input("Masukkan nomor telepon: ")
    uid = id_generator()
    anggotaBaru = AnggotaPerpus(uid, namaAng, telpAng)
    dataAnggota.append(anggotaBaru)
    return anggotaBaru

def pinjam() :
    print("===           MASUKKAN DATA PEMINJAMAN            ===")
    idPeminjaman = id_generator(size=10)
    idPeminjam = input("ID Anggota                    : ")
    idBuku = input("ID Buku                       : ")
    tanggalPinjam = input("Tanggal Peminjaman (YYYYMMDD) : ")
    tanggalKembali = input("Tanggal Kembali (YYYYMMDD)    : ")
    
    try:
        if len(tanggalPinjam) == 8 and len(tanggalKembali) == 8:
            tahunPinjam = int(tanggalPinjam[:4])
            bulanPinjam = int(tanggalPinjam[4:6])
            hariPinjam = int(tanggalPinjam[6:])

            tanggalPinjamParsed = datetime.date(tahunPinjam, bulanPinjam, hariPinjam)
        
            tahunKembali = int(tanggalKembali[:4])
            bulanKembali = int(tanggalKembali[4:6])
            hariKembali = int(tanggalKembali[6:])

            tanggalKembaliParsed = datetime.date(tahunKembali, bulanKembali, hariKembali)
        else:
            raise Exception("Format Tanggal Salah")
    except Exception as e:
        print("Error : " + str(e))
    finally:
        selisih = tanggalKembaliParsed - tanggalPinjamParsed
        if selisih.days > 7:
            denda = (selisih.days - 7) * 2000
        else:
            denda = 0

        for i in dataAnggota:
            if i.get_id_ang() == idPeminjam:
                for j in dataBuku:
                    if j.get_id_buku() == idBuku:
                        peminjamanBaru = PeminjamanBuku(idPeminjaman, j, i, tanggalPinjamParsed, tanggalKembaliParsed, denda)
                        dataPeminjaman.append(peminjamanBaru)

                        return peminjamanBaru
                else:
                    print("Buku Tidak Ditemukan!")
        else:
            print("ID Anggota Tidak Ditemukan!")

def addPustakawan():
    dataPustakawan.append(Pustakawan("000001","-"))

def loginPustakawan():
    while(True):
        id = input("ID Anda : ")
        try:
            for i in dataPustakawan:
                if i.get_id_pus() == id:
                    return i.get_nama_pus()

            else:
                raise Exception("ID Tidak Ditemukan!")
        except Exception as e:
            print("Error : " + str(e))

def addBuku():
    print("===              MASUKKAN DATA BUKU               ===")
    id_buku = id_generator(size=10)
    judul = input("Masukkan Judul        : ")
    penulis = input("Masukkan Penulis      : ")
    penerbit = input("Masukkan Penerbit     : ")
    tahun_terbit = input("Masukkan Tahun Terbit : ")
    bukuBaru = Buku(id_buku, judul, penulis, penerbit, tahun_terbit)

    dataBuku.append(bukuBaru)

    return bukuBaru