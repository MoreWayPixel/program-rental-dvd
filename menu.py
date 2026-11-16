import inquirer

from tema import tema_admin, tema_user
from utils import clear_terminal, enter
from dvd import tampilkan_koleksi, cari_dvd, manage_dvd
from penyewa import tampilkan_penyewa, manage_penyewa
from transaksi import tampilkan_transaksi, pengembalian_dvd, manage_transaksi, sewa_dvd, lihat_total_pendapatan


def menu_admin():
    clear_terminal()
    print("Anda login sebagai admin!")
    enter("Tekan Enter untuk melanjutkan ke menu admin...")

    while True:
        clear_terminal()
        print("=====================================")
        print("              MENU ADMIN")
        print("=====================================")
        pertanyaan = [inquirer.List("pilihan", 
                                    message="Pilih menu", 
                                    choices=[" Lihat koleksi DVD", " Cari DVD", " Manage DVD", " Lihat data penyewa", " Manage data penyewa", " Lihat semua transaksi", " Manage transaksi", " Lihat total pendapatan", " Logout"])
                     ]

        jawaban = inquirer.prompt(pertanyaan, theme=tema_admin())

        if jawaban["pilihan"] == " Lihat koleksi DVD":
            clear_terminal()
            print("KOLEKSI DVD 💿")
            tampilkan_koleksi()
            print()
            enter("Tekan Enter untuk kembali ke menu admin...")

        elif jawaban["pilihan"] == " Cari DVD":
            cari_dvd()

        elif jawaban["pilihan"] == " Manage DVD":
            manage_dvd()

        elif jawaban["pilihan"] == " Lihat data penyewa":
            clear_terminal()
            print("DATA PENYEWA 📄")
            tampilkan_penyewa()
            enter("Tekan Enter untuk kembali ke menu admin...")

        elif jawaban["pilihan"] == " Manage data penyewa":
            manage_penyewa()

        elif jawaban["pilihan"] == " Lihat semua transaksi":
            clear_terminal()
            print("SEMUA TRANSAKSI 📝")
            tampilkan_transaksi()
            print()
            enter("Tekan Enter untuk kembali ke menu admin...")
            
        elif jawaban["pilihan"] == " Manage transaksi":
            manage_transaksi()

        elif jawaban["pilihan"] == " Lihat total pendapatan":
            lihat_total_pendapatan()

        elif jawaban["pilihan"] == " Logout":
            clear_terminal()
            print("Logout berhasil.")
            enter("Tekan Enter untuk melanjutkan...")
            break

        else:
            print("Opsi tidak valid! Masukkan pilihan 1 sampai 13.")
            enter("Tekan Enter untuk mencoba lagi...")

def menu_pengguna(username):
    while True:
        clear_terminal()
        print("=============================")
        print("        MENU PENGGUNA")
        print("=============================")
        pertanyaan = [inquirer.List("pilihan", 
                                    message="Pilih menu", 
                                    choices=[" Lihat koleksi DVD", " Cari DVD", " Sewa DVD", " Lihat transaksi saya", " Kembalikan DVD", " Logout"])
                    ]

        jawaban = inquirer.prompt(pertanyaan, theme=tema_user())

        if jawaban["pilihan"] == " Lihat koleksi DVD":
            clear_terminal()
            print("KOLEKSI DVD 💿")
            tampilkan_koleksi()
            enter()

        elif jawaban["pilihan"] == " Cari DVD":
            cari_dvd()

        elif jawaban["pilihan"] == " Sewa DVD":
            sewa_dvd(username)

        elif jawaban["pilihan"] == " Lihat transaksi saya":
            clear_terminal()
            print("TRANSAKSI SAYA 👤")
            tampilkan_transaksi(username)
            enter()

        elif jawaban["pilihan"] == " Kembalikan DVD":
            pengembalian_dvd(username)

        elif jawaban["pilihan"] == " Logout":
            clear_terminal()
            print("Logout berhasil.")
            enter("Tekan Enter untuk melanjutkan...")
            break

        else:
            print("\nOpsi tidak valid! Masukkan pilihan 1 sampai 6.")
            enter("Tekan Enter untuk mencoba lagi...")