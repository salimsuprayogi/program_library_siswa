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
# untuk import fungsi di dalam file jurusan
from jurusan import *
# untuk import fungsi di dalam file pertanyaan
from pertanyaan import *
# untuk import fungsi di dalam file jawaban
from jawaban import *

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
        "9. Tambah Pertanyaan",
        "10. Tampilkan Pertanyaan",
        "11. Hapus Pertanyaan",
        "12. Ubah Pertanyaan",
        "===========================\n"
        "13. Tambah Jawaban",
        "14. Tampilkan Jawaban",
        "15. Hapus Jawaban",
        "16. Ubah Jawaban",
        "===========================\n"
        "17. Keluar\n"
        "===========================\n"
    ]

    # perulangan selama menu di tampilkan dan tidak memilih selain keluar
    # jika di pilih keluar, maka program akan berhenti
    while True:
        # menu
        for menu in menus:
            print(menu)

        # pilih daftar menu dengan angka
        selected = input("Pilih Menu : ")

        # siswa
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

        # jurusan
        elif (selected == "5"):
            insert_jurusan()
        elif (selected == "6"):
            show_jurusan()
        elif (selected == "7"):
            delete_jurusan()
        elif (selected == "8"):
            update_jurusan()

        # pertanyaan
        elif (selected == "9"):
            insert_pertanyaan()
        elif (selected == "10"):
            show_pertanyaan()
        elif (selected == "11"):
            delete_pertanyaan()
        elif (selected == "12"):
            update_pertanyaan()

        # jawaban
        elif (selected == "13"):
            insert_jawaban()
        elif (selected == "14"):
            show_jawaban()
        elif (selected == "15"):
            delete_jawaban()
        elif (selected == "16"):
            update_jawaban()

        # keluar
        else:
            print("Sampai jumpa kembali... :-D")
            # exit code=0 artinya program keluar dengan benar/tidak terjadi error
            # exit code=1 artinya program keluar tidak semestinya/error
            exit(code=0)

# terima kasih....... 