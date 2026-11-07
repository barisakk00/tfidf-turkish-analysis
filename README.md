# Turkish Sentiment Analysis

[English](#english) | [Türkçe](#türkçe)

## English

An educational machine learning project that classifies Turkish product reviews as positive, negative, or neutral using a TF-IDF and Logistic Regression pipeline.

### Installation and Usage

Use Python 3.14 and run these commands from the project root:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Open `notebooks/turkish_sentiment_analysis.ipynb` in Jupyter or VS Code and run its cells in order. The final model-save cell writes the fitted pipeline under `models/`.

### Dataset

The project uses [TRSAv1 on Hugging Face](https://huggingface.co/datasets/maydogan/Turkish_SentimentAnalysis_TRSAv1), which provides 150,000 Turkish reviews across three sentiment labels. The source dataset has `review` text and `score` label fields. It is loaded with `datasets.load_dataset`; dataset files are not included in this repository.

The dataset card references Aydoğan and Kocaman, “TRSAv1: A new benchmark dataset for classifying user reviews on Turkish e-commerce websites,” *Journal of Information Science*, 2022, [doi:10.1177/01655515221074328](https://doi.org/10.1177/01655515221074328). The Hugging Face dataset page does not specify a license. Dataset and model redistribution rights have not been established.

### Project Workflow

- Load the dataset and inspect its schema and labels.
- Explore missing values, text lengths, repeated reviews, and conflicting labels.
- Trim surrounding whitespace, remove blank records, keep conflicting-label records in a separate review set, and exclude them from this baseline. Remove repeated review-label pairs.
- Split the cleaned data into stratified train, validation, and test sets at 70%, 15%, and 15%.
- Train a TF-IDF and Logistic Regression baseline.
- Evaluate on the validation set and reserve the test set for final evaluation.
- Save the fitted pipeline and use it through a terminal prediction interface.

### Current Model

The baseline uses word-level TF-IDF with unigrams and bigrams, `min_df=2`, and sublinear term frequency, followed by `LogisticRegression(max_iter=1000, random_state=42)`. The fitted pipeline is stored at `models/tfidf_v0.1.joblib`.

The terminal interface is `src/predict_cli.py`. After running the notebook’s model-save cell, start it from the project root with:

```powershell
.\.venv\Scripts\python.exe src\predict_cli.py
```

Enter a review at the prompt. Enter `q` to exit.

### Evaluation Metrics

The current validation run used 21,009 reviews and achieved accuracy of 0.80199 and macro F1 of 0.80056. Class F1 scores were 0.84106 for negative, 0.71879 for neutral, and 0.84183 for positive. The test set has not yet been used for evaluation. These results are a baseline and do not represent performance on every Turkish text domain.

### Project Status

Version `v0.1.0` includes dataset exploration, initial cleaning, stratified split, baseline model, validation report, confusion matrix, saved model artifact, and terminal interface. The neutral class is the main area for improvement. Next steps include comparing word and character n-grams, measuring emoji-related features, tuning with cross-validation on training data, and evaluating the selected model once on the reserved test set.

### License

No software license has been selected for this project. The upstream dataset page does not specify a license, and redistribution rights for the dataset and trained model are not established. Do not redistribute the dataset or model until their applicable terms are clarified. Public release is pending this review.

### Developer

Baris AK

Artificial Intelligence and Data Engineering Student

## Türkçe

Türkçe ürün yorumlarını TF-IDF ve Logistic Regression pipeline’ı ile pozitif, negatif veya nötr olarak sınıflandıran bir makine öğrenmesi öğrenme projesidir.

### Installation and Usage

Python 3.14 kullan ve bu komutları proje kök dizininde çalıştır:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

`notebooks/turkish_sentiment_analysis.ipynb` dosyasını Jupyter veya VS Code’da açıp hücreleri sırayla çalıştır. Son model kaydetme hücresi eğitilmiş pipeline’ı `models/` altına yazar.

### Dataset

Proje, üç duygu etiketine sahip 150.000 Türkçe yorum sunan [Hugging Face TRSAv1 veri setini](https://huggingface.co/datasets/maydogan/Turkish_SentimentAnalysis_TRSAv1) kullanır. Kaynak veri setinde metin alanı `review`, etiket alanı `score` olarak adlandırılmıştır. Veri `datasets.load_dataset` ile yüklenir; veri dosyaları bu depoya eklenmez.

Veri seti kartında Aydoğan ve Kocaman’ın “TRSAv1: A new benchmark dataset for classifying user reviews on Turkish e-commerce websites” başlıklı, *Journal of Information Science* dergisinde 2022’de yayımlanan çalışmasına [doi:10.1177/01655515221074328](https://doi.org/10.1177/01655515221074328) atıf yapılır. 

### Project Workflow

- Veri setini yükleme; şemasını ve etiketlerini inceleme.
- Eksik değerleri, metin uzunluklarını, tekrar eden yorumları ve çelişkili etiketleri inceleme.
- Metinlerin başındaki ve sonundaki boşlukları temizleme, boş kayıtları çıkarma, çelişkili etiketli kayıtları ayrı bir inceleme kümesinde tutup bu baseline’dan çıkarma ve yinelenen yorum-etiket çiftlerini kaldırma.
- Temiz veriyi sınıf oranlarını koruyarak %70 train, %15 validation ve %15 test olarak ayırma.
- TF-IDF ve Logistic Regression baseline modelini eğitme.
- Validation kümesinde değerlendirme yapma ve test kümesini son değerlendirme için ayırma.
- Eğitilmiş pipeline’ı kaydetme ve terminal tahmin arayüzünden kullanma.

### Current Model

Baseline; unigram ve bigram kullanan, `min_df=2` ve alt doğrusal terim sıklığı ayarlı kelime tabanlı TF-IDF ile `LogisticRegression(max_iter=1000, random_state=42)` sınıflandırıcısından oluşur. Eğitilmiş pipeline `models/tfidf_v0.1.joblib` konumunda saklanır.

Terminal arayüzü `src/predict_cli.py` dosyasındadır. Notebook’taki model kaydetme hücresini çalıştırdıktan sonra proje kökünde şu komutla başlat:

```powershell
.\.venv\Scripts\python.exe src\predict_cli.py
```

İstem satırına bir yorum yaz. Çıkmak için `q` gir.

### Evaluation Metrics

Mevcut validation çalışmasında 21.009 yorum kullanıldı; accuracy 0.80199, macro F1 0.80056 elde edildi. Sınıf F1 değerleri negatif için 0.84106, nötr için 0.71879 ve pozitif için 0.84183 oldu. Test kümesi henüz değerlendirmede kullanılmadı. Bu sonuçlar başlangıç baseline’ına aittir ve Türkçedeki her metin alanındaki performansı temsil etmez.

### Project Status

`v0.1.0` sürümü veri keşfini, ilk temizliği, stratified split’i, baseline modeli, validation raporunu, confusion matrix’i, kaydedilmiş model dosyasını ve terminal arayüzünü içerir. Geliştirmeye en açık sınıf nötrdür. Sonraki adımlar kelime ve karakter n-gramlarını karşılaştırmak, emoji özelliklerinin katkısını ölçmek, eğitim verisi üzerinde çapraz doğrulamayla ayar yapmak ve seçilen modeli ayrılmış test kümesinde bir kez değerlendirmektir.

### License

Bu proje için henüz bir yazılım lisansı seçilmemiştir. Kaynak veri seti sayfasında lisans belirtilmemiş, veri setinin ve eğitilmiş modelin yeniden dağıtım hakları netleştirilmemiştir. Uygulanabilir koşullar açıklığa kavuşana kadar veri setini veya modeli yeniden dağıtma. Public yayın bu incelemenin tamamlanmasını beklemektedir.

### Developer

Baris AK

Artificial Intelligence and Data Engineering Student
