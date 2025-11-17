from flask import Flask, request, jsonify
from config import buat_koneksi

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Selamat Datang di API Barang</h1>'

# ==================================================
# BACA DATA
# ==================================================
@app.route('/baca_data', methods=['GET'])
def baca_data():
    try:
        conn = buat_koneksi()
        if conn is None:
            return jsonify({"error": "Koneksi database gagal"}), 500

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM barang")
        hasil = cursor.fetchall()
        cursor.close()
        conn.close()

        data = []
        for row in hasil:
            data.append({
                "id_barang": row[0],
                "nama_barang": row[1],
                "harga_barang": row[2]
            })

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================================================
# TAMBAH DATA
# ==================================================
@app.route('/tambah_data', methods=['POST'])
def tambah_data():
    try:
        id_barang = request.form.get('id_barang')
        nama_barang = request.form.get('nama_barang')
        harga_barang = request.form.get('harga_barang')

        conn = buat_koneksi()
        cursor = conn.cursor()
        sql = "INSERT INTO barang (id_barang, nama_barang, harga_barang) VALUES (%s, %s, %s)"
        cursor.execute(sql, (id_barang, nama_barang, harga_barang))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"pesan": "Data berhasil ditambahkan!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================================================
# EDIT DATA
# ==================================================
@app.route('/edit/<id_barang>', methods=['POST'])
def edit_data(id_barang):
    try:
        nama_barang = request.form.get('nama_barang')
        harga_barang = request.form.get('harga_barang')

        conn = buat_koneksi()
        cursor = conn.cursor()
        sql = "UPDATE barang SET nama_barang=%s, harga_barang=%s WHERE id_barang=%s"
        cursor.execute(sql, (nama_barang, harga_barang, id_barang))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"pesan": "Data berhasil diubah!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================================================
# HAPUS DATA
# ==================================================
@app.route('/hapus/<id_barang>', methods=['DELETE'])
def hapus_data(id_barang):
    try:
        conn = buat_koneksi()
        cursor = conn.cursor()
        sql = "DELETE FROM barang WHERE id_barang=%s"
        cursor.execute(sql, (id_barang,))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"pesan": "Data berhasil dihapus!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
