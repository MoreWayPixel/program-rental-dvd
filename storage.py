
import json
import os

from data import koleksi_dvd, data_akun, data_penyewa, data_transaksi, counter


file_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.json")

semua_data = {
    "koleksi_dvd": koleksi_dvd,
    "data_akun": data_akun,
    "data_penyewa": data_penyewa,
    "data_transaksi": data_transaksi,
    "counter": counter,
}


def simpan_data():
    isi = {nama: data for nama, data in semua_data.items()}
    file_sementara = file_data + ".tmp"

    try:
        with open(file_sementara, "w", encoding="utf-8") as f:
            json.dump(isi, f, indent=4, ensure_ascii=False)
        os.replace(file_sementara, file_data)

    except (OSError, TypeError, ValueError) as e:
        print(f"\nPERINGATAN: data GAGAL disimpan ke {file_data}")
        print(f"Penyebab: {e}")

def muat_data():
    if not os.path.exists(file_data):
        simpan_data()
        return

    try:
        with open(file_data, "r", encoding="utf-8") as f:
            isi = json.load(f)

        for nama in semua_data:
            if not isinstance(isi.get(nama), dict):
                raise ValueError(f"bagian '{nama}' tidak valid")

    except (json.JSONDecodeError, ValueError, OSError):

        os.replace(file_data, file_data + ".rusak")
        print("File database.json rusak, dipindahkan ke database.json.rusak.")
        print("Program memakai data awal.")
        simpan_data()
        return

    for nama, data in semua_data.items():
        data.clear()
        data.update(isi[nama])
