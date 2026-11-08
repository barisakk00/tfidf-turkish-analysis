# İlerleme Kaydı

## v0.1.0 - 2026-11-08

- TRSAv1 veri seti incelendi; eksik/boş kayıtlar, çelişkili etiketler ve yinelenen yorum-etiket çiftleri ele alındı.
- Veri katmanlı olarak %70 eğitim, %15 validation, %15 test kümelerine ayrıldı.
- Kelime unigram/bigram TF-IDF + Logistic Regression baseline modeli kuruldu.
- Validation sonucu: accuracy 0.801990, macro F1 0.800560.
- Terminal tahmin arayüzü ve `models/tfidf_v0.1.joblib` modeli eklendi.

## v1.0.0 - 2026-11-08

### Eklenenler ve İyileştirmeler

- Baseline, kelime + karakter TF-IDF ve kelime + karakter + emoji TF-IDF modelleri karşılaştırıldı.
- Karakter özellikleri `char_wb` analyzer ile (3, 5) n-gram aralığında eklendi; `max_features=300000` ile boyut sınırlandı.
- Emojiler korunarak ayrı TF-IDF kolunda (1, 3) n-gram aralığıyla temsil edildi.
- 3 katlı `StratifiedKFold` ile 8 ayar senaryosu macro F1’e göre karşılaştırıldı: 24 çapraz doğrulama eğitimi ve en iyi model için bir yeniden eğitim.
- Seçilen ayarlar: Logistic Regression `C=1.0`; kelime n-gram `(1, 3)`, `min_df=2`; karakter n-gram `(3, 5)`, `min_df=3`; emoji n-gram `(1, 3)`, `min_df=2`.
- Seçilen pipeline, train ve validation kümelerinin birleşimi üzerinde yeniden eğitildi ve `models/tfidf_v1.0.joblib` dosyasına kaydedildi.
- Terminal arayüzü v1.0 model dosyasını kullanacak şekilde güncellendi.

### Doğrulama ve Test Sonuçları

- En iyi CV macro F1 ortalaması: 0.805857.
- Validation (21.009 örnek): accuracy 0.808939, macro F1 0.807661.
- Test (21.010 örnek; model seçimi tamamlandıktan sonra bir kez): accuracy 0.813232, macro F1 0.812124.
- Test sınıf F1 değerleri: Negatif 0.848099, Nötr 0.734394, Pozitif 0.853879.
- Nötr sınıfı en zayıf sınıf olmaya devam ediyor.
- Terminal smoke test: `Ürün harika 😍` Pozitif (%96,4) tahmin edildi; `q` ile çıkış çalıştı.

### Veri ve Lisans Durumu

- Temizleme sonrasında 140.063 kayıt kaldı; çelişkili etiketli 6.883 satır modelden çıkarıldı, 3.054 yinelenen yorum-etiket satırı kaldırıldı.
- Hugging Face veri seti sayfasında lisans belirtilmiyor. Depo özel tutuluyor; veri/modelin kamuya açık yeniden dağıtımı kullanım hakları incelenene kadar beklemede.

### Sonraki İşler

- Nötr sınıfındaki hataları confusion matrix ve örnek incelemesiyle analiz etmek.
- Kamuya açık dağıtımdan önce veri ve model kullanım haklarını netleştirmek.
