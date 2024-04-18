import gzip

def compress_file(file_name):
    compressed_file_name = file_name + ".gz"
    with open(file_name, 'rb') as f_in:
        with gzip.open(compressed_file_name, 'wb') as f_out:
            f_out.writelines(f_in)
    return compressed_file_name

def decompress_file(compressed_file_name):
    decompressed_file_name = compressed_file_name[:-3]
    with gzip.open(compressed_file_name, 'rb') as f_in:
        with open(decompressed_file_name, 'wb') as f_out:
            f_out.writelines(f_in)
    return decompressed_file_name