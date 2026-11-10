from pathlib import Path

import joblib
import pandas as pd
from openpyxl.worksheet.table import Table, TableStyleInfo


LABEL_NAMES = {
    "Negative": "Negatif",
    "Neutral": "Nötr",
    "Positive": "Pozitif",
}
MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "tfidf_v1.0.joblib"


def predict_single(model):
    print("Tek metin tahmini. Ana menüye dönmek için q yazın.")

    while True:
        try:
            text = input("Metin> ").strip()
        except EOFError:
            return

        if text.lower() in {"q", "quit", "exit"}:
            return

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


def predict_batch(model):
    input_value = input("TXT dosyasının yolu> ").strip().strip('"')
    if not input_value:
        print("Dosya yolu boş bırakılamaz.")
        return

    input_path = Path(input_value).expanduser()
    if not input_path.is_absolute():
        input_path = Path.cwd() / input_path
    input_path = input_path.resolve()

    if input_path.suffix.lower() != ".txt":
        print("Girdi dosyası .txt uzantılı olmalı.")
        return
    if not input_path.is_file():
        print(f"Dosya bulunamadı: {input_path}")
        return

    try:
        lines = input_path.read_text(encoding="utf-8-sig").splitlines()
    except UnicodeDecodeError:
        print("Dosya UTF-8 biçiminde okunamadı. TXT dosyasını UTF-8 olarak kaydedin.")
        return

    entries = [
        (line_number, line.strip())
        for line_number, line in enumerate(lines, start=1)
        if line.strip()
    ]
    if not entries:
        print("TXT dosyasında tahmin edilecek boş olmayan satır bulunamadı.")
        return

    texts = [text for _, text in entries]
    predictions = model.predict(texts)
    probabilities = model.predict_proba(texts)
    class_labels = list(model.classes_)

    rows = []
    for (line_number, text), predicted_label, probability_row in zip(
        entries, predictions, probabilities
    ):
        row = {
            "Satır": line_number,
            "Metin": text,
            "Tahmin": LABEL_NAMES.get(predicted_label, predicted_label),
            "Güven": float(max(probability_row)),
        }
        for label, probability in zip(class_labels, probability_row):
            row[f"{LABEL_NAMES.get(label, label)} olasılığı"] = float(probability)
        rows.append(row)

    output_value = input(
        "Excel çıktı yolu (boş bırakılırsa TXT dosyasının yanına kaydedilir)> "
    ).strip().strip('"')
    output_path = (
        Path(output_value).expanduser()
        if output_value
        else input_path.with_name(f"{input_path.stem}_tahminler.xlsx")
    )
    if not output_path.is_absolute():
        output_path = Path.cwd() / output_path
    output_path = output_path.resolve()

    if output_path == input_path:
        print("Çıktı dosyası, girdi TXT dosyasının üzerine yazamaz.")
        return
    if output_path.suffix.lower() != ".xlsx":
        output_path = output_path.with_suffix(".xlsx")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    results = pd.DataFrame(rows)
    results.to_excel(output_path, index=False, sheet_name="Tahminler", engine="openpyxl")

    from openpyxl import load_workbook

    workbook = load_workbook(output_path)
    worksheet = workbook["Tahminler"]
    worksheet.freeze_panes = "A2"
    table = Table(displayName="DuyguTahminleri", ref=worksheet.dimensions)
    table.tableStyleInfo = TableStyleInfo(
        name="TableStyleMedium2",
        showFirstColumn=False,
        showLastColumn=False,
        showRowStripes=True,
        showColumnStripes=False,
    )
    worksheet.add_table(table)

    for column_cells in worksheet.columns:
        column_letter = column_cells[0].column_letter
        header = str(column_cells[0].value)
        width = min(max(max(len(str(cell.value or "")) for cell in column_cells) + 2, len(header) + 2), 60)
        worksheet.column_dimensions[column_letter].width = width
        if header == "Metin":
            worksheet.column_dimensions[column_letter].width = 60
        if header == "Güven" or header.endswith(" olasılığı"):
            for cell in column_cells[1:]:
                cell.number_format = "0.0%"

    workbook.save(output_path)
    print(f"{len(rows)} metin tahmin edildi.")
    print(f"Sonuç dosyası: {output_path}")


def main():
    if not MODEL_PATH.exists():
        raise SystemExit("Model dosyası bulunamadı. Önce notebook'taki model kaydetme hücresini çalıştırın.")

    model = joblib.load(MODEL_PATH)
    print("Duygu analizi hazır.")

    while True:
        print("\n1: Tek metin tahmini")
        print("2: TXT dosyasından toplu tahmin")
        print("q: Çıkış")
        choice = input("Seçim> ").strip().lower()

        if choice in {"q", "quit", "exit"}:
            break
        if choice == "1":
            predict_single(model)
        elif choice == "2":
            predict_batch(model)
        else:
            print("Geçersiz seçim. 1, 2 veya q girin.")

    print("Duygu analizi kapatıldı.")


if __name__ == "__main__":
    main()
