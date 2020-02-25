# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

from db_connector import connect_db as dbpy
import json
from pymysql import OperationalError, ProgrammingError


def insert_jurusan():
    db = dbpy()
    cursor = db.cursor()

    no_id = input("Masukkan No Id Jurusan : ")
    jurusan = input("Masukkan Nama Jurusan : ")
    deskripsi = input("Masukkan Deskripsi Jurusan : ")

    try:
        sql = "INSERT INTO tbl_jurusan VALUES ('%s', '%s','%s')" % (
            no_id, jurusan, deskripsi)
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()


def show_jurusan():
    semua_jurusan = []

    db = dbpy()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_jurusan")
    data_jurusan = cursor.fetchall()

    for hasil_jurusan in data_jurusan:
        no_id = hasil_jurusan[0]
        jurusan = hasil_jurusan[1]
        deskripsi = hasil_jurusan[2]

        total_jurusan = {
            "no_id": no_id,
            "jurusan": jurusan,
            "deskripsi": deskripsi
        }

        semua_jurusan.append(total_jurusan)

    print(json.dumps(obj=semua_jurusan, sort_keys=True, indent=4))

    db.close()


def delete_jurusan():
    db = dbpy()
    cursor = db.cursor()

    no_id = input("Masukan ID Jurusan : ")

    try:
        sql = "DELETE from tbl_jurusan WHERE id = '%s'" % no_id
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()


def update_jurusan():
    db = dbpy()
    cursor = db.cursor()

    no_id = input("Masukkan No Id Jurusan : ")
    jurusan = input("Masukkan Nama Jurusan : ")
    deskripsi = input("Masukkan Deskripsi Jurusan : ")

    try:
        sql = "UPDATE tbl_jurusan SET jurusan='%s', deskripsi='%s' WHERE id='%s'" % (
            jurusan, deskripsi, no_id)
        cursor.execute(sql)
        db.commit()
    except OperationalError as u:
        print(u)
        db.rollback()
    except ProgrammingError as u:
        print(u)
        db.rollback()

    db.close()

# ini untuk pengecekan kode pada file jurusan
# if __name__ == "__main__":
    # insert_jurusan()
    # show_jurusan()
    # delete_jurusan()
    # update_jurusan()
