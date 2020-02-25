# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

# untuk import fungsi connector database mywql
from db_connector import connect_db as dbpy
# import json untuk menampilkan di terminal menjadi rapi / nyaman di baca
import json
# import OperationalError dan ProgrammingError untuk exception
from pymysql import OperationalError, ProgrammingError


def insert_siswa():
    # fungsi tambah siswa
    # open database connection
    db = dbpy()

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
    db = dbpy()

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
    db = dbpy()

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
    db = dbpy()

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
