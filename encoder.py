import qrcode
from PIL import Image
import os
import base64

max_chunk_size = int(3680*0.8)

def split_file_into_chunks(file_data, max_chunk_size):
    chunks = []
    for i in range(0, len(file_data), max_chunk_size):
        chunks.append(file_data[i:i + max_chunk_size])
    return chunks


def generate_qr_codes(chunks, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for idx, chunk in enumerate(chunks):
        qr = qrcode.QRCode(
            version=40, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4
        )
        qr.add_data(chunk)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(os.path.join(output_directory, f"qr_code_{idx + 1}.png"))


def main():
    filename = input("Enter the file path: ")
    output_directory = input("Enter the output directory for QR codes: ")

    with open(filename, 'rb') as file:
        file_data = file.read()

    # Convert the binary data to a base64 string
    b64_data = base64.b64encode(file_data).decode("utf-8")

    chunks = split_file_into_chunks(b64_data, max_chunk_size)

    # Prepend the total number of chunks and the current chunk number
    chunks_with_info = [f"{len(chunks)}|{idx + 1}|{chunk}" for idx, chunk in enumerate(chunks)]

    generate_qr_codes(chunks_with_info, output_directory)
    print(f"Generated QR codes for {len(chunks)} chunks in {output_directory}.")


if __name__ == "__main__":
    main()
