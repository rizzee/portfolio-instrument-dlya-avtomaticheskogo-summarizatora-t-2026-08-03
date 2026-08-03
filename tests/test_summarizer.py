import unittest
from pathlib import Path
from summarizer import preprocess_text, score_sentences


class TestSummarizer(unittest.TestCase):
    def setUp(self):
        self.fixture = """This is a test text. It contains multiple sentences.
        The goal is to verify that the summarizer works correctly."""

    def test_preprocess_text(self):
        text = "  This   has   extra   spaces  "
        result = preprocess_text(text)
        self.assertEqual(result, "This has extra spaces")

    def test_score_sentences(self):
        sentences = score_sentences(self.fixture)
        self.assertEqual(len(sentences), 2)
        self.assertIsInstance(sentences, dict)


if __name__ == '__main__':
    unittest.main()
