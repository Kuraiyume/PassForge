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
