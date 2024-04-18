import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import compressor
import pyfiglet



"""
Main Function
"""
def main():

    print(pyfiglet.figlet_format("ChiperPack", font="slant"))

    while True:
        user_input_choice = input("\n\n Type 'e' for encryption or 'd' for decryption or 'ls' for list of encrypted files (or 'q' to quit): ")


        if user_input_choice.lower() == 'e':
            file_name = input("\n\n Name of the file to encrypt: ")
            key = input("\n\n Enter the key: ")
            encrypted_file = encrypt_file(file_name, key)
            if encrypted_file:
                print("\n\n File encrypted successfully. Encrypted file saved at:", encrypted_file)
        

        elif user_input_choice.lower() == 'd':
            file_name = input("\n\n Name of the file to decrypt: ")
            key = input("\n\n Enter the key: ")
            decrypted_file = decrypt_file(file_name, key)
            if decrypted_file:
                print("\n\n File decrypted successfully. Decrypted file saved at:", decrypted_file)
        

        elif user_input_choice.lower() == 'ls':
            print(list_encrypted_files())


        elif user_input_choice.lower() == 'q':
            print(pyfiglet.figlet_format("Exiting...", font="slant"))
            break
        


        else:
            print("Invalid choice. Please enter 'e' for encryption, 'd' for decryption, or 'q' to quit.")






"""
Encryption Function
"""
def encrypt_file(file_name, key):
    try:
        if not os.path.exists(file_name):
            return "File not found"

        iv = get_random_bytes(AES.block_size)

        cipher = AES.new(hashlib.sha256(key.encode()).digest(), AES.MODE_CBC, iv)


        chunk_size = 64 * 1024
        output = b''


        with open(file_name, 'rb') as infile:
            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break
 
                elif len(chunk) % AES.block_size != 0:
                    chunk += b' ' * (AES.block_size - len(chunk) % AES.block_size)
     
                encrypted_chunk = cipher.encrypt(chunk)
                output += encrypted_chunk

  

        encrypted_file_name = file_name + ".sree"
        with open(encrypted_file_name, 'wb') as outfile:
            outfile.write(iv + output)
            

        compressor.compress_file(encrypted_file_name)
        os.remove(encrypted_file_name)
        os.remove(file_name)
        return f"Encrypted successfully"

        
    except Exception as e:
        return f"An error occurred during encryption: {str(e)}"





"""
Decryption Function
"""
def decrypt_file(encrypted_file_name, key):
    try:
        if not os.path.exists(encrypted_file_name):

            if encrypted_file_name.endswith(".sree.gz"):
                if os.path.exists(encrypted_file_name):
                    compressed_file = encrypted_file_name
                    encrypted_file_name = compressor.decompress_file(encrypted_file_name)
                    os.remove(compressed_file)
                else:
                    raise FileNotFoundError(f"Encrypted file not found: {encrypted_file_name}")


            elif encrypted_file_name.endswith(".sree"):
                if os.path.exists(encrypted_file_name):
                    compressed_file_name = compressor.compress_file(encrypted_file_name + ".gz")
                    os.remove(encrypted_file_name)
                    encrypted_file_name = compressed_file_name
                else:
                    raise FileNotFoundError(f"Encrypted file not found: {encrypted_file_name}")

                
            else:
                sree_gz_file_name = encrypted_file_name + ".sree.gz"
                gz_file_name = encrypted_file_name + ".gz"

                if os.path.exists(sree_gz_file_name):
                    compressed_file_path = sree_gz_file_name
                    encrypted_file_name = compressor.decompress_file(sree_gz_file_name)
                elif os.path.exists(gz_file_name):
                    encrypted_file_name = gz_file_name
                else:
                    raise FileNotFoundError(f"Encrypted file not found: {encrypted_file_name}")


        chunk_size = 64 * 1024
        decrypted_file_name = encrypted_file_name[:-5]


        with open(encrypted_file_name, 'rb') as infile:
            iv = infile.read(AES.block_size)
            decryptor = AES.new(hashlib.sha256(key.encode()).digest(), AES.MODE_CBC, iv)
            with open(decrypted_file_name, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    decrypted_chunk = decryptor.decrypt(chunk)
                    outfile.write(decrypted_chunk.rstrip(b' '))

        os.remove(encrypted_file_name)
        return decrypted_file_name


    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise Exception(f"An error occurred during decryption: {str(e)}")






"""
List Encrypted Files Function
"""
def list_encrypted_files():

    try:
        encrypted_files = [file for file in os.listdir() if file.endswith(".sree.gz")]

        returnval = ""

        if encrypted_files:
            print("Encrypted files:")
            for file in encrypted_files:
                returnval = returnval +  f"- {file}\n"
        else:
            returnval = "No encrypted files found"

        return returnval


    except Exception as e:
        print(f"An error occurred while listing encrypted files: {str(e)}")



"""
Remove All Encrypted Files Function
"""
def remove_all_encrypted_files():
    try:
        encrypted_files = [file for file in os.listdir() if file.endswith(".sree.gz")]
        
        if encrypted_files:
            print("Removing encrypted files:")
            for file in encrypted_files:
                os.remove(file)
                print(f"Deleted: {file}")
            print("All encrypted files have been successfully removed.")
        else:
            print("No encrypted files found.")
    except Exception as e:
        print(f"An error occurred while removing encrypted files: {str(e)}")





if __name__ == "__main__":
    main()
