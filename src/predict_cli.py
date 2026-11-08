from pathlib import Path

import joblib


LABEL_NAMES = {
    "Negative": "Negatif",
    "Neutral": "Nötr",
    "Positive": "Pozitif",
}
MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "tfidf_v1.0.joblib"


def main():
    if not MODEL_PATH.exists():
        raise SystemExit("Model dosyası bulunamadı. Önce notebook'taki model kaydetme hücresini çalıştırın.")

    model = joblib.load(MODEL_PATH)
    print("Duygu analizi hazır. Çıkmak için q yazın.")

    while True:
        try:
            text = input("Metin> ").strip()
        except EOFError:
            break

        if text.lower() in {"q", "quit", "exit"}:
            break

        if not text:
            continue

        predicted_label = model.predict([text])[0]
        probabilities = model.predict_proba([text])[0]
        ranked_predictions = sorted(
            zip(model.classes_, probabilities),
            key=lambda prediction: prediction[1],
            reverse=True,
        )

        print(f"Tahmin: {LABEL_NAMES.get(predicted_label, predicted_label)}")

        for label, probability in ranked_predictions:
            print(f"{LABEL_NAMES.get(label, label)}: {probability:.1%}")

    print("Duygu analizi kapatıldı.")


if __name__ == "__main__":
    main()
