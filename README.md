# QR Storage

## This repository contains a set of two Python scripts which fulfill automatic encoding/decoding duties to and from version 40 QR codes.
#### The logic is very straightforward - the file fed into the encoder is first turned into Base64, then split into adequate chunks. A preamble is added to the first chunk in the following format:
```num_chunks, chunk_number, chunk_data = data.split('|', 2)```

#### The complete chunked dataset with the preamble is subsequently turned into QR codes inside a folder the user chooses.

#### The decoder is the exact same process in reverse.
