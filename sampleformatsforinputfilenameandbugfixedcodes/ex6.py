import csv

input_filename = 'inputfile1.csv'
output_filename = 'catholicemails.csv'  # updated output filename
domain = 'chsli.org'  # updated domain

def parse_name_and_credentials(fullname_cred):
    if not fullname_cred.strip():
        return '', '', '', ''
        
    if ',' in fullname_cred:
        name_part, credential_part = fullname_cred.split(',', 1)
        credential = credential_part.strip()
    else:
        name_part = fullname_cred
        credential = ''
        
    name_parts = name_part.strip().split()
    
    if len(name_parts) == 0:
        return '', '', '', credential
    
    first_name = name_parts[0]
    last_name = name_parts[-1] if len(name_parts) > 1 else ''
    middle_name = ' '.join(name_parts[1:-1]) if len(name_parts) > 2 else ''
    
    return first_name, middle_name, last_name, credential

with open(input_filename, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    writer.writerow(['First Name', 'Middle Name', 'Last Name', 'Credentials', 'Email'])
    
    for row in reader:
        if not row:
            continue
        full_name_cred = row[0].strip()
        if not full_name_cred:
            continue
        first, middle, last, cred = parse_name_and_credentials(full_name_cred)
        if first and last:
            email = f"{first.lower()}.{last.lower()}@{domain}"
        else:
            email = ''
        writer.writerow([first, middle, last, cred, email])
