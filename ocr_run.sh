#!/data/data/com.termux/files/usr/bin/bash

FILE_PATH="$HOME/ocr-logistics/input.jpg"
OUTPUT_TXT="$HOME/ocr-logistics/hasil_scan"

if [ ! -f "$FILE_PATH" ]; then
    echo "File input.jpg kagak ada di folder, Wir!"
    exit 1
fi

echo "Memproses OCR secara LOKAL di Termux..."

# Jalankan tesseract pake data bahasa Indonesia
tesseract "$FILE_PATH" "$OUTPUT_TXT" -l ind > /dev/null 2>&1

echo -e "\n--- HASIL OCR BERHASIL (100% LOKAL) ---"
if [ -f "${OUTPUT_TXT}.txt" ]; then
    cat "${OUTPUT_TXT}.txt"
    rm -f "${OUTPUT_TXT}.txt"
else
    echo "Gagal memproses gambar lokal, Wir. Cek format filenya."
fi
