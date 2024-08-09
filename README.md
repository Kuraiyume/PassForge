# PassForge

PassForge is an advanced password generation tool designed to provide users with highly customizable and secure password options. It blends sophistication with flexibility, allowing users to craft passwords tailored to their specific needs, enhancing both security and usability in a user-friendly manner.

## Features

- Generate passwords with specific counts of digits, lowercase letters, uppercase letters, and special characters.
- Specify total length of the password, including optional prefixes and suffixes.
- Exclude certain characters from the password.
- Convert custom names to leet speak.
- Output passwords in plain text or JSON format.
- Evaluate and display password strength as a percentage.

## Installation

You can install PassForge using pip:

```bash
pip3 install passforge
```

## Available Parameters

```
                           ____
    ____  ____ ___________/ __/___  _________ ____
   / __ \/ __ `/ ___/ ___/ /_/ __ \/ ___/ __ `/ _ \
  / /_/ / /_/ (__  |__  ) __/ /_/ / /  / /_/ /  __/
 / .___/\__,_/____/____/_/  \____/_/   \__, /\___/
/_/                                   /____/v0.4
                                    veilwr4ith

usage: PassForge [-h] [-n NUMBERS] [-l LOWERCASE] [-u UPPERCASE] [-s SPECIAL_CHARS] [-a AMOUNT] [-o OUTPUT_FILE] [--output-format {txt,json}] [--exclude-chars EXCLUDE_CHARS]
                 [--prefix PREFIX] [--suffix SUFFIX] [--total-length TOTAL_LENGTH] [--seed SEED] [--custom CUSTOM]

Advanced Password Generator that generates customizable passwords with sophisticated options.

options:
  -h, --help            show this help message and exit
  -n NUMBERS, --numbers NUMBERS
                        Number of digits in the password
  -l LOWERCASE, --lowercase LOWERCASE
                        Number of lowercase characters in the password
  -u UPPERCASE, --uppercase UPPERCASE
                        Number of uppercase characters in the password
  -s SPECIAL_CHARS, --special-chars SPECIAL_CHARS
                        Number of special characters in the password
  -a AMOUNT, --amount AMOUNT
                        Number of passwords to generate
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        File to write the generated passwords to
  --output-format {txt,json}
                        Format of the output file (txt or json)
  --exclude-chars EXCLUDE_CHARS
                        Characters to exclude from the password
  --prefix PREFIX       Prefix to add to each password
  --suffix SUFFIX       Suffix to add to each password
  --total-length TOTAL_LENGTH
                        Total length of the password (including prefix and suffix) If 0, use specified counts
  --seed SEED           Seed for randomization to allow reproducible results
  --custom CUSTOM       Custom name for the password with leet speak conversion
```
## Usage

1. Generate a Password with Specific Counts
   ```bash
   passforge -n 2 -l 4 -u 2 -s 2
   ```
   *This generates a password with 2 digits, 4 lowercase letters, 2 uppercase letters, and 2 special characters.*
   
2. Generate a Password with a Total Length
   ```bash
   passforge --total-length 12
   ```
   *This generates a password with a total length of 12 characters, including any specified prefixes and suffixes.*

3. Exclude Certain Characters
   ```bash
   passforge -n 3 -l 2 -u 4 -s 3 or --total-length 12 --exclude-chars "0OIl"
   ```
   *This generates a password excluding the characters 0, O, I, and l.*

4. Add Prefix and Suffix
   ```bash
   passforge -n 3 -l 2 -u 4 -s 3 or --total-length 12 --prefix "start-" --suffix "-end"
   ```
   *This generates a password with the specified prefix and suffix.*

5. Convert a Custom Name to Leet Speak
   ```bash
   passforge --custom "example"
   ```
   *This generates a password based on the leet speak conversion of the custom name "example". (Note: All parameters cannot be applied in customized password)*

6. Output to a file
   ```bash
   passforge -n 3 -l 2 -u 4 -s 3 or --total-length 12 --output-file passwords --output-format txt
   ```
   *This generates passwords and saves them to passwords.txt in plain text format. You can also use json format.*

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes. Make sure to follow the code of conduct and ensure all tests pass before submitting.

## License

This project is licensed under the MIT License
