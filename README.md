# 🧪 Aplikasi Web Tabel Periodik (Flask + SQLite)

Ini adalah aplikasi web edukatif sederhana yang dibuat dengan **Flask** untuk menampilkan unsur-unsur kimia dari tabel periodik. Aplikasi ini menggunakan database **SQLite** dan mengikuti arsitektur **MVC (Model-View-Controller)**.

---

## 🚀 Fitur

- Menampilkan semua unsur kimia dari tabel periodik.
- Melihat detail setiap unsur dengan mengklik tautannya.
- Tampilan rapi menggunakan HTML + CSS (gaya kartu).
- Data dimuat dari file JSON lalu disimpan ke SQLite.
- Mengikuti struktur MVC (memisahkan model, view, dan controller).

---

## 🌱 Seed_db.py
 - Script untuk membaca file element.json dan mengisi (seed) data ke dalam database elements.db menggunakan SQLAlchemy.

## 💻 Yang perlu diinstal
 - pip install flask flask_sqlalchemy

## 💻 Pengisian database
 - python seed_db.py

![Screenshot 2025-05-30 232446](https://github.com/user-attachments/assets/9051904e-5ba8-49c4-aef8-3150a16f4a70)
