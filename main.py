# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

# - [ ] Implementasi kode
# - [ Setup Library ] Kebutuhan libarary & instalasi
# - [ Implementasi ] Menghubungkan database dg kode
# - [ Implementasi ] Membuat fungsi crud pada kode

# pip3 install pymysql
# pip install MySQL-python
# ref : https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html
# ref : https://www.tutorialspoint.com/python3/python_database_access.htm

# untuk import fungsi di dalam file siswa
# * untuk memanggil semua fungsi di dalam file siswa
from siswa import *
from jurusan import *

if __name__ == "__main__":
    # ini digunakan untuk tes setiap fungsi dalam pembuatan awal fungsi satu persatu
    # insert_siswa()
    # show_siswa()
    # delete_siswa()
    # update_siswa()
    # insert_jurusan()

    # menampilkan program
    print("Library Siswa")
    # daftar menu
    menus = [
        "1. Tambah Siswa",
        "2. Tampilkan Siswa",
        "3. Hapus Siswa",
        "4. Ubah Siswa",
        "===========================\n"
        "5. Tambah Jurusan",
        "6. Tampilkan Jurusan",
        "7. Hapus Jurusan",
        "8. Ubah Jurusan",
        "===========================\n"
        "9. Keluar"
    ]

    # perulangan selama menu di tampilkan dan tidak memilih selain keluar
    # jika di pilih keluar, maka program akan berhenti
    while True:
        for menu in menus:
            print(menu)

        # pilih daftar menu dengan angka
        selected = input("Pilih Menu : ")

        # jika pilih 1, akan eksekusi kondisi ini
        if (selected == "1"):
            insert_siswa()
        # jika pilih 2, akan eksekusi kondisi ini
        elif (selected == "2"):
            show_siswa()
        # jika pilih 3, akan eksekusi kondisi ini
        elif (selected == "3"):
            delete_siswa()
        # jika pilih 4, akan eksekusi kondisi ini
        elif (selected == "4"):
            update_siswa()
        # jika pilih 5 / selain daftar menu akan eksekusi program ini
        elif (selected == "5"):
            insert_jurusan()
        elif (selected == "6"):
            show_jurusan()
        elif (selected == "7"):
            delete_jurusan()
        elif (selected == "8"):
            update_jurusan()
        else:
            print("Sampai jumpa kembali... :-D")
            # exit code=0 artinya program keluar dengan benar/tidak terjadi error
            # exit code=1 artinya program keluar tidak semestinya/error
            exit(code=0)
