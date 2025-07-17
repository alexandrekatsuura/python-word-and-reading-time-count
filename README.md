# 📖 Word & Reading Time Count

![GitHub repo size](https://img.shields.io/github/repo-size/alexandrekatsuura/python-word-and-reading-time-count?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/alexandrekatsuura/python-word-and-reading-time-count?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/alexandrekatsuura/python-word-and-reading-time-count?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/alexandrekatsuura/python-word-and-reading-time-count?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/alexandrekatsuura/python-word-and-reading-time-count?style=for-the-badge)

## 📚 Academic Use Disclaimer

> ⚠️ This is an academic project created solely for educational purposes.
> It is not intended for production use or handling sensitive data.

## ℹ️ About

**Word & Reading Time Count** is a simple Python-based CLI application that counts the number of words in a text input and estimates the time required to read it based on an average reading speed.

This project is a practical example of basic string manipulation, command-line input handling, and unit testing in Python.

## 🚀 Features

* 🔢 **Word Count**: Calculates the number of words in the input text.
* ⏱️ **Reading Time Estimation**: Computes how long it would take to read the input based on 200 words per minute.
* 🧪 **Unit Testing with Pytest**: Ensures accuracy of the core logic.
* 💻 **Command-Line Interface**: Simple user interaction via terminal.
* 🧩 **Modular Codebase**: Clean separation of logic and execution.

## 🛠️ Technologies Used

* **Python 3.x**
* **`input()` / `print()`**: For terminal interaction
* **`pytest`**: For writing and running unit tests

## ⚙️ How to Run the Project

### Prerequisites

Make sure you have **Python 3.x** installed on your system.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/alexandrekatsuura/python-word-and-reading-time-count
cd python-word-and-reading-time-count
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/macOS
# .venv\Scripts\activate    # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

To run the application and analyze a text:

```bash
python src/main.py
```

You will be prompted to enter your text. After typing or pasting the text and pressing Enter, the program will display:

* The total number of words.
* The estimated reading time in minutes.

## ✅ Running the Tests

To run all unit tests using `pytest`, execute the following command from the project root:

```bash
pytest -v
```

This will run all tests in the `tests/` folder and report the results in verbose mode.

## 📁 Project Structure

```bash
python-word-and-reading-time-count/
├── src/
│   ├── main.py             # Main execution logic (CLI)
│   └── service.py          # Core logic: word count & reading time
├── tests/
│   └── test_service.py     # Unit tests for service logic
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).