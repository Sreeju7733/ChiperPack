import os
import pytest
from project import encrypt_file, decrypt_file, list_encrypted_files, remove_all_encrypted_files


def test_remove_all_encrypted_files():
    if list_encrypted_files() == "No encrypted files found" or list_encrypted_files().startswith("An error"):
        print("No encrypted files found")
    else:
        remove_all_encrypted_files()


def test_encryption():

    # Prepare a sample file to encrypt
    file_name = "test_file.txt"
    with open(file_name, "wb") as f:
        f.write(b"This is a test file for encryption.")
    key = "secret_key"


    try:
        # Encrypt the file
        encrypted_file = encrypt_file(file_name, key)
        # Assert that encryption was successful
        assert encrypted_file is not None
    finally:
        # Clean up the test file
        if os.path.exists(file_name):
            os.remove(file_name)




def test_decryption():

    # Prepare a sample file to encrypt
    file_name = "test_file.txt"
    encryptedfilename = file_name + ".sree.gz"
    key = "secret_key"


    try:
        # Decrypt the encrypted file
        decrypted_file = decrypt_file(file_name, key)

        # Assert that decryption was successful
        assert decrypted_file is not None

        # Read and verify the decrypted content
        with open(decrypted_file, "rb") as f:
            decrypted_content = f.read()
            assert decrypted_content == b"This is a test file for encryption."

    finally:
        # Clean up the test files
        if os.path.exists(file_name):
            os.remove(file_name)
        if decrypted_file and os.path.exists(decrypted_file):
            os.remove(decrypted_file)
        if encryptedfilename and os.path.exists(encryptedfilename):
            os.remove(encryptedfilename)




def test_list_encrypted_files(tmp_path):

    # Prepare a sample file to encrypt
    file_name = "test_file.txt"
    with open(file_name, "wb") as f:
        f.write(b"This is a test file for encryption.")
    key = "secret_key"
    try:
        # Encrypt the file
        encrypted_file = encrypt_file(file_name, key)
        # Assert that encryption was successful
        assert encrypted_file is not None
    finally:
        # Clean up the test file
        if os.path.exists(file_name):
            os.remove(file_name)


    encrypted_files_list = list_encrypted_files()
    expected_result = "- " + file_name + ".sree.gz\n"

    # Assert expected result matches the actual result
    assert encrypted_files_list == expected_result

    # Clean up the test files
    remove_all_encrypted_files()



if __name__ == "__main__":
    pytest.main([__file__])
