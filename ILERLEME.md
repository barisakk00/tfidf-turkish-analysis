# Progress Log

## v0.1.0 - 2026-11-08

### Added

- Hugging Face TRSAv1 dataset loading and exploratory analysis for 150,000 labeled Turkish reviews.
- Data cleaning that trims surrounding whitespace, removes blank records, excludes conflicting-label reviews from the baseline, and deduplicates review-label pairs.
- Stratified 70/15/15 train, validation, and test partitions.
- TF-IDF word unigram and bigram features with Logistic Regression.
- Saved pipeline at `models/tfidf_v0.1.joblib` and a terminal prediction interface at `src/predict_cli.py`.
- Bilingual project documentation and pinned direct dependencies.

### Validation Results

- Validation examples: 21,009.
- Accuracy: 0.80199.
- Macro F1: 0.80056.
- Class F1: Negative 0.84106, Neutral 0.71879, Positive 0.84183.
- The held-out test partition has not been evaluated.
- Terminal smoke test: `Harika ürün çok güzel` returned Positive with 93.2% model probability; the `q` exit command worked.

### Data Handling

- 891 conflicting review groups containing 6,883 rows were separated for inspection and excluded from the baseline.
- 3,054 repeated review-label rows were removed.
- 140,063 records remained for stratified splitting.
- The upstream dataset card does not specify a license. Public redistribution of the dataset or trained model remains pending a rights review.

### Remaining Work

- Compare word and character TF-IDF features and measure the contribution of emoji features.
- Tune model parameters using cross-validation on training data.
- Evaluate the selected model once on the held-out test set.
- Clarify dataset and model redistribution terms before any public release.
