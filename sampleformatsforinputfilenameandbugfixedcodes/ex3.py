import pandas as pd
import re

# Load input CSV file (update filename if needed)
df = pd.read_csv("inputfile3.csv")

def split_name_creds(name):
    # Separate credentials (common medical degrees) from names
    creds_pattern = r'\b(MD|DO|PhD|DNP|FNP-BC|BSN|RN|MPH|MSc|MBA|MHA|JD|MD, MPH|M\.D\.|D\.O\.)\b'
    creds = re.findall(creds_pattern, name, flags=re.IGNORECASE)
    creds_str = ", ".join(creds) if creds else ""
    
    # Remove credentials from name to isolate pure name part
    name_only = re.sub(creds_pattern, '', name, flags=re.IGNORECASE).strip()
    
    # Remove commas (like "John D. Smith, MD" -> "John D. Smith")
    if "," in name_only:
        name_only = name_only.split(",")[0].strip()

    # Split the name into parts by spaces/hyphens/apostrophes where needed
    # Treat first token as first name, last token as last name, everything in the middle as middle name
    name_tokens = re.split(r"[ \-']", name_only)
    if len(name_tokens) == 1:
        first, middle, last = name_tokens[0], "", ""
    elif len(name_tokens) == 2:
        first, middle, last = name_tokens[0], "", name_tokens[1]
    else:
        first, middle, last = name_tokens[0], " ".join(name_tokens[1:-1]), name_tokens[-1]
    
    return first.strip(), middle.strip(), last.strip(), creds_str

def create_email(first, last, domain):
    if not first or not last or not domain:
        return ""
    return f"{first[0].lower()}{last.lower()}@{domain.lower()}"

# Apply split and email generation to dataframe
df[['FirstName', 'MiddleName', 'LastName', 'Credentials']] = df['Name'].apply(lambda x: pd.Series(split_name_creds(x)))
df['email'] = df.apply(lambda row: create_email(row['FirstName'], row['LastName'], row['domain name']), axis=1)

# Save to CSV with all columns
df.to_csv("outputfile3.csv", index=False)
