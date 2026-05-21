# Intelligent Logistics RPA Pipeline

### 🌐 Repository Address

```text
https://github.com/nightfurry325-code/ocr-logistics-rpa.git
```

---

## 🛠️ Project Architecture Diagram

```mermaid
graph TD
    A[LOGISTICS DOCUMENT IMAGE\ninput.jpg] -->|1. System Polling Loop| B(TESSERACT OCR ENGINE\nExtracts English & Indonesian Text)
    B -->|2. Text Semantics| C{DETERMINISTIC CLASSIFIER\nDetects Institutional Keywords}
    C -->|TRANSPORT Keyword| D[CLASSIFIED AS:\nTRANSPORT_DOCUMENT]
    C -->|INVOICE Keyword| E[CLASSIFIED AS:\nINVOICE_DOCUMENT]
    D --> F(REGEX & PANDAS DATA PARSING\nWaybills, Weights, Items)
    E --> F
    F -->|3. Compile Structure| G[MULTI-SHEET EXCEL WORKBOOK\nGoogleAIOutputsheet.xlsx]
    G -->|4a. Automated Sync| H(FTP UPLOAD\nto USOFT Server)
    G -->|4b. End-of-Day Summary| I(EMAIL SMTP REPORT\nto operations management)

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style G fill:#ccf,stroke:#f66,stroke-width:2px,stroke-dasharray: 5, 5
```

---

## An automated RPA system built for **Proficient Cargo Services India LLP**.

This system processes incoming shipping documents via OCR, classifies them, and formats the data into structured multi-sheet Excel outputs.

### Installation (Linux Server)
1. **Install OCR & Dependencies:**
   ```bash
   sudo apt update
   sudo apt install tesseract-ocr tesseract-ocr-eng tesseract-ocr-ind python3 python3-pip -y
   ```
2. **Install Python Libraries:**
   ```bash
   pip3 install pandas openpyxl Pillow
   ```

### Executing the Program
Run the daemon loop:
```bash
python3 ocr_run.sh
```
*The script will poll the system dynamically every few minutes.*
