# MITRA Sentence Aligner lightweight API client

This repository contains the script to align sentences from two text files using the MITRA API to facilitate a more efficient collaboration between the FGS data collection team and MITRA. The script reads two text files, splits them into lists of sentences, sends these lists to our API for alignment, and writes the returned data to a TSV file.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dharmamitra/mitra-aligner-client
    cd mitra-aligner-client
    ```

2. Install the required Python packages:
    ```bash
    pip install requests
    ```

## Usage

The script `align.py` takes three command-line parameters:
- `--input-a`: Path to the first input text file. Each line should be a separate sentence. This can be either Chinese or English.
- `--input-b`: Path to the second input text file. Each line should be a separate sentence. This can be either Chinese or English.
- `--output`: Path to the output TSV file.

### Example

Run the script with the required parameters as follows:
```bash
python align.py --input-a <path_to_first_text_file> --input-b <path_to_second_text_file> --output <path_to_output_tsv_file>
```
Please be aware that depending on the length of the files, this can take a while to complete. A file with a few hundred lines input and output can take a few minutes, files with thousands of lines can take much longer.  
The aligner is already using GPUs and optimized for performance, its difficult to make it faster than this! 

