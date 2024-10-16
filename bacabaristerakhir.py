import pandas as pd

# Baca file Excel
# Ganti 'data.xlsx' dengan path ke file Excel kamu
df = pd.read_excel('hasil_tabel.xlsx', header=3)

# Menampilkan DataFrame
print("DataFrame:")
print(df)

# Mengambil nilai di baris terakhir dari kolom 'Nilai'
total_jumlah_transaksi_qr = df['A'].iloc[-3]
total_nominal_transaksi_qr = df['B'].iloc[-3]
total_fee_transaksi_qr = df['C'].iloc[-3]
total_net_kewajiban = df['S= N+O+Q'].iloc[-2]
total_net_hak = df['T= G+P+R'].iloc[-2]
total_settlement = df['S= N+O+Q'].iloc[-1]


print(f"\nNilai di baris terakhir dari kolom 'total jumlah transaksi qr': {total_jumlah_transaksi_qr}")
print(f"\nNilai di baris terakhir dari kolom 'total nominal transaksi qr': {total_nominal_transaksi_qr}")
print(f"\nNilai di baris terakhir dari kolom 'total fee transaksi qr': {total_fee_transaksi_qr}")
print(f"\nNilai di baris terakhir dari kolom 'total net kewajiban': {total_net_kewajiban}")
print(f"\nNilai di baris terakhir dari kolom 'total net hak': {total_net_hak}")
print(f"\nNilai di baris terakhir dari kolom 'total settlement': {total_settlement}")
