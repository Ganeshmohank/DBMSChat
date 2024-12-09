import unittest

from your_module import chunk_text  # Adjust import based on where the function is stored

class TestChunkTextFunction(unittest.TestCase):

    # 1. Basic Test Case for Chunking
    def test_chunk_text_basic(self):
        text = "This is a test text that will be chunked into multiple pieces based on the token size limit."
        pdf_path = "test_pdf_1.pdf"
        chunks = chunk_text(pdf_path, text, max_tokens=10)
        self.assertEqual(len(chunks), 5, f"Expected 5 chunks, but got {len(chunks)}")

    # 2. Edge Case: Text length exactly equals the chunk size
    def test_chunk_text_exact_chunk_size(self):
        text = "This is an exact chunk test."
        pdf_path = "test_pdf_2.pdf"
        chunks = chunk_text(pdf_path, text, max_tokens=4)  # Text has 4 words
        self.assertEqual(len(chunks), 1, f"Expected 1 chunk, but got {len(chunks)}")

    # 3. Small Text Input: Text smaller than max_tokens
    def test_chunk_text_small_text(self):
        text = "Short text."
        pdf_path = "test_pdf_3.pdf"
        chunks = chunk_text(pdf_path, text, max_tokens=1000)
        self.assertEqual(len(chunks), 1, f"Expected 1 chunk, but got {len(chunks)}")

    # 4. Empty Text Case
    def test_chunk_text_empty_text(self):
        text = ""
        pdf_path = "test_pdf_4.pdf"
        chunks = chunk_text(pdf_path, text, max_tokens=10)
        self.assertEqual(len(chunks), 0, "Expected 0 chunks for empty text.")

    # 5. Text with Special Characters
    def test_chunk_text_special_characters(self):
        text = "This is a test with special characters: !@#$%^&*()_+."
        pdf_path = "test_pdf_5.pdf"
        chunks = chunk_text(pdf_path, text, max_tokens=5)
        self.assertEqual(len(chunks), 5, f"Expected 5 chunks, but got {len(chunks)}")

    # 6. Chunk size greater than text length
    def test_chunk_text_large_chunk_size(self):
        text = "Short text."
        pdf_path = "test_pdf_6.pdf"
        chunks = chunk_text(pdf_path, text, max_tokens=50)
        self.assertEqual(len(chunks), 1, f"Expected 1 chunk, but got {len(chunks)}")

    # 7. Verify if chunking respects the token limit (checking last chunk)
    def test_chunk_text_respects_token_limit(self):
        text = " ".join(["word"] * 30)  # 30 words
        pdf_path = "test_pdf_7.pdf"
        chunks = chunk_text(pdf_path, text, max_tokens=10)  # Should have 3 chunks
        self.assertEqual(len(chunks), 3, f"Expected 3 chunks, but got {len(chunks)}")
        self.assertEqual(len(chunks[-1].split()), 10, "Last chunk should have exactly 10 words.")

if __name__ == "__main__":
    unittest.main()
