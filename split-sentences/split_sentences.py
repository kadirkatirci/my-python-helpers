import os
import re

def process_text(text):
    paragraphs = [p for p in text.split('\n') if p.strip()]
    all_sentences = []

    for paragraph in paragraphs:
        # Remove text within [] or {}
        cleaned_paragraph = re.sub(r'\[.*?\]|\{.*?\}', '', paragraph)
        sentence_start = 0
        in_quotes = False
        p_len = len(cleaned_paragraph)
        i = 0

        while i < p_len:
            char = cleaned_paragraph[i]
            if char == '"':
                in_quotes = not in_quotes

            is_visible_end_char = char in ['.', '?', '!', ':'] and not in_quotes
            is_invisible_end_char = char in ['@', '#'] and not in_quotes
            is_end_of_sentence = is_visible_end_char or is_invisible_end_char
            is_end_of_paragraph = i == p_len - 1
            next_char = cleaned_paragraph[i+1] if i+1 < p_len else ''

            if (is_end_of_sentence and (next_char == ' ' or is_end_of_paragraph)) or is_end_of_paragraph:
                if is_end_of_paragraph and not is_end_of_sentence:
                    end_idx = p_len
                else:
                    end_idx = i + 1
                if is_invisible_end_char:
                    end_idx = i
                sentence = cleaned_paragraph[sentence_start:end_idx].strip()
                if sentence:
                    all_sentences.append(sentence)
                if is_end_of_sentence and next_char == ' ':
                    sentence_start = i + 2
                    i += 1  # Skip the space
                else:
                    sentence_start = i + 1
            i += 1
    return '\n'.join(all_sentences)

def main():
    for root, dirs, files in os.walk('.'):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                # Read file content
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Process content
                new_content = process_text(content)
                # Write new content back to file
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Processed file: {filepath}")
            except Exception as e:
                print(f"Error processing file {filepath}: {e}")

if __name__ == '__main__':
    main()
