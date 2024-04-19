# ChiperPack: Secure File Encryptor and Decryptor

[![CS50P Sreeju](https://certificates.cs50.io/2c93ffd9-177a-4187-9bb7-cac0780fa781.png?size=A4)](https://certificates.cs50.io/2c93ffd9-177a-4187-9bb7-cac0780fa781)
[![image](https://github.com/Sreeju7733/ChiperPack/assets/77568405/c689a19e-aed1-47df-9e31-f2b7cb24f0e1)](https://certificates.cs50.io/2c93ffd9-177a-4187-9bb7-cac0780fa781)

#### Video Demo: [https://youtu.be/USu6akq9ZmQ?si=ygvK6CHDgeGHs_-A](https://youtu.be/USu6akq9ZmQ?si=ygvK6CHDgeGHs_-A)

## Table of Contents
- [Description](#description)
- [Technologies Used](#technologies-used)
- [Project Overview](#project-overview)
- [Files and Functionality](#files-and-functionality)
- [Design Choices](#design-choices)
- [Usage](#usage)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)
- [Conclusion](#conclusion)
- [Acknowledgements](#acknowledgements)


## Description:
ChiperPack is a tool that helps keep your files safe by encrypting them. Encryption means converting your file into a secret code that only you can unlock with a special key.


## Technologies Used
ChiperPack is developed using the following technologies:

- **Python**: The core programming language used to implement the file encryption and decryption functionalities.
- **pycryptodome**: A library used for cryptographic operations, including AES encryption and decryption.
- **pyfiglet**: A library used for generating ASCII art text, enhancing the visual presentation of the command-line interface.
- **gzip**: A module in Python used for file compression and decompression.


## Project Overview
ChiperPack lets you encrypt your files using a secret key. Encrypted files are saved with a special extension (`.sree`). You can also decrypt these files back to their original form using the same secret key. ChiperPack can also show you a list of all encrypted files in the folder.


## Files and Functionality
- **`project.py`**: This file has the main part of ChiperPack. It includes functions to encrypt files (`encrypt_file`), decrypt files (`decrypt_file`), list encrypted files (`list_encrypted_files`), and control the program (`main`). It also uses `compressor.py` to handle file compression.

- **`compressor.py`**: This file handles compressing and decompressing files using the `gzip` library. It includes functions to compress (`compress_file`) and decompress (`decompress_file`) files.


## Design Choices
- **AES Encryption**: ChiperPack uses a type of encryption called AES (Advanced Encryption Standard) to keep your files safe. AES is known for being very secure and is commonly used in encryption.

- **File Compression**: Before encrypting files, ChiperPack compresses them to make them smaller. This can be helpful for large files. After decrypting, compressed files are decompressed to get the original content back.

- **User Interface**: ChiperPack is easy to use with a simple command-line interface (CLI). You can choose to encrypt, decrypt, or list encrypted files interactively.


## Usage
1. Clone the repository:  `git clone https://github.com/Sreeju/ChiperPack`
2. Install the required dependencies using pip: `pip install -r requirements.txt`
3. Run the program by executing `python project.py`
4. Follow the prompts to encrypt, decrypt, or list encrypted files.


## Installation
You can install the required dependencies using pip: `pip install pyfiglet pytest pycryptodome pytest pycryptodome hashlib os`


## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance the project.


## License
This project is licensed under the [MIT License](LICENSE) - see the `LICENSE` file for details.


## Conclusion
ChiperPack is a beginner-friendly tool for file encryption and decryption using Python. It's a good starting point to learn about encryption and file security. Check out the project on GitHub for more details and updates.


## Acknowledgements
Thank you to David Malan and his entire team for helping to make the harvard CS50P course accessible to everyone who wants to learn, and teach it in such an astounding way.
