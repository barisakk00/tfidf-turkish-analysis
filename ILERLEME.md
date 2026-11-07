# İlerleme Kaydı

## v0.1.0 - 2026-11-08

- 70/15/15 eğitim, doğrulama ve test bölünmesi.
- Katmanlı bölme için 140.063 kayıt kaldı.

### Doğrulama Sonuçları

- Doğrulama kümesi: 21.009 örnek.
- Accuracy: 0.80199.
- Makro F1: 0.80056.
- Sınıf bazında F1: Negatif 0.84106, Nötr 0.71879, Pozitif 0.84183.
- Ayrılmış test kümesi henüz değerlendirilmedi.
- Terminal denemesinde `Harika ürün çok güzel` metni, model olasılığı %93,2 ile Pozitif tahmin edildi; `q` ile çıkış çalıştı.

### Sonraki İşler

- Eğitim verisi üzerinde çapraz doğrulama ile model parametrelerini ayarlamak.
- Kelime ve karakter TF-IDF özelliklerini, emoji özelliklerini ve duygu sözlüğü özelliklerini karşılaştırmak.
- Seçilen modeli ayrılmış test kümesinde bir kez değerlendirmek.
- Kamuya açık dağıtımdan önce veri kümesi ve modelin kullanım/dağıtım koşullarını netleştirmek.
