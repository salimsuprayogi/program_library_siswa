# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

from db_connector import connect_db as dbpy
import json
from pymysql import OperationalError, ProgrammingError


def insert_pertanyaan():
    db = dbpy()
    cursor = db.cursor()

    no_id = input("Masukkan No Id Pertanyaan Siswa : ")
    pertanyaan = input("Masukkan Pertanyaan Siswa : ")
    deskripsi = input("Masukkan Deskripsi Pertanyaan Siswa : ")

    try:
        sql = "INSERT INTO tbl_pertanyaan VALUES ('%s', '%s', '%s')" % (
            no_id, pertanyaan, deskripsi)
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()


def show_pertanyaan():
    semua_pertanyaan = []

    db = dbpy()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_pertanyaan")
    tanya = cursor.fetchall()

    for tanyas in tanya:
        no_id = tanyas[0]
        pertanyaan = tanyas[1]
        deskripsi = tanyas[2]
        # print(no_id)
        # print(pertanyaan)
        # print(deskripsi)

        data_tanyas = {
            "id": no_id,
            "pertanyaan": pertanyaan,
            "deskripsi": deskripsi,
        }

        semua_pertanyaan.append(data_tanyas)

    print(json.dumps(obj=semua_pertanyaan, sort_keys=True, indent=4))

    db.close()


def delete_pertanyaan():
    db = dbpy()
    cursor = db.cursor()

    no_id = input("Masukkan No Id Pertanyaan : ")

    try:
        sql = "DELETE FROM tbl_pertanyaan WHERE id='%s'" % no_id
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()


def update_pertanyaan():
    db = dbpy()
    cursor = db.cursor()

    no_id = input("Masukkan No Id Pertanyaan Siswa : ")
    pertanyaan = input("Masukkan Pertanyaan Siswa : ")
    deskripsi = input("Masukkan Deskripsi Pertanyaan Siswa : ")

    try:
        sql = "UPDATE tbl_pertanyaan SET pertanyaan='%s', deskripsi='%s' WHERE id='%s'" % (
            pertanyaan, deskripsi, no_id)
        cursor.execute(sql)
        db.commit()
    except OperationalError as p:
        print(p)
        db.rollback()
    except ProgrammingError as p:
        print(p)
        db.rollback()

    db.close()


# if __name__ == "__main__":
    # insert_pertanyaan()
    # show_pertanyaan()
    # delete_pertanyaan()
    # update_pertanyaan()
