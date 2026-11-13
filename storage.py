
import json
import os

from data import koleksi_dvd, data_akun, data_penyewa, data_transaksi, counter


FILE_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.json")

# Semua dictionary di bawah ini diisi ulang di tempat (bukan dibuat baru),
# supaya modul lain yang sudah meng-import-nya tetap memakai data yang sama.
SEMUA_DATA = {
    "koleksi_dvd": koleksi_dvd,
    "data_akun": data_akun,
    "data_penyewa": data_penyewa,
    "data_transaksi": data_transaksi,
    "counter": counter,
}


def simpan_data():
    isi = {nama: data for nama, data in SEMUA_DATA.items()}
    file_sementara = FILE_DATA + ".tmp"

    try:
        with open(file_sementara, "w", encoding="utf-8") as f:
            json.dump(isi, f, indent=4, ensure_ascii=False)
        os.replace(file_sementara, FILE_DATA)

    except (OSError, TypeError, ValueError) as e:
        print(f"\nPERINGATAN: data GAGAL disimpan ke {FILE_DATA}")
        print(f"Penyebab: {e}")

def muat_data():
    if not os.path.exists(FILE_DATA):
        simpan_data()
        return

    try:
        with open(FILE_DATA, "r", encoding="utf-8") as f:
            isi = json.load(f)

        # validasi dulu sebelum mengganti data yang sedang berjalan
        for nama in SEMUA_DATA:
            if not isinstance(isi.get(nama), dict):
                raise ValueError(f"bagian '{nama}' tidak valid")

    except (json.JSONDecodeError, ValueError, OSError):
        # file rusak: simpan sebagai cadangan, lalu lanjut dengan data awal
        os.replace(FILE_DATA, FILE_DATA + ".rusak")
        print("File database.json rusak, dipindahkan ke database.json.rusak.")
        print("Program memakai data awal.")
        simpan_data()
        return

    for nama, data in SEMUA_DATA.items():
        data.clear()
        data.update(isi[nama])
