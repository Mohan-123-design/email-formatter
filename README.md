# Email Formatter

Python scripts that generate formatted corporate email addresses from name data. Supports multiple email format conventions (firstname.lastname, flastname, etc.) — with credential extraction and honorific stripping built in.

## Use Case

Given a list of names like `"Dr. Sarah Johnson, MD"`, generate:
- `sarah.johnson@company.com` (dot format)
- `sjohnson@company.com` (initial format)
- `johnson.sarah@company.com` (reversed format)

## Scripts

| File/Folder | Format | Example Output |
|-------------|--------|----------------|
| `altais_email_formatter.py` | dot + initial | `john.doe@altais.com`, `jdoe@altais.com` |
| `emailformat1(base format)/` | base dot format | `firstname.lastname@domain.com` |
| `firstletter,lastnameformat/` | initial + last | `flastname@domain.com` |
| `lastname,firstletterformat/` | last + initial | `lastnamef@domain.com` |
| `threeemailformat/` | all 3 formats at once | generates all variants |
| `sampleformatsforinputfilenameandbugfixedcodes/` | bug-fixed versions | tested & stable |

## Key Features

- **Credential extraction** — strips `M.D.`, `PhD`, `RN`, etc. into a separate column
- **Honorific removal** — removes `Dr.`, `Prof.`, `Mr.`, `Ms.` before processing
- **Middle name handling** — correctly separates first, middle, last
- **Dual output** — generates both email format variants in one run

## Usage

```bash
pip install pandas

# Place your input file as inputfile1.csv with a "Name" column
python altais_email_formatter.py
```

## Input Format

```csv
Name
Dr. John Smith MD
Sarah Johnson PhD
Michael Robert Brown
```

## Output Format

```csv
Name,FirstName,MiddleName,LastName,Credentials,email_dot,email_initial
Dr. John Smith MD,John,,Smith,MD,john.smith@altais.com,jsmith@altais.com
```

## Tech Stack

- Python
- Pandas
- Regular expressions (re)
