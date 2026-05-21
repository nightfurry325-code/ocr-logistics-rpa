# Intelligent Logistics RPA & Document Processing Pipeline

An enterprise-grade Robotic Process Automation (RPA) and Intelligent Document Processing (IDP) solution designed for **Proficient Cargo Services India LLP**. This system automates the logistics data workflow by monitoring email dispatch, executing local Optical Character Recognition (OCR), classifying logistical documents, and structuring extracted data into multi-sheet Excel workbooks for downstream integration into the USOFT ecosystem.

---

## 🛠️ Core System Architecture

The automation pipeline utilizes local processing engines to ensure data sovereignty and eliminate recurring API costs.

1. **Ingestion Module (IMAP):** Monitors `proficientdocuments@gmail.com` in real-time, filters secure incoming traffic from verified dispatchers, and downloads transactional documentation.
2. **OCR Engine (Tesseract):** Performs local multi-language pixel-to-text extraction supporting mixed English and Indonesian logistical terminology.
3. **Deterministic Classifier:** Analyzes textual semantics to segregate files into `TRANSPORT_DOCUMENT` (Bill of Lading / Airway Bill) or `INVOICE_DOCUMENT` based on institutional keywords.
4. **Data Extraction & Structuring (Regex & Pandas):** Parses high-fidelity data points (Waybill Numbers, Carrier Weights, Line-item descriptions) and compiles them into a standardized multi-sheet workbook (`GoogleAIOutputsheet.xlsx`).
5. **Distribution Module (FTP & SMTP):** Syncs output files directly to the corporate FTP instance for USOFT ingestion and dispatches automated end-of-day summary analytics to operations management.

---

## 🚀 Server Installation & Deployment Guide

### Option A: Deployment on Linux Server (Ubuntu/Debian VPS)
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install tesseract-ocr tesseract-ocr-eng tesseract-ocr-ind python3 python3-pip -y
git clone https://github.com/nightfurry325-code/ocr-logistics-rpa.git
cd ocr-logistics-rpa
pip3 install pandas openpyxl Pillow
```

### Option B: Deployment on Windows Server
1. Download Python 3.10+ and add to PATH.
2. Download Tesseract OCR Windows Installer, install it, and add the folder path to Environment Variables.
3. Run: `pip install pandas openpyxl Pillow`

---

## ⚙️ Production Configuration
Before launching the pipeline execution cycle, configure the secure access variables within the script environment:
* **Gmail IMAP Account & 16-digit App Password**
* **Corporate FTP Server Integration (Host, User, Pass)**
* **Management Reporting Distribution List**

*Note: The script runs on an infinite automated polling loop.*
