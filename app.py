import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Veri Setini Yükleme
print("Veri seti yükleniyor...")
df = pd.read_csv('telco_churn.csv')

# 2. Veri Temizleme (Data Cleaning)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)
df.drop('customerID', axis=1, inplace=True)

print("Veri temizleme başarıyla tamamlandı!")
print(f"Toplam kullanılabilir müşteri verisi sayısı: {len(df)}")

# 3. Veri Ön İşleme
print("Veriler makine öğrenmesi için hazırlanıyor...")
le = LabelEncoder()

# Sayısal olmayan (number) TÜM sütunları bul, metne çevir ve sayısal kodlara (0, 1, 2...) dönüştür:
for col in df.select_dtypes(exclude=['number']).columns:
    df[col] = le.fit_transform(df[col].astype(str))

# Hedef değişken ve özellikleri ayırma
X = df.drop('Churn', axis=1)
y = df['Churn']

# Eğitim ve test verilerini ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model Eğitimi ve Karşılaştırması
print("Modeller eğitiliyor (Lojistik Regresyon vs Random Forest)...")

# Model 1: Lojistik Regresyon
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
log_pred = log_model.predict(X_test)
log_acc = accuracy_score(y_test, log_pred)

# Model 2: Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)

# Overfitting Kontrolü
rf_train_acc = accuracy_score(y_train, rf_model.predict(X_train))

print("-" * 30)
print(f"Lojistik Regresyon Test Doğruluğu: %{log_acc * 100:.2f}")
print(f"Random Forest Test Doğruluğu: %{rf_acc * 100:.2f}")
print(f"Random Forest Eğitim Doğruluğu: %{rf_train_acc * 100:.2f} (Overfitting kontrolü)")
print("-" * 30)