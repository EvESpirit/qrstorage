# QR Storage

## This repository contains a set of two Python scripts which fulfill automatic file encoding/decoding duties to and from version 40 QR codes.

## Theory
#### The logic is very straightforward - the file fed into the encoder is first turned into Base64, then split into adequate chunks. A preamble is added to the first chunk in the following format:
```num_chunks, chunk_number, chunk_data = data.split('|', 2)```

#### The complete chunked dataset with the preamble is subsequently turned into QR codes inside a folder the user chooses.

#### The decoder is the exact same process in reverse.

## Installation and usage

### 1. Clone this repository either with ```git clone https://github.com/EvESpirit/qrstorage/``` or using the green "Code" dropdown and selecting "Download ZIP".
### 2. Depending on which method you chose, either navigate to the directory or unzip the downloaded file and then navigate to it.
### 3. Install project requirements using ```pip install -r requirements.txt``` in your native CLI.
### 4. Run the desired script using ```python encoder.py``` or ```python decoder.py``` in your native CLI.
### 5. Follow on-screen instructions.

### Note that it's highly recommended to first compress whatever you're trying to represent as QR codes. I personally recommend CMIX v19 or ZPAQ, however, WinRAR seems sufficent for most practical uses, though obviously less overall data volume means less QR chunks. There is no source data manipulation code in this repository at all (no encryption, no real encapsulation, no version tags, no compression, no error correction) so user's due diligence is required for maximum usability. Both WinRAR and CMIX v19/ZPAQ offer an excellent source of every feature mentioned without me mostly unnecessarily bloating this elegant and short script.

### Please also note that the error correction part is also important. If any/all of your QR codes get damaged, the QR code's built-in error correction likely will not save you, since it's set to the minimum possible level to enable more data bits to be carried in a single chunk. The minimum QR code error correction level is only capable of recovering up to 7% of any given QR code chunk - which only works out to around 300 characters out of the roughly 4300 characters per chunk (including preamble data if the chunk in question happens to be the first one).
