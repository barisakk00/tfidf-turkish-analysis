# TF-IDF Turkish Sentiment Analysis

[English](#english) | [Türkçe](#türkçe)

## English

An educational machine learning project that classifies Turkish product reviews as positive, negative, or neutral. The final pipeline combines word, character, and emoji TF-IDF features with Logistic Regression.

### Dataset

The project uses [TRSAv1 on Hugging Face](https://huggingface.co/datasets/maydogan/Turkish_SentimentAnalysis_TRSAv1), a dataset of 150,000 Turkish reviews with `review` text and `score` label fields. The dataset is loaded with `datasets.load_dataset`; its data files are not stored in this repository.

The dataset card cites Aydoğan and Kocaman, “TRSAv1: A new benchmark dataset for classifying user reviews on Turkish e-commerce websites,” *Journal of Information Science* (2022), [doi:10.1177/01655515221074328](https://doi.org/10.1177/01655515221074328). The dataset page does not specify a license. This GitHub repository is private; do not redistribute the dataset or model until applicable rights are clarified.

### Project Workflow

- Inspect labels, missing values, text lengths, duplicates, and conflicting labels.
- Trim surrounding whitespace, remove blank or missing records, exclude conflicting-label reviews from model training, and remove duplicate review-label pairs.
- Split the remaining 140,063 records into stratified train, validation, and test sets at 70%, 15%, and 15%.
- Compare word-only, word-plus-character, and word-plus-character-plus-emoji TF-IDF models.
- Tune a compact set of model parameters using 3-fold `StratifiedKFold` on training data only. Eight explicit candidates are compared with macro F1; validation is used to assess the selected settings.
- Refit the selected pipeline on train plus validation data, then evaluate once on the held-out test set.
- Inspect validation errors and compare a balanced class-weight experiment without revisiting the test set.
- Use the saved pipeline through the terminal for single reviews or line-by-line TXT batches exported to XLSX.

### Current Model

Version `v1.0.0` uses:

- Word TF-IDF with n-grams `(1, 3)`, `min_df=2`, and `sublinear_tf=True`.
- Character TF-IDF with `analyzer="char_wb"`, n-grams `(3, 5)`, `min_df=3`, `max_features=300000`, and `sublinear_tf=True`.
- An emoji TF-IDF feature branch with emoji n-grams `(1, 3)`, `min_df=2`, and `sublinear_tf=True`.
- `LogisticRegression(C=1.0, max_iter=1000, random_state=42)`.

The selected settings achieved mean cross-validation macro F1 of `0.805857` across three folds. The final fitted pipeline, trained on train plus validation data, is stored at `models/tfidf_v1.0.joblib`.

### Evaluation Metrics

The selected settings achieved validation accuracy `0.808939` and macro F1 `0.807661`. The held-out test set was evaluated once after model selection:

| Metric | Validation | Test |
|---|---:|---:|
| Examples | 21,009 | 21,010 |
| Accuracy | 0.808939 | 0.813232 |
| Macro F1 | 0.807661 | 0.812124 |
| Negative F1 | 0.846851 | 0.848099 |
| Neutral F1 | 0.727447 | 0.734394 |
| Positive F1 | 0.848686 | 0.853879 |

Neutral remains the weakest class. These results describe this dataset and split; they do not guarantee performance on other Turkish text domains.

### Validation Error Analysis

The tuned model made 4,014 incorrect predictions among 21,009 validation examples. The most frequent confusions were Neutral → Positive (1,061), Negative → Neutral (968), Positive → Neutral (857), and Neutral → Negative (812). The notebook includes a review queue with 10 high-confidence errors per true/predicted class pair; labels are not changed automatically.

An exploratory `class_weight="balanced"` fit on the training split achieved validation accuracy `0.807559`, macro F1 `0.806569`, and Neutral F1 `0.726740`. The default tuned model scored `0.808939`, `0.807661`, and `0.727447` respectively, so balanced weights were not selected. These comparisons use validation data only; the held-out test set remains reserved for final evaluation.

### Installation and Usage

Use Python 3.14 and run these commands from the project root:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Open `notebooks/turkish_sentiment_analysis.ipynb` in Jupyter or VS Code and run its cells in order to reproduce the workflow and save the model. Start the terminal interface with:

```powershell
.\.venv\Scripts\python.exe src\predict_cli.py
```

Choose `1` for a single review or `2` to classify a TXT file. Put one review on each line, enter the TXT path, and optionally enter an XLSX output path. Leaving the output path empty saves `<filename>_tahminler.xlsx` beside the TXT file. The spreadsheet includes the source line number, review, predicted sentiment, confidence, and class probabilities. Enter `q` in the menu to exit.

### Project Status

`v1.1.0` builds on the `v1.0.0` model and adds validation error analysis plus TXT-to-XLSX batch prediction in the terminal interface. The fitted model artifact and its reported evaluation metrics remain those of `v1.0.0`; this release does not claim a new model-performance improvement. The repository remains private because the upstream dataset page does not state a license. Public redistribution is pending a rights review.

### License

No software license has been selected for this project. The upstream dataset page does not specify a license, and redistribution rights for the dataset and trained model have not been established. Do not redistribute the dataset or model until applicable terms are clarified.

### Developer

Baris AK

Artificial Intelligence and Data Engineering Student

## Türkçe

Türkçe ürün yorumlarını pozitif, negatif veya nötr olarak sınıflandıran bir makine öğrenmesi öğrenme projesidir. Son pipeline, kelime, karakter ve emoji TF-IDF özelliklerini Logistic Regression ile birleştirir.

### Veri Seti

Proje, `review` metin ve `score` etiket alanlarına sahip 150.000 Türkçe yorumdan oluşan [Hugging Face TRSAv1 veri setini](https://huggingface.co/datasets/maydogan/Turkish_SentimentAnalysis_TRSAv1) kullanır. Veri `datasets.load_dataset` ile yüklenir; veri dosyaları bu depoda tutulmaz.

Veri seti kartında Aydoğan ve Kocaman’ın “TRSAv1: A new benchmark dataset for classifying user reviews on Turkish e-commerce websites” başlıklı, *Journal of Information Science* dergisinde 2022’de yayımlanan çalışmasına [doi:10.1177/01655515221074328](https://doi.org/10.1177/01655515221074328) atıf yapılır. Veri seti sayfasında lisans belirtilmemiştir. Bu GitHub deposu özeldir; kullanım hakları netleşene kadar veri setini veya modeli yeniden dağıtma.

### Proje Akışı

- Etiketleri, eksik değerleri, metin uzunluklarını, tekrarları ve çelişkili etiketleri inceleme.
- Baştaki ve sondaki boşlukları temizleme, boş veya eksik kayıtları çıkarma, çelişkili etiketli yorumları model eğitiminden hariç tutma ve yinelenen yorum-etiket çiftlerini kaldırma.
- Kalan 140.063 kaydı sınıf oranlarını koruyarak %70 train, %15 validation ve %15 test olarak ayırma.
- Yalnızca kelime, kelime + karakter ve kelime + karakter + emoji TF-IDF modellerini karşılaştırma.
- Eğitim verisi üzerinde 3 katlı `StratifiedKFold` ile sınırlı sayıda model ayarını macro F1’e göre karşılaştırma; seçilen ayarları validation kümesinde değerlendirme.
- Seçilen pipeline’ı train ve validation verilerinin birleşiminde yeniden eğitme, ardından ayrılmış test kümesinde bir kez değerlendirme.
- Test kümesini yeniden kullanmadan validation hatalarını inceleme ve sınıf ağırlıklı modeli karşılaştırma.
- Kaydedilmiş pipeline’ı terminalde tek yorum veya satır satır TXT dosyasından toplu tahmin için kullanıp sonuçları XLSX’e aktarma.

### Mevcut Model

`v1.0.0` sürümünde kullanılan ayarlar:

- `(1, 3)` n-gram aralığı, `min_df=2` ve `sublinear_tf=True` ile kelime TF-IDF.
- `analyzer="char_wb"`, `(3, 5)` n-gram aralığı, `min_df=3`, `max_features=300000` ve `sublinear_tf=True` ile karakter TF-IDF.
- `(1, 3)` emoji n-gram aralığı, `min_df=2` ve `sublinear_tf=True` ile ayrı emoji TF-IDF kolu.
- `LogisticRegression(C=1.0, max_iter=1000, random_state=42)`.

Seçilen ayarlar, üç katlı çapraz doğrulamada ortalama `0.805857` macro F1 elde etti. Train ve validation verileriyle yeniden eğitilen son pipeline `models/tfidf_v1.0.joblib` konumunda saklanır.

### Değerlendirme Metrikleri

Seçilen ayarlar validation kümesinde `0.808939` accuracy ve `0.807661` macro F1 elde etti. Ayrılmış test kümesi model seçimi tamamlandıktan sonra bir kez değerlendirildi:

| Metrik | Validation | Test |
|---|---:|---:|
| Örnek sayısı | 21.009 | 21.010 |
| Accuracy | 0.808939 | 0.813232 |
| Macro F1 | 0.807661 | 0.812124 |
| Negatif F1 | 0.846851 | 0.848099 |
| Nötr F1 | 0.727447 | 0.734394 |
| Pozitif F1 | 0.848686 | 0.853879 |

Nötr sınıfı diğer sınıflara göre daha zayıftır. Bu sonuçlar yalnızca bu veri seti ve bölünme için geçerlidir; Türkçedeki diğer metin alanlarında aynı performansı garanti etmez.

### Validation Hata Analizi

Ayarlı model 21.009 validation örneğinin 4.014’ünü yanlış sınıflandırdı. En sık karışan çiftler Nötr → Pozitif (1.061), Negatif → Nötr (968), Pozitif → Nötr (857) ve Nötr → Negatif (812) oldu. Notebook’ta her gerçek/tahmin sınıf çifti için güveni yüksek 10 hata içeren bir inceleme tablosu bulunur; etiketler otomatik değiştirilmez.

Train kümesinde eğitilen deneme `class_weight="balanced"` modeli validation’da `0.807559` accuracy, `0.806569` macro F1 ve `0.726740` Nötr F1 aldı. Varsayılan ayarlı modelin değerleri sırasıyla `0.808939`, `0.807661` ve `0.727447` olduğundan dengeli sınıf ağırlıkları seçilmedi. Karşılaştırma yalnızca validation verisini kullanır; ayrılmış test kümesi nihai değerlendirme için korunur.

### Kurulum ve Kullanım

Python 3.14 kullan ve komutları proje kök dizininde çalıştır:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

İş akışını tekrarlamak ve modeli kaydetmek için `notebooks/turkish_sentiment_analysis.ipynb` dosyasını Jupyter veya VS Code’da açıp hücreleri sırayla çalıştır. Terminal arayüzünü şu komutla başlat:

```powershell
.\.venv\Scripts\python.exe src\predict_cli.py
```

`1` ile tek yorum, `2` ile TXT dosyası seç. Her satıra bir yorum yaz; TXT yolunu gir ve istersen XLSX çıktı yolunu belirt. Çıktı yolu boş bırakılırsa dosya, TXT’nin yanına `<dosyaadı>_tahminler.xlsx` adıyla kaydedilir. Tabloda kaynak satır numarası, yorum, tahmin, güven ve sınıf olasılıkları yer alır. Menüden çıkmak için `q` yaz.

### Proje Durumu

`v1.1.0`, `v1.0.0` modelinin üzerine validation hata analizini ve terminal arayüzünde TXT’den XLSX’e toplu tahmini ekler. Eğitilmiş model dosyası ve raporlanan değerlendirme metrikleri `v1.0.0` sürümündekiyle aynıdır; bu sürüm yeni bir model performansı artışı iddia etmez. Kaynak veri seti sayfasında lisans belirtilmediği için depo özel tutulmaktadır. Kamuya açık dağıtım, kullanım hakları incelenene kadar beklemededir.

### Lisans

Bu proje için henüz yazılım lisansı seçilmemiştir. Kaynak veri seti sayfasında lisans belirtilmemiş, veri setinin ve eğitilmiş modelin yeniden dağıtım hakları netleştirilmemiştir. İlgili koşullar açıklığa kavuşana kadar veri setini veya modeli yeniden dağıtma.

### Geliştirici

Baris AK

Artificial Intelligence and Data Engineering Student
