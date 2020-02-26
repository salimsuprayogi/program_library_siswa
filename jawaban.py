# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

from db_connector import connect_db as dbpy
import json
from pymysql import OperationalError, ProgrammingError


def insert_jawaban():
    db = dbpy()
    cursor = db.cursor()

    no_id = input("Masukan No Id Jawaban : ")
    nis = input("Masukan Nis Siswa : ")
    pertanyaan_id = input("Masukan No Id Pertanyaan Siswa : ")
    jawaban = input("Masukan Jawaban Siswa : ")

    try:
        sql = "INSERT INTO tbl_jawaban VALUES ('%s', '%s', '%s','%s')" % (
            no_id, nis, pertanyaan_id, jawaban)
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()


def show_jawaban():
    jawaban_semua = []
    db = dbpy()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_jawaban")

    jawaban_siswa = cursor.fetchall()

    for jawabans in jawaban_siswa:
        no_id = jawabans[0]
        nis = jawabans[1]
        pertanyaan_id = jawabans[2]
        jawaban = jawabans[3]

        jawaban_total = {
            "id": no_id,
            "nis": nis,
            "pertanyaan": pertanyaan_id,
            "jawaban": jawaban,
        }

        jawaban_semua.append(jawaban_total)
    
    print(json.dumps(obj=jawaban_semua, sort_keys=4, indent=True))

    db.close()


def delete_jawaban():
    db = dbpy()
    cursor = db.cursor()

    no_id = input("Masukan No Id Jawaban : ")

    try:
        sql = "DELETE FROM tbl_jawaban WHERE id='%s'" % no_id
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()


def update_jawaban():
    db = dbpy()
    cursor = db.cursor()

    no_id = input("Masukan No Id Jawaban : ")
    nis = input("Masukan Nis Siswa : ")
    pertanyaan_id = input("Masukan No Id Pertanyaan Siswa : ")
    jawaban = input("Masukan Jawaban Siswa : ")

    try:
        sql = "UPDATE tbl_jawaban SET tbl_siswa_nis='%s',tbl_pertanyaan_id='%s', jawaban='%s' WHERE id='%s'" % (
            nis, pertanyaan_id, jawaban, no_id)
        cursor.execute(sql)
        db.commit()
    except OperationalError as j:
        print(j)
        db.rollback()
    except ProgrammingError as j:
        print(j)
        db.rollback()

    db.close()


# if __name__ == "__main__":
    # insert_jawaban()
    # show_jawaban()
    # delete_jawaban()
    # update_jawaban()
