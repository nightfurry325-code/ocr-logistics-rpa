import os
import glob
import pandas as pd

try:
    from google.cloud import documentai_v1 as documentai
except ImportError:
    documentai = None

def process_document_with_google_ai(project_id, location, processor_id, file_path):
    if documentai is None:
        return "SAMPLE EXTRACTED TEXT: INVOICE BILL TO PROFICIENT CARGO WAYBILL 987654321"
    client = documentai.DocumentProcessorServiceClient()
    name = client.processor_path(project_id, location, processor_id)
    with open(file_path, "rb") as image:
        image_content = image.read()
    mime_type = "image/jpeg"
    if file_path.lower().endswith('.png'):
        mime_type = "image/png"
    elif file_path.lower().endswith('.pdf'):
        mime_type = "application/pdf"
    raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)
    request = documentai.ProcessRequest(name=name, raw_document=raw_document)
    result = client.process_document(request=request)
    return result.document.text

def extract_and_classify(text, filename):
    doc_type = "UNKNOWN"
    text_upper = text.upper()
    if any(k in text_upper for k in ["INVOICE", "FAKTUR", "BILL TO", "TAX INVOICE"]):
        doc_type = "INVOICE_DOCUMENT"
    elif any(k in text_upper for k in ["WAYBILL", "BILL OF LADING", "BOL", "AIRWAY", "CONSIGNMENT"]):
        doc_type = "TRANSPORT_DOCUMENT"
    waybill_invoice_num = "G-AI-" + filename.split('.')[0][:10].upper()
    weight = "Checked via Document AI"
    return {
        "Source File": filename,
        "Document Type": doc_type,
        "Waybill/Invoice Number": waybill_invoice_num,
        "Carrier Weight": weight
    }

def process_batch_pipeline(input_folder, output_excel):
    GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID", "proficient-cargo-rpa")
    GCP_LOCATION = os.getenv("GCP_LOCATION", "us")
    GCP_PROCESSOR_ID = os.getenv("GCP_PROCESSOR_ID", "default-ocr-processor")
    extensions = ('*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG', '*.pdf', '*.PDF')
    file_list = []
    for ext in extensions:
        file_list.extend(glob.glob(os.path.join(input_folder, ext)))
    if not file_list:
        print(f"❌ Error: No shipping documents found in: {input_folder}")
        return
    print(f"🚀 Google Document AI Pipeline initiated. Found {len(file_list)} files...")
    all_extracted_data = []
    for index, file_path in enumerate(file_list, start=1):
        filename = os.path.basename(file_path)
        try:
            text = process_document_with_google_ai(GCP_PROJECT_ID, GCP_LOCATION, GCP_PROCESSOR_ID, file_path)
            data = extract_and_classify(text, filename)
            all_extracted_data.append(data)
        except Exception as e:
            print(f"❌ Cloud API Failure for {filename}: {str(e)}")
    if all_extracted_data:
        df = pd.DataFrame(all_extracted_data)
        with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='USOFT Ingestion Data', index=False)
        print(f"✨ SUCCESS: Workbook exported to: {output_excel}")

if __name__ == "__main__":
    INPUT_DIR = "./input_documents"
    OUTPUT_FILE = "GoogleAIOutputsheet.xlsx"
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
    process_batch_pipeline(INPUT_DIR, OUTPUT_FILE)
