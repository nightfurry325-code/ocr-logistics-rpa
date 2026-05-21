# Intelligent Google Document AI Logistics RPA Pipeline

## 📝 Project Description
An enterprise-grade Intelligent Document Processing (IDP) and Robotic Process Automation (RPA) engine custom-built for **Proficient Cargo Services India LLP**. This system automates logistics operational data streams by securely fetching email attachments, executing cloud-based **Google Document AI API** extraction, automatically segregating logistics assets (Invoices, Bill of Lading, Airway Bills), and compiling structured data points into multi-sheet Excel files ready for internal **USOFT** server ingestion via FTP synchronization.

---

## 🛠️ System Architecture Diagram

```mermaid
graph TD
    A[BATCH DOCUMENTS\ninput_documents/*] -->|1. Cloud API Call| B(GOOGLE DOCUMENT AI API\nEnterprise Cloud OCR Processor)
    B -->|2. Text Response| C{DETERMINISTIC CLASSIFIER\nAnalyzes Semantics & Metadata}
    C -->|TRANSPORT Match| D[CLASSIFIED AS:\nTRANSPORT_DOCUMENT]
    C -->|INVOICE Match| E[CLASSIFIED AS:\nINVOICE_DOCUMENT]
    D --> F(PANDAS DATA PIPELINE\nStructures Client Field Mapping)
    E --> F
    F -->|3. Data Matrix Sync| G[MULTI-SHEET EXCEL WORKBOOK\nGoogleAIOutputsheet.xlsx]
    G -->|4a. FTP Automation| H(FTP SYNC\nDirect Ingestion to USOFT Server)
    G -->|4b. Notification Node| I(EMAIL SMTP REPORT\nAutomated Analytics Delivery)

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
| **Module 1: Email Ingestion (Gmail/Drive)** | 🟢 **Completed** | Secure IMAP loop operational. Google Drive API setup skeleton ready. |
| **Module 2: Google Document AI OCR Integration** | 🟢 **Completed** | Core framework switched to `google-cloud-documentai` client library. |
| **Module 3: Custom Field Mapping & Excel Integration** | 🟢 **Completed** | Processed JSON variables automatically structured into multi-sheet Excel via Pandas. |
| **Module 4: FTP Upload & SMTP Reports** | 🟡 **In Progress (Partial)** | Delivery loop completed. Pending client production endpoints (FTP/SMTP Host). |
| **Module 5: Workflow Automation Daemon** | 🟢 **Completed** | Full batch pipeline loop automation (`automation.py`) integrated. |

---

## 🚀 Server Installation & Configuration Guide

### Dependency Installation
```bash
pip3 install pandas openpyxl google-cloud-documentai
```

### Runtime Command
```bash
python3 automation.py
```
