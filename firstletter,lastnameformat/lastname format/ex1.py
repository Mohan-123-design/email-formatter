import pandas as pd
import re

# Load the input CSV file (update path if necessary)
df = pd.read_csv("inputfile3.csv")

def split_name(name):
    # Handle missing values
    if pd.isna(name):
        return "", "", "", ""
    name = str(name).strip()
    credential = ""
    # Extract credential (e.g., "Dr." at the start)
    match = re.match(r'^(Dr\.|Prof\.|Mr\.|Ms\.)\s+', name)
    if match:
        credential = match.group(1)
        name = name[len(match.group(0)):]  # Remove credential from start
    else:
        credential = ""
    # Split name into tokens separated by spaces
    tokens = name.split()
    # Assign names based on number of tokens
    if len(tokens) == 1:
        first, middle, last = tokens[0], "", ""
    elif len(tokens) == 2:
        first, middle, last = tokens[0], "", tokens[1]
    elif len(tokens) == 3:
        first, middle, last = tokens[0], tokens[1], tokens[2]
    else:
        first = tokens[0]
        middle = " ".join(tokens[1:-1])
        last = tokens[-1]
    return first, middle, last, credential

def generate_email(first, last, domain):
    if not first or not last or not domain:
        return ""
    return f"{first[0].lower()}{last.lower()}@{domain.lower()}"

# Split name columns
df[['FirstName', 'MiddleName', 'LastName', 'Credentials']] = df['Name'].apply(lambda x: pd.Series(split_name(x)))

# Generate both email formats
df['email_ccphp'] = df.apply(lambda row: generate_email(row['FirstName'], row['LastName'], "ccphp.net"), axis=1)
# df['email_castleconnolly'] = df.apply(lambda row: generate_email(row['FirstName'], row['LastName'], "castleconnolly.com"), axis=1)

# Save to CSV
df.to_csv("outputfile3.csv", index=False)
