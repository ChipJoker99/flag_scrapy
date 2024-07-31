# Flag Downloader and SVG Creator

This Python script downloads SVG files of country flags from a specified URL. If a flag file is not found, it automatically generates an SVG file for the corresponding country using the country code.

## Features
- Reads configuration and file names from JSON files.
- Downloads SVG files from a specified base URL.
- Creates a log file with detailed information about each process.
- Generates SVG files for missing flags using the `pycountry` and `pycountry_convert` libraries.


## How to Use
1. Ensure you have the required libraries installed:
   
   ```bash
   pip install requests pycountry pycountry-convert

3. Modify `config.json` with the following structure:
   
   ```json
     {
      "base_url": "https://www.url.com/folder1/folder2/folder3/",
      "destination_folder": "local/destination/folder"
     }
   
4. Modify `file_names.json` with the list of file names:
   
   ```json
    [
        "not_existing_flag.svg", "nld", "gbr.svg"
    ]

6. Run the script

   ```bash
   python flag_scrape.py

## Example Log Entry:

Here is an example of the log entry

      2024-07-31 16:16:0707 - 1. LINK RECEIVED: https://www.url.com/folder1/folder2/folder3/not_existing_flag.svg
      2024-07-31 16:16:0707 - 1. FILE NAME RECEIVED: not_existing_flag.svg
      2024-07-31 16:16:0707 - 1. SEARCHING FOR THE FILE...
      2024-07-31 16:16:0707 - 1. FILE not_existing_flag.svg NOT FOUND: ERROR 404
      
      2024-07-31 16:16:0707 - 2. LINK RECEIVED: https://www.url.com/folder1/folder2/folder3/nld.svg
      2024-07-31 16:16:0707 - 2. FILE NAME RECEIVED: nld.svg
      2024-07-31 16:16:0707 - 2. SEARCHING FOR THE FILE...
      2024-07-31 16:16:0707 - 2. FILE nld.svg NOT FOUND: ERROR 404
      2024-07-31 16:16:0707 - 2. CREATED SVG nld.svg FOR Netherlands
      
      2024-07-31 16:16:0807 - 3. LINK RECEIVED: https://www.url.com/folder1/folder2/folder3/gbr.svg
      2024-07-31 16:16:0807 - 3. FILE NAME RECEIVED: gbr.svg
      2024-07-31 16:16:0807 - 3. SEARCHING FOR THE FILE...
      2024-07-31 16:16:0807 - 3. FILE FOUND: gbr.svg - STATUS CODE 200
      2024-07-31 16:16:0807 - 3. FILE DOWNLOADED: gbr.svg in local/destination/folder

## Install Requirements
In order to install requirements, run the script
      
      python flag_scrape.py



## Notes
- The script creates a `logs` folder to store log files.
- If a flag file is not found, the script generates an SVG file with the country’s flag using the `pycountry` and `pycountry_convert` libraries.

