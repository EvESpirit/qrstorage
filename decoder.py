import os
import cv2
from pyzbar.pyzbar import decode
from collections import defaultdict
from pathlib import Path
import base64


def decode_qr_codes(input_directory):
    qr_codes = defaultdict(str)
    total_chunks = 0

    for file in os.listdir(input_directory):
        file_path = os.path.join(input_directory, file)
        if file_path.endswith('.png') or file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
            img = cv2.imread(file_path)
            decoded_qr_codes = decode(img)

            if len(decoded_qr_codes) == 1:
                data = decoded_qr_codes[0].data.decode("utf-8")
                num_chunks, chunk_number, chunk_data = data.split('|', 2)
                total_chunks = int(num_chunks)
                qr_codes[int(chunk_number)] = chunk_data

    return total_chunks, qr_codes


def combine_chunks(total_chunks, chunks, output_file):
    with open(output_file, "wb") as output:
        for i in range(1, total_chunks + 1):
            if i in chunks:
                b64_data = chunks[i].encode("utf-8")
                output.write(base64.b64decode(b64_data))
            else:
                print(f"Error: Missing chunk {i}. Cannot combine the file.")
                return

        print(f"File successfully combined and saved as {output_file}.")


def main():
    input_directory = input("Enter the input directory containing QR code images: ")
    output_file = input("Enter the output file path: ")

    total_chunks, chunks = decode_qr_codes(input_directory)
    if total_chunks != len(chunks):
        print(f"Error: Found {len(chunks)} QR codes, but expected {total_chunks}.")
    else:
        combine_chunks(total_chunks, chunks, output_file)


if __name__ == "__main__":
    main()
