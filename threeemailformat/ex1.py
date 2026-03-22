import csv
import re

def split_name_credential(full_name):
    # Remove trailing spaces
    full_name = full_name.strip()
    # Split on comma to separate credentials
    if ',' in full_name:
        name_part, credential_part = full_name.split(',', 1)
        credential_part = credential_part.strip()
    else:
        name_part = full_name
        credential_part = ''
    name_part = name_part.strip()

    # Split by spaces, handle middle names and apostrophes
    name_tokens = name_part.split()

    first_name = name_tokens[0] if len(name_tokens) > 0 else ""
    last_name = ""
    middle_name = ""

    if len(name_tokens) == 1:
        last_name = ""
    elif len(name_tokens) == 2:
        last_name = name_tokens[1]
    else:
        middle_name = " ".join(name_tokens[1:-1])
        last_name = name_tokens[-1]

    return first_name, last_name, middle_name, credential_part

def normalize_for_email(text):
    # Lowercase and remove spaces, special characters except apostrophes are removed for email purposes
    text = text.lower()
    text = text.replace(" ", "")
    # For apostrophes in email, some systems allow them, but safer to remove or replace with empty or underscore
    text = text.replace("'", "")
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("-", "")
    return text

input_file = 'inputfile3.csv'  # Assuming input file is CSV
output_file = 'cumedicineemails.csv'
domain = 'cumedicine.us'

output_rows = []
header = ['First Name', 'Last Name', 'Middle Name', 'Credentials', 'Email Type 1', 'Email Type 2', 'Email Type 3']

with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    for row in reader:
        # Assuming the full name with credentials is in the first column for each row
        full_name = row[0]
        first, last, middle, cred = split_name_credential(full_name)

        # Normalize parts for email
        first_norm = normalize_for_email(first)
        last_norm = normalize_for_email(last)

        # Email Type 1: first.last@domain
        email1 = f"{first_norm}.{last_norm}@{domain}"

        # Email Type 2: firstinitial + last@domain
        first_initial = first_norm[0] if first_norm else ""
        email2 = f"{first_initial}{last_norm}@{domain}"

        # Email Type 3: last + _ + firstinitial@domain
        email3 = f"{last_norm}_{first_initial}@{domain}"

        output_rows.append([first, last, middle, cred, email1, email2, email3])

with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(output_rows)

print(f"Processed {len(output_rows)} entries and saved to '{output_file}'")
