class AnggotaPerpus :
    def __init__(self, id_ang, nama_ang, telp) :
        self.id_ang = id_ang
        self.nama_ang = nama_ang
        self.telp = telp

    def set_id_ang(self, id_ang) :
        self.id_ang = id_ang

    def get_id_ang(self) :
        return self.id_ang
    
    def set_nama_ang(self, nama_ang) :
        self.nama_ang = nama_ang
    
    def get_nama_ang(self) :
        return self.nama_ang

    def set_telp(self, telp) :
        self.telp = telp

    def get_telp(self) :
        return self.telp

class Pustakawan :
    def __init__(self, id_pus, nama_pus) :
        self.id_pus = id_pus
        self.nama_pus = nama_pus

    def set_id_pus(self, id_pus) :
        self.id_pus = id_pus
    
    def get_id_pus(self) :
        return self.id_pus
    
    def set_nama_pus(self, nama_pus) :
        self.nama_pus = nama_pus
    
    def get_nama_pus(self) :
        return self.nama_pus
    

class Buku :
    def __init__(self, id_buku, judul, penulis, penerbit, tahun_terbit) :
        self.id_buku = id_buku
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
    
    def set_id_buku(self, id_buku) :
        self.id_buku = id_buku
    
    def get_id_buku(self) :
        return self.id_buku
    
    def set_judul(self, judul) :
        self.judul = judul

    def get_judul(self) :
        return self.judul
    
    def set_penulis(self, penulis) :
        self.penulis = penulis

    def get_penulis(self) :
        return self.penulis

    def set_penerbit(self, penerbit) :
        self.penerbit = penerbit

    def get_penerbit(self) :
        return self.penerbit

    def set_tahun_terbit(self, tahun_terbit) :
        self.tahun_terbit = tahun_terbit

    def get_tahun_terbit(self) :
        return self.tahun_terbit


class PeminjamanBuku :
    def __init__(self, id_peminjaman, id_buku, id_peminjam, tgl_pinjam, tgl_kembali, denda) :
        self.id_peminjaman = id_peminjaman
        self.id_buku = id_buku
        self.id_peminjam = id_peminjam
        self.tgl_pinjam = tgl_pinjam
        self.tgl_kembali = tgl_kembali
        self.denda = denda

    def set_id_peminjaman(self, id_peminjaman) :
        self.id_peminjaman = id_peminjaman
    
    def get_id_peminjaman(self) :
        return self.id_peminjaman

    def set_id_buku(self, id_buku) :
        self.id_buku = id_buku
    
    def get_id_buku(self) :
        return self.id_buku

    def set_id_peminjam(self, id_peminjam) :
        self.id_peminjaman = id_peminjam
    
    def get_id_peminjam(self) :
        return self.id_peminjam
    
    def set_tgl_pinjam(self, tgl_pinjam) :
        self.tgl_pinjam = tgl_pinjam
    
    def get_tgl_pinjam(self) :
        return self.tgl_pinjam
    
    def set_tgl_kembali(self, tgl_kembali) :
        self.tgl_kembali = tgl_kembali
    
    def get_tgl_kembali(self) :
        return self.tgl_kembali
    
    def set_denda(self, denda) :
        self.denda = denda
    
    def get_denda(self) :
        return self.denda