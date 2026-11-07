# İlerleme Kaydı

## v0.1.0 - 2026-11-08

### Eklenenler

- 150.000 etiketli Türkçe incelemeden oluşan Hugging Face TRSAv1 veri kümesini yükleme ve keşifsel veri analizi.
- Baştaki ve sondaki boşlukları temizleme, boş kayıtları çıkarma, çelişkili etiketli incelemeleri temel model dışında tutma ve yinelenen inceleme-etiket çiftlerini tekilleştirme.
- Katmanlı 70/15/15 eğitim, doğrulama ve test bölünmesi.
- Lojistik Regresyon ile kelime düzeyinde TF-IDF tekli ve ikili sözcük öbekleri.
- `models/tfidf_v0.1.joblib` konumuna kaydedilmiş model hattı ve `src/predict_cli.py` terminal tahmin arayüzü.
- İki dilli proje belgeleri ve sabitlenmiş doğrudan bağımlılıklar.

### Doğrulama Sonuçları

- Doğrulama örneği: 21.009.
- Doğruluk (accuracy): 0.80199.
- Makro F1: 0.80056.
- Sınıf bazında F1: Negatif 0.84106, Nötr 0.71879, Pozitif 0.84183.
- Ayrılmış test kümesi henüz değerlendirilmedi.
- Terminal denemesinde `Harika ürün çok güzel` metni, model olasılığı %93,2 ile Pozitif tahmin edildi; `q` ile çıkış çalıştı.

### Veri İşleme

- Çelişkili etiket içeren 891 inceleme grubu (toplam 6.883 satır) inceleme için ayrıldı ve temel modelden çıkarıldı.
- Yinelenen 3.054 inceleme-etiket satırı kaldırıldı.
- Katmanlı bölme için 140.063 kayıt kaldı.
- Kaynak veri kümesinin kartında lisans belirtilmiyor. Veri kümesinin veya eğitilmiş modelin kamuya açık dağıtımı, kullanım hakları incelenene kadar beklemede.

### Sonraki İşler

- Kelime ve karakter TF-IDF özelliklerini karşılaştırmak, emoji özelliklerinin katkısını ölçmek.
- Eğitim verisi üzerinde çapraz doğrulama ile model parametrelerini ayarlamak.
- Seçilen modeli ayrılmış test kümesinde bir kez değerlendirmek.
- Kamuya açık dağıtımdan önce veri kümesi ve modelin kullanım/dağıtım koşullarını netleştirmek.
