import pymysql

def buat_koneksi():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='irham344nahrul',
            database='distro'
        )
        print("Koneksi ke database BERHASIL")
        return conn
    except Exception as e:
        print("Koneksi database GAGAL:", e)
        return None
