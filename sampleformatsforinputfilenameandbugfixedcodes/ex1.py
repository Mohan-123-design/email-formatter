import csv

def process_name(name_str):
    # Split on commas to separate credentials, if any
    parts = name_str.split(',')
    name = parts[0].strip()
    credentials = ','.join([p.strip() for p in parts[1:]]) if len(parts) > 1 else ''
    
    # Split name into tokens to extract first, middle, last names
    name_tokens = name.split()
    if len(name_tokens) == 2:
        first, last = name_tokens
        middle = ''
    elif len(name_tokens) == 3:
        first, middle, last = name_tokens
    elif len(name_tokens) > 3:
        first = name_tokens[0]
        middle = ' '.join(name_tokens[1:-1])
        last = name_tokens[-1]
    else:
        first = name_tokens[0]
        last = ''
        middle = ''
    
    return first, last, middle, credentials

def main():
    input_file = 'inputfile.csv'
    output_file = 'doctors_output.csv'
    domain = 'sutterhealth.org'

    with open(input_file, newline='', encoding='utf-8') as infile, \
            open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write header
        writer.writerow(['First Name', 'Last Name', 'Middle Name', 'Credentials', 'Email'])
        
        for row in reader:
            if not row:
                continue
            name_line = row[0]
            first, last, middle, credentials = process_name(name_line)
            
            # Construct email only if last name exists
            if last:
                email = f"{first.lower()}.{last.lower()}@{domain}"
            else:
                email = ''
            
            writer.writerow([first, last, middle, credentials, email])

if __name__ == "__main__":
    main()
