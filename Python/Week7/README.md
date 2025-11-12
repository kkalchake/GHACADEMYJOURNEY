# Word Count Script

A command-line Python script that reads a text file, tokenizes its content using a custom regex, counts word occurrences, and prints statistics such as total and unique words, as well as the top 5 most frequent words.

---

## 🔧 Features

- Reads file content as UTF-8
- Uses advanced regex for robust tokenization
- Converts all tokens to lowercase
- Logs tokens and word count to `stderr`
- Uses `collections.Counter` for word counting
- Outputs:
  - Total word count
  - Unique word count
  - Top 5 most frequent words (left-aligned)
- Handles file read errors and missing arguments gracefully

---

## 🧪 Tokenization Regex

```
(?:[A-Za-z]\.){2,}[A-Za-z]?\.?|\d+\.\d+|(?:[#@]?\w+(?:[-']\w+)*)|[A-Za-z]+
```

Handles:
- Abbreviations like `U.S.A.`
- Decimal numbers like `3.14`
- Hashtags/usernames like `#tag` or `@user`
- Words with apostrophes or hyphens like `don't`, `mother-in-law`

---

## 🚀 Usage

```bash
python script.py <file_path>
```

### Example

```bash
python script.py sample.txt
```

---

## 📦 Output Example

```
Total Words: 350
Unique Words: 180

Top 5 most repeated unique words and their occurrences:
---------------------------------------------
the                  27
and                  19
of                   15
to                   14
in                   13
```

If the file is empty or contains no valid words:

```
The text does not have any words.
```

If no file path is given:

```
Usage: python script.py <file_path>
```

---

## ❗ Dependencies

- Python 3.x (standard library only)

---

## 🛠 Structure

- `read_file(path)` – Reads file content
- `tokenize(text)` – Extracts words using regex
- `count_words(tokens)` – Counts with `Counter`
- `word_count_main(text)` – Orchestrates analysis
- `main()` – Handles command-line arguments

---

## ✅ License

This project is free to use and modify for any purpose.
