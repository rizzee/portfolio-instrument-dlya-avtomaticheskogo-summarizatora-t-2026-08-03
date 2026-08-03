import argparse
from pathlib import Path
from summarizer import summarize_text


def main():
    parser = argparse.ArgumentParser(description='Summarize long articles into concise bullet points.')
    parser.add_argument('file', type=Path, help='Path to the text file to summarize')
    args = parser.parse_args()

    text = args.file.read_text()
    summary = summarize_text(text)
    print('\n'.join(summary))


if __name__ == '__main__':
    main()
