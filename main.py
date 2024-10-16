import pdfplumber
import pandas as pd

def extract_table_pdfplumber(pdf_path, excel_path):
    # Membuka file PDF
    with pdfplumber.open(pdf_path) as pdf:
        tables = []
        # Loop untuk setiap halaman PDF
        for page in pdf.pages:
            # Ekstrak tabel dari halaman PDF
            table = page.extract_table()
            if table:
                tables.append(table)

        # Konversi tabel ke DataFrame dan simpan ke Excel
        if tables:
            # Mengubah list menjadi DataFrame
            df = pd.DataFrame(tables[0][1:], columns=tables[0][0])
            df.to_excel(excel_path, index=False)
            print(f"Tabel berhasil diekstrak ke {excel_path}")
        else:
            print("Tidak ada tabel yang ditemukan dalam file PDF.")

# Contoh penggunaan
pdf_path = "contoh.pdf"  # Ganti dengan path file PDF
excel_path = "hasil_tabel.xlsx"  # Ganti dengan path file hasil Excel
extract_table_pdfplumber(pdf_path, excel_path)
