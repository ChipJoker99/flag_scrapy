import os
import requests
import json
from datetime import datetime
import pycountry
from pycountry_convert import country_alpha3_to_country_alpha2

with open('config.json', 'r') as f:
    config = json.load(f)

base_url = config['base_url']
destination_folder = config['destination_folder']

with open('file_names.json', 'r') as f:
    file_names = json.load(f)

def create_svg_flag(country_code, file_name, destination_folder):
    try:
        alpha_2_code = country_alpha3_to_country_alpha2(country_code)
        country = pycountry.countries.get(alpha_2=alpha_2_code)
        flag_svg = f"https://flagcdn.com/{alpha_2_code.lower()}.svg"
        response = requests.get(flag_svg)
        if response.status_code == 200:
            svg_file_name = f"{file_name}.svg" if not file_name.endswith('.svg') else file_name
            with open(os.path.join(destination_folder, svg_file_name), 'wb') as file:
                file.write(response.content)
            print(f"CREATED SVG FOR {country.name} in {destination_folder}")
            return country.name
        else:
            print(f"ERROR WITH DOWNLOADING FLAG FOR {country.name}: {response.status_code}")
            return None
    except KeyError:
        print(f"COUNTRY CODE {country_code} NOT FOUND")
        return None

log_folder = "logs"
os.makedirs(log_folder, exist_ok=True)

now = datetime.now()
log_file = f"{log_folder}/process_log_{now.strftime('%Y%m%d-%H%M%S')}.log"

os.makedirs(destination_folder, exist_ok=True)

for i, file_name in enumerate(file_names, start=1):
    country_code = file_name.split('.')[0].upper()
    svg_file_name = f"{file_name}.svg" if not file_name.endswith('.svg') else file_name
    url = f"{base_url}{svg_file_name}"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S%m')
    with open(log_file, 'a') as log:
        log.write(f"{timestamp} - {i}. LINK RECEIVED: {url}\n")
        log.write(f"{timestamp} - {i}. FILE NAME RECEIVED: {svg_file_name}\n")
        log.write(f"{timestamp} - {i}. SEARCHING FOR THE FILE...\n")
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(destination_folder, svg_file_name), 'wb') as file:
            file.write(response.content)
        print(f"FILE DOWNLOADED: {svg_file_name} in {destination_folder}: STATUS CODE {response.status_code}")
        with open(log_file, 'a') as log:
            log.write(f"{timestamp} - {i}. FILE FOUND: {svg_file_name} - STATUS CODE {response.status_code}\n")
            log.write(f"{timestamp} - {i}. FILE DOWNLOADED: {svg_file_name} in {destination_folder}\n")
    else:
        print(f"FILE {svg_file_name} NOT FOUND: ERROR {response.status_code}")
        with open(log_file, 'a') as log:
            log.write(f"{timestamp} - {i}. FILE {svg_file_name} NOT FOUND: ERROR {response.status_code}\n")
        country_name = create_svg_flag(country_code, svg_file_name, destination_folder)
        if country_name:
            with open(log_file, 'a') as log:
                log.write(f"{timestamp} - {i}. CREATED SVG {svg_file_name} FOR {country_name}\n")

print(f"\n\nLOG CREATED IN {log_file}\n")
