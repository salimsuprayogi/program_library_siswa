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

# modul
# import mysql.connector
import pymysql
# import json untuk menampilkan di terminal menjadi rapi / nyaman di baca
import json
# import OperationalError dan ProgrammingError untuk exception
from pymysql import OperationalError, ProgrammingError


def connect_db():
    # fungsi connect database
    # open database connection
    db = pymysql.connect("127.0.0.1", "root", "admin", "angket")
    return db


def insert_siswa():
    # fungsi tambah siswa
    # open database connection
    db = connect_db()

    # persiapkan objek kursor menggunakan metode kursor ()
    cursor = db.cursor()

    # tambah data siswa dengan input
    nis = input("Masukkan Nis Siswa : ")
    nama = input("Masukkan Nama Siswa : ")
    sex = input("Masukkan Gender Siswa : ")
    tgl_lahir = input("Masukkan Tanggal Lahir Siswa : ")
    tempat_lahir = input("Masukkan Tempat Lahir Siswa : ")
    kelas = input("Masukkan Kelas Siswa : ")
    tbl_jurusan_id = input("Masukkan Jurusan Siswa : ")

    # metode exception
    try:
        # simpan query mysql
        sql = "INSERT INTO tbl_siswa VALUES ('%s','%s','%s','%s', '%s', '%s', '%s')" % (
            nis, nama, sex, tgl_lahir, tempat_lahir, kelas, tbl_jurusan_id)
        # mengeksekusi query
        cursor.execute(sql)
        # commit perubahan di database
        db.commit()
    except:
        # kembalikan jika seandainya ada kesalahan
        db.rollback()

    # disconnect from database
    db.close()


def show_siswa():
    # fungsi menampilkan data siswa
    # untuk menyimpan data yang sudah di tambahkan
    data_siswa = []

    # open database connection
    db = connect_db()

    # persiapkan objek kursor menggunakan metode kursor ()
    cursor = db.cursor()

    # mengeksekusi query SQL menggunakan metode execute ()
    cursor.execute("SELECT * FROM tbl_siswa")

    # ambil semua data menggunakan metode fetchall ()
    siswas = cursor.fetchall()

    # pengambilan data siswa
    for siswa in siswas:
        nim = siswa[0]
        nama = siswa[1]
        gender = siswa[2]
        tgl_lahir = siswa[3]
        tempat_lahir = siswa[4]
        kelas = siswa[5]
        jurusan = siswa[6]

        # data dibungkus dalam list
        data = {
            "nim": nim,
            "nama": nama,
            "gender": gender,
            "tgl_lahir": tgl_lahir,
            "tempat_lahir": tempat_lahir,
            "kelas": kelas,
            "tbl_jurusan_id": jurusan,
        }
        # tambah data siswa
        data_siswa.append(data)

    # tampilkan siswa ( di luar for penempatan print nya)
    # print(data_siswa)
    print(json.dumps(obj=data_siswa, sort_keys=True, indent=4))

    # disconnect from database
    db.close()


def delete_siswa():
    # fungsi hapus data siswa
    # open database connection
    db = connect_db()

    # persiapkan objek kursor menggunakan metode kursor ()
    cursor = db.cursor()

    # hapus siswa dengan menggunakan nis
    nis = input("Masukkan NIS Siswa : ")

    # metode exception
    try:
        # simpan query mysql
        sql = "DELETE from tbl_siswa WHERE nis = %s" % nis
        # mengeksekusi query
        cursor.execute(sql)
        # commit perubahan di database
        db.commit()
    except:
        # kembalikan jika seandainya ada kesalahan
        db.rollback()

    # disconnect from database
    db.close()


def update_siswa():
    # fungsi ubah data siswa
    # open database connection
    db = connect_db()

    # persiapkan objek kursor menggunakan metode kursor ()
    cursor = db.cursor()

    # Ubah data berdasarkan :
    nis = input("Masukkan Nis Siswa : ")
    nama = input("Masukkan Nama Siswa : ")
    sex = input("Masukkan Gender Siswa : ")
    tgl_lahir = input("Masukkan Tanggal Lahir Siswa : ")
    tempat_lahir = input("Masukkan Tempat Lahir Siswa : ")
    kelas = input("Masukkan Kelas Siswa : ")
    tbl_jurusan_id = input("Masukkan Jurusan Siswa : ")

    try:
        # simpan query mysql
        sql = "UPDATE tbl_siswa SET nama='%s', gender='%s', tgl_lahir='%s', tempat_lahir='%s', kelas='%s', tbl_jurusan_id='%s' WHERE nis='%s'" % (
            nama, sex, tgl_lahir, tempat_lahir, kelas, tbl_jurusan_id, nis)
        # mengeksekusi query
        cursor.execute(sql)
        # commit perubahan di database
        db.commit()
    except OperationalError as o:
        # untuk cek jika sintaks error
        print(o)
        db.rollback()
    except ProgrammingError as o:
        # untuk cek jika pengambilan data ke database terjadi error
        print(o)
        db.rollback()

    # disconnect from database
    db.close()


if __name__ == "__main__":
    """
    # ini digunakan untuk tes setiap fungsi dalam pembuatan awal fungsi satu persatu
    insert_siswa()
    show_siswa()
    delete_siswa()
    update_siswa()
    """
    # menampilkan program
    print("Library Siswa")
    # daftar menu
    menus = [
        "1. Tambah Siswa",
        "2. Tampilkan Siswa",
        "3. Hapus Siswa",
        "4. Ubah Siswa",
        "5. Keluar"
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
            insert.siswa()
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
        else:
            print("Sampai jumpa kembali... :-D")
            # exit code=0 artinya program keluar dengan benar/tidak terjadi error
            # exit code=1 artinya program keluar tidak semestinya/error
            exit(code=0)
