# QR Storage

## This repository contains a set of two Python scripts which fulfill automatic encoding/decoding duties to and from version 40 QR codes.

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
