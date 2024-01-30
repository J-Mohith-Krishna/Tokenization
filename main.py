import re

def detect_word_patterns(text):
    # Regular expression pattern for detecting words
    word_pattern = re.compile(r'\b\w+\b')

    # Find all matches for the word pattern in the text
    words = word_pattern.findall(text)

    return words

def tokenize_text(text):
    # Regular expression pattern for tokenizing text
    token_pattern = re.compile(r'\b\w+\b|\s|[^\w\s]')

    # Find all matches for the token pattern in the text
    tokens = token_pattern.findall(text)

    return tokens

def main():
    # Example text
    text = "A paragraph is a series of sentences that are organized and coherent, and are all related to a single topic.  "

    # Detect word patterns
    words = detect_word_patterns(text)
    print("Words:", words)

    # Tokenize text
    tokens = tokenize_text(text)
    print("Tokens:", tokens)

if __name__ == "__main__":
    main()
