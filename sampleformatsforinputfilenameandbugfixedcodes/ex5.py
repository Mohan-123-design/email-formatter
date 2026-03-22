import pandas as pd
import re

# Load your CSV file
df = pd.read_csv("inputfile3.csv")

def split_name_creds(name):
    # Convert to string and handle NaN or empty
    if pd.isna(name):
        return "", "", "", ""
    name = str(name)

    # Credentials regex pattern
    creds_pattern = r'\b(MD|DO|PhD|DNP|FNP-BC|BSN|RN|MPH|MSc|MBA|MHA|JD|MD, MPH|M\.D\.|D\.O\.)\b'
    creds = re.findall(creds_pattern, name, flags=re.IGNORECASE)
    creds_str = ", ".join(creds) if creds else ""
    
    # Remove credentials from name
    name_only = re.sub(creds_pattern, '', name, flags=re.IGNORECASE).strip()
    # Remove trailing commas
    name_only = name_only.split(",")[0].strip()

    # Split by space/hyphen/apostrophe
    tokens = re.split(r"[ \-']", name_only)

    if len(tokens) == 1:
        return tokens[0], "", "", creds_str
    elif len(tokens) == 2:
        return tokens[0], "", tokens[1], creds_str
    else:
        return tokens[0], " ".join(tokens[1:-1]), tokens[-1], creds_str

def create_email(first, last, domain):
    if not first or not last or not domain:
        return ""
    return f"{first[0].lower()}{last.lower()}@{domain.lower()}"

df[['FirstName', 'MiddleName', 'LastName', 'Credentials']] = df['Name'].apply(lambda x: pd.Series(split_name_creds(x)))
df['email'] = df.apply(lambda row: create_email(row['FirstName'], row['LastName'], row['domain name']), axis=1)

df.to_csv("outputfile3.csv", index=False)
