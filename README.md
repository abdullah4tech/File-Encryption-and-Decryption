# 🔒 File Encryption and Decryption 🔓

This Python program includes two scripts, 📜 `encrypt.py` and 📜 `decrypt.py`, designed for encrypting and decrypting text files using the Fernet encryption scheme from the `cryptography` library.

## How it Works 🛠️

### `encrypt.py` 🌐

The `encrypt.py` script follows these steps:

1. Gets the current directory.
2. Identifies all text files (files with a '.txt' extension) in the directory.
3. Generates a Fernet key.
4. Writes the key to a file named `key.key`.
5. Encrypts the content of each text file using the generated key.

### `decrypt.py` 🔓

The `decrypt.py` script follows these steps:

1. Gets the current directory.
2. Identifies all encrypted text files in the directory (files with a '.txt' extension).
3. Reads the Fernet key from the `key.key` file.
4. Decrypts the content of each encrypted text file using the stored key.

## Requirements 📋

- Python
- `cryptography` library

Install the required library using:

```bash
pip install cryptography
```

## Contribution 🤝

Feel free to contribute to the project by opening issues or submitting pull requests. Follow the guidelines outlined in [CONTRIBUTING.md](CONTRIBUTING.md).

## How to Run ▶️

### Encryption 🔐

Run the encryption script using a Python interpreter:

```bash
python encrypt.py
```

### Decryption 🔓

Run the decryption script using a Python interpreter:

```bash
python decrypt.py
```

## Key Storage 🗝️

The encryption key is generated and stored in a file named `key.key` during the encryption process. This key file is crucial for decryption. Ensure its security and do not share it with encrypted files.

## Important Security Information ⚠️

- Keep the encryption key (`key.key`) secure.
- Do not share the key or store it with the encrypted files.
- Losing the key will result in permanent data loss as decryption will not be possible.

**Caution:** Use this encryption method responsibly, and always keep a secure backup of your key.

## License 📄

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

**Disclaimer:** This program is for educational purposes and should be used responsibly. The developers are not responsible for any misuse or data loss resulting from the use of this software.