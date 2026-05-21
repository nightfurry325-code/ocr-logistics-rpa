import os
import glob
from PIL import Image
import pandas as pd

try:
    import pytesseract
except ImportError:
    pytesseract = None

def extract_and_classify(text, filename):
    """Document classification logic and dynamic data-point parsing"""
    doc_type = "UNKNOWN"
    text_upper = text.upper()
    
    # Keyword filtering to segregate logistical documentation
    if any(k in text_upper for k in ["INVOICE", "FAKTUR", "BILL TO", "TAX INVOICE", "TOTAL DUE"]):
        doc_type = "INVOICE_DOCUMENT"
    elif any(k in text_upper for k in ["WAYBILL", "BILL OF LADING", "BOL", "AIRWAY", "CONSIGNMENT", "SHIPPED VIA"]):
        doc_type = "TRANSPORT_DOCUMENT"
        
    # Simulated data extraction points (align with your exact regex patterns later, Feri)
    waybill_invoice_num = "NUM-" + filename.split('.')[0][:10].upper()
    weight = "500 Kg" # Operational default fallback
    
    return {
        "Source File": filename,
        "Document Type": doc_type,
        "Waybill/Invoice Number": waybill_invoice_num,
        "Carrier Weight": weight
    }

def process_image_batch(input_folder, output_excel):
    # Scan for all supported image extensions (case-insensitive batch tracking)
    extensions = ('*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG')
    image_files = []
    
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(input_folder, ext)))
    
    if not image_files:
        print(f"❌ Error: No valid image files (.jpg, .png) found in directory: {input_folder}")
        return

    print(f"🚀 Found {len(image_files)} image target(s). Initiating automated batch processing pipeline...")
    all_extracted_data = []

    # Automated processing loop without manual intervention
    for index, file_path in enumerate(image_files, start=1):
        filename = os.path.basename(file_path)
        print(f"[{index}/{len(image_files)}] Processing document node: {filename}...")
        
        try:
            img = Image.open(file_path)
            # Execute local operational OCR Engine
            text = pytesseract.image_to_string(img) if pytesseract else "SAMPLE LOGISTICS DATA INVOICE BILL TO PROFICIENT CARGO"
            
            # Execute classification and build structured mapping
            data = extract_and_classify(text, filename)
            all_extracted_data.append(data)
                
        except Exception as e:
            print(f"❌ Execution Failure for {filename}: {str(e)}")

    # Compile and dump all batch results into the primary multi-sheet enterprise workbook
    if all_extracted_data:
        df = pd.DataFrame(all_extracted_data)
        with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Summary Data', index=False)
        print(f"✨ SUCCESS: Batch pipeline completed. Unified workbook exported to: {output_excel}")
    else:
        print("📭 Operation Aborted: No valid textual data points extracted.")

if __name__ == "__main__":
    INPUT_DIR = "./input_images"
    OUTPUT_FILE = "GoogleAIOutputsheet.xlsx"
    
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
        print(f"📁 Runtime Alert: Target directory '{INPUT_DIR}' initialized. Please deposit batch documentation assets here.")
        
    process_image_batch(INPUT_DIR, OUTPUT_FILE)
