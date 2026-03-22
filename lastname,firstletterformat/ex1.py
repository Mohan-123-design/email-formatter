import pandas as pd
from nameparser import HumanName

def parse_name(full_name):
    name = HumanName(full_name)
    return pd.Series([name.first, name.middle, name.last, name.suffix])

def generate_email(first_name, last_name, domain):
    clean_first = first_name.lower().replace(",", "").replace(" ", "").strip()
    clean_last = last_name.lower().replace(",", "").replace(" ", "").strip()
    clean_domain = domain.lower().strip()
    if clean_first and clean_last and clean_domain:
        return f"{clean_last}{clean_first[0]}@{clean_domain}"
    else:
        return ""

# Load input CSV
df = pd.read_csv("inputfile3.csv")

# Parse names to components
df[['First Name', 'Middle Name', 'Last Name', 'Credentials']] = df['Name'].apply(parse_name)

# Generate email addresses
df['Email'] = df.apply(lambda x: generate_email(x['First Name'], x['Last Name'], x['domain name']), axis=1)

# Save to output CSV
df.to_csv("outputemails1.csv", index=False)
