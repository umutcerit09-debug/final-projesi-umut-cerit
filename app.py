import pandas as pd

# 1. Veri Setini Yükleme
print("Veri seti yükleniyor...")
df = pd.read_csv('telco_churn.csv')

# 2. Veri Temizleme (Data Cleaning)
# TotalCharges sütununda boşluk karakterleri var, onları NaN yapıp float tipine çeviriyoruz
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Eksik verileri (NaN) olan satırları siliyoruz
df.dropna(inplace=True)

# Gereksiz müşteri ID sütununu modelden çıkarıyoruz (Öğrenmeye bir katkısı yok)
df.drop('customerID', axis=1, inplace=True)

print("Veri temizleme başarıyla tamamlandı!")
print(f"Toplam kullanılabilir müşteri verisi sayısı: {len(df)}")