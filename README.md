# Intelligent Logistics RPA & Document Processing Pipeline

## 📝 Project Description
An enterprise-grade Robotic Process Automation (RPA) and Intelligent Document Processing (IDP) solution custom-built for **Proficient Cargo Services India LLP**. This system automates the manual logistics workflow by dynamically monitoring incoming email dispatches via secure IMAP, executing local multi-language Optical Character Recognition (OCR), classifying documents based on institutional semantics, and structuring extracted high-fidelity data into clean multi-sheet Excel reports. The final pipeline ensures automated operational synchronizations directly to corporate FTP instances for USOFT ingestion, reducing processing overhead and eliminating recurring external API reliance.

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

    %% Neon Cyan Styling
    style A fill:#00f2fe,stroke:#020c1b,stroke-width:2px,color:#020c1b
    style B fill:#00b4db,stroke:#020c1b,stroke-width:2px,color:#020c1b
    style C fill:#10ac84,stroke:#020c1b,stroke-width:2px,color:#fff
    style D fill:#eccc68,stroke:#020c1b,stroke-width:2px,color:#020c1b
    style E fill:#ffa502,stroke:#020c1b,stroke-width:2px,color:#020c1b
    style F fill:#00b4db,stroke:#020c1b,stroke-width:2px,color:#020c1b
    style G fill:#00f2fe,stroke:#020c1b,stroke-width:3px,color:#020c1b
    style H fill:#2f3542,stroke:#00f2fe,stroke-width:2px,color:#00f2fe
    style I fill:#2f3542,stroke:#00f2fe,stroke-width:2px,color:#00f2fe
```

---

## 📊 Statement of Work (SoW) Development Status

| SoW Module & Criteria | Implementation Status | Technical Details / Dependencies |
| :--- | :--- | :--- |
| **Module 1: Automated Email Ingestion** | 🟢 **Completed** | Full IMAP attachment downloader engine is ready to fetch incoming documents. |
| **Module 2: Local OCR & Document Classification** | 🟢 **Completed** | Tesseract OCR core successfully isolates text and splits data into *Invoice* vs *Transport* docs. |
| **Module 3: Data Extraction & Excel Structuring** | 🟢 **Completed** | Regex engine parses variables into standard multi-sheet `GoogleAIOutputsheet.xlsx`. |
| **Module 4: FTP Sync & Email Reporting** | 🟡 **In Progress (Partial)** | Core delivery script is built. **Requires client's FTP credentials and Gmail App Password to activate live deployment.** |
| **Module 5: Daemon Automation (Polling Loop)** | 🟢 **Completed** | Continuous background processing loop (`ocr_run.sh`) is operational for server execution. |

---

## 🚀 Server Installation & Deployment Guide

### Linux Server Deployment (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-eng tesseract-ocr-ind python3 python3-pip -y
pip3 install pandas openpyxl Pillow
```

### Executing the Program
```bash
python3 ocr_run.sh
```
