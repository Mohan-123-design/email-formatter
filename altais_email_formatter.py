import pandas as pd
import re

def split_name_and_credential(name):
    # Handle missing values
    if pd.isna(name) or not str(name).strip():
        return "", "", "", ""

    name = str(name).strip()

    # Find credentials at the end (e.g., "M.D." etc)
    cred_pattern = r'(,\s*)?(M\.D\.|MD|DO|PhD|DNP|FNP-BC|BSN|RN|MPH|MSc|MBA|MHA|JD)$'
    cred_match = re.search(cred_pattern, name)
    credentials = ""
    if cred_match:
        credentials = cred_match.group(2)  # extract only the degree
        name = name[:cred_match.start()].strip()  # remove from name

    # Remove honorifics at the start
    name = re.sub(r'^(Dr\.|Prof\.|Mr\.|Ms\.)\s+', '', name, flags=re.IGNORECASE)

    # Split tokens
    parts = name.split()
    if len(parts) == 0:
        return "", "", "", credentials
    elif len(parts) == 1:
        return parts[0], "", "", credentials
    elif len(parts) == 2:
        return parts[0], "", parts[1], credentials
    else:
        first = parts[0]
        last = parts[-1]
        middle = " ".join(parts[1:-1])
        return first, middle, last, credentials

def email_dot(first, last):
    if not first or not last:
        return ""
    return f"{first.lower()}.{last.lower()}@altais.com"

def email_initial(first, last):
    if not first or not last:
        return ""
    return f"{first[0].lower()}{last.lower()}@altais.com"

# Load the input CSV file
df = pd.read_csv("inputfile1.csv")

# Apply split function to Name column
df[['FirstName', 'MiddleName', 'LastName', 'Credentials']] = df['Name'].apply(lambda x: pd.Series(split_name_and_credential(x)))

# Generate both email formats
df['email_dot'] = df.apply(lambda row: email_dot(row['FirstName'], row['LastName']), axis=1)
df['email_initial'] = df.apply(lambda row: email_initial(row['FirstName'], row['LastName']), axis=1)

# Save to CSV
df.to_csv("browntolandtoaltais.csv", index=False)
