# Flag Downloader and SVG Creator

This Python script downloads SVG files of country flags from a specified URL. If a flag file is not found, it automatically generates an SVG file for the corresponding country using the country code.

## Features:
- Reads configuration and file names from JSON files.
Downloads SVG files from a specified base URL.
Creates a log file with detailed information about each process.
Generates SVG files for missing flags using the `pycountry` and `pycountry_convert` libraries.


## How to Use:
1. Ensure you have the required libraries installed:
   ```bash
   pip install requests pycountry pycountry-convert

2. Modify `config.json` with the following structure:
   ```json
     {
      "base_url": "https://www.url.com/folder1/folder2/folder3/",
      "destination_folder": "local/destination/folder"
     }
   
3. Modify `file_names.json` with the list of file names:
   ```json
    [
        "file1.svg", "file2.svg", "file3.svg"
    ]

4. Run the script:
`python flag_scrape.py`

## Example Log Entry:
   `
      2024-07-31 14:49:3607 - 1. LINK RECEIVED: https://www.url.com/folder1/folder2/folder3/nld.svg
      2024-07-31 14:49:3607 - 1. FILE NAME RECEIVED: nld.svg
      2024-07-31 14:49:3607 - 1. SEARCHING FOR THE FILE...
      2024-07-31 14:49:3607 - 1. FILE nld.svg NOT FOUND: ERROR 404
      2024-07-31 14:49:3607 - 1. CREATED SVG nld.svg FOR "Netherlands"`

## Notes:
- The script creates a `logs` folder to store log files.
- If a flag file is not found, the script generates an SVG file with the country’s flag using the `pycountry` and `pycountry_convert` libraries.




