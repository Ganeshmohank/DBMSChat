import unittest
import os
from your_module import extract_text_from_pdf  # Adjust based on where the function is stored

class TestExtractTextFromPdf(unittest.TestCase):

    # 1. Test Case for Basic Text Extraction
    def test_extract_text_basic(self):
        pdf_path = "sample_pdf_1.pdf"  # Provide a sample PDF with simple text
        expected_output = "This is a sample PDF text."
        extracted_text = extract_text_from_pdf(pdf_path)
        self.assertEqual(extracted_text, expected_output, f"Expected '{expected_output}', but got '{extracted_text}'")

    # 2. Test Case for Empty PDF
    def test_extract_text_empty_pdf(self):
        pdf_path = "empty_pdf.pdf"  # Provide a sample empty PDF
        extracted_text = extract_text_from_pdf(pdf_path)
        self.assertEqual(extracted_text, "", "Expected empty string for empty PDF")

    # 3. Test Case for PDF with Images/Non-Text Content
    def test_extract_text_pdf_with_images(self):
        pdf_path = "pdf_with_images.pdf"  # Provide a PDF that contains images or scanned content
        extracted_text = extract_text_from_pdf(pdf_path)
        self.assertEqual(extracted_text, "", "Expected empty string for PDF with no extractable text")

    # 4. Test Case for Multi-page PDF
    def test_extract_text_multi_page_pdf(self):
        pdf_path = "multi_page_pdf.pdf"  # Provide a sample multi-page PDF with text
        expected_output = "Page 1 text\nPage 2 text"
        extracted_text = extract_text_from_pdf(pdf_path)
        self.assertEqual(extracted_text, expected_output, f"Expected '{expected_output}', but got '{extracted_text}'")

    # 5. Test Case for PDF with Text Formatting
    def test_extract_text_with_formatting(self):
        pdf_path = "formatted_text_pdf.pdf"  # Provide a PDF with formatted text (e.g., bold, italics)
        extracted_text = extract_text_from_pdf(pdf_path)
        self.assertNotEqual(extracted_text, "", "Expected non-empty string for formatted text PDF")
        self.assertIn("bold text", extracted_text, "Expected 'bold text' to be found in extracted text")

    # 6. Test Case for Invalid PDF Path
    def test_extract_text_invalid_path(self):
        pdf_path = "non_existent_pdf.pdf"  # Provide a non-existent file path
        with self.assertRaises(FileNotFoundError):
            extract_text_from_pdf(pdf_path)

    # 7. Test Case for PDF with Mixed Content (Text + Images)
    def test_extract_text_mixed_content_pdf(self):
        pdf_path = "mixed_content_pdf.pdf"  # Provide a PDF with both text and images
        extracted_text = extract_text_from_pdf(pdf_path)
        self.assertGreater(len(extracted_text), 0, "Expected non-empty string from mixed content PDF")

if __name__ == "__main__":
    unittest.main()
