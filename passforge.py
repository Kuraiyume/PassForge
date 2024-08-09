import argparse
import random
import string
import json
import sys
import secrets
import re

banner = r"""
                           ____
    ____  ____ ___________/ __/___  _________ ____
   / __ \/ __ `/ ___/ ___/ /_/ __ \/ ___/ __ `/ _ \
  / /_/ / /_/ (__  |__  ) __/ /_/ / /  / /_/ /  __/
 / .___/\__,_/____/____/_/  \____/_/   \__, /\___/
/_/                                   /____/v0.4
                                    veilwr4ith
"""

def validate_positive_int(value):
    """Ensure that a value is a positive integer."""
    ivalue = int(value)
    if ivalue < 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer.")
    return ivalue

def leet_speak_conversion(custom_string):
    """Convert a string to leet speak."""
    leet_mapping = {
        'a': '4', 'b': '8', 'c': '<', 'd': '|)', 'e': '3', 'f': '|=', 'g': '9',
        'h': '#', 'i': '!', 'j': '_|', 'k': '|<', 'l': '1', 'm': r'/\/\\', 'n': '^/',
        'o': '0', 'p': '|D', 'q': '9', 'r': '|2', 's': '$', 't': '7', 'u': '(_)',
        'v': r'\/', 'w': r'\/\/', 'x': '%', 'y': '`/', 'z': '2',
        'A': '4', 'B': '8', 'C': '<', 'D': '|)', 'E': '3', 'F': '|=', 'G': '9',
        'H': '#', 'I': '!', 'J': '_|', 'K': '|<', 'L': '1', 'M': r'/\/\\', 'N': '^/',
        'O': '0', 'P': '|D', 'Q': '9', 'R': '|2', 'S': '$', 'T': '7', 'U': '(_)',
        'V': r'\/', 'W': r'\/\/', 'X': '%', 'Y': '`/', 'Z': '2'
    }
    return ''.join(leet_mapping.get(c, c) for c in custom_string)

def generate_password(counts, pools, exclude_chars, prefix, suffix, total_length, secrets_generator, custom):
    """
    Generate a password based on specified counts, total length, or custom string.
    :param counts: Dictionary containing the count of each character type
    :param pools: Dictionary of character pools
    :param exclude_chars: Characters to exclude from the password
    :param prefix: Prefix to add to the password
    :param suffix: Suffix to add to the password
    :param total_length: Desired total length of the password
    :param secrets_generator: Random generator instance
    :param custom: Custom string for leet speak conversion
    :return: Generated password
    """
    if custom:
        return leet_speak_conversion(custom)
    # Create a string of available characters by excluding specified characters
    available_chars = ''.join(c for c in ''.join(pools.values()) if c not in exclude_chars)
    # Ensure there are available characters left after exclusion
    if not available_chars:
        print("[-] No available characters left after applying exclusions.")
        sys.exit(1)
    # Ensure at least one character from each selected pool is present
    password_chars = []
    if total_length > 0:
        for pool in pools.values():
            if pool:
                # Filter pool to exclude unwanted characters
                filtered_pool = ''.join(c for c in pool if c not in exclude_chars)
                if filtered_pool:
                    password_chars.append(secrets_generator.choice(filtered_pool))
        # Fill the rest of the password with random characters from the combined pool
        remaining_length = total_length - len(password_chars) - len(prefix) - len(suffix)
        if remaining_length > 0:
            password_chars.extend(secrets_generator.choice(available_chars) for _ in range(remaining_length))
    else:
        # Use counts to determine the exact number of each character type
        for char_type, count in counts.items():
            if count > 0:
                # Filter pool to exclude unwanted characters
                filtered_pool = ''.join(c for c in pools[char_type] if c not in exclude_chars)
                if filtered_pool:
                    password_chars.extend(secrets_generator.choice(filtered_pool) for _ in range(count))
    # Shuffle the characters and add prefix and suffix
    random.shuffle(password_chars)
    password = f"{prefix}{''.join(password_chars)}{suffix}"
    # Ensure the password meets the total length requirement
    if total_length > 0 and len(password) < total_length:
        additional_chars = [secrets_generator.choice(available_chars) for _ in range(total_length - len(password))]
        password += ''.join(additional_chars)
    return password

def evaluate_password_strength(password):
    """
    Evaluate the strength of a password based on its complexity.
    :param password: Password to evaluate
    :return: Strength percentage
    """
    score = 0
    length = len(password)
    if length >= 8:
        score += 10
    if re.search(r'[a-z]', password):
        score += 10
    if re.search(r'[A-Z]', password):
        score += 10
    if re.search(r'[0-9]', password):
        score += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 10
    # Length contributes more to strength
    if length >= 12:
        score += 20
    if length >= 16:
        score += 20
    if length >= 20:
        score += 20
    return min(score, 100)  # Ensure the score does not exceed 100%

def parse_arguments():
    """Parse command-line arguments."""
    print(banner)
    parser = argparse.ArgumentParser(
        prog='PassForge',
        description='Advanced Password Generator that generates customizable passwords with sophisticated options.'
    )
    parser.add_argument("-n", "--numbers", default=0, type=validate_positive_int, help="Number of digits in the password")
    parser.add_argument("-l", "--lowercase", default=0, type=validate_positive_int, help="Number of lowercase characters in the password")
    parser.add_argument("-u", "--uppercase", default=0, type=validate_positive_int, help="Number of uppercase characters in the password")
    parser.add_argument("-s", "--special-chars", default=0, type=validate_positive_int, help="Number of special characters in the password")
    parser.add_argument("-a", "--amount", default=1, type=validate_positive_int, help="Number of passwords to generate")
    parser.add_argument("-o", "--output-file", help="File to write the generated passwords to")
    parser.add_argument("--output-format", choices=['txt', 'json'], default='txt', help="Format of the output file (txt or json)")
    parser.add_argument("--exclude-chars", default='', type=str, help="Characters to exclude from the password")
    parser.add_argument("--prefix", default='', type=str, help="Prefix to add to each password")
    parser.add_argument("--suffix", default='', type=str, help="Suffix to add to each password")
    parser.add_argument("--total-length", default=0, type=validate_positive_int, help="Total length of the password (including prefix and suffix) If 0, use specified counts")
    parser.add_argument("--seed", type=int, help="Seed for randomization to allow reproducible results")
    parser.add_argument("--custom", default='', type=str, help="Custom name for the password with leet speak conversion")
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return args

def main():
    args = parse_arguments()
    if args.custom and (args.amount > 1 or args.prefix or args.suffix or args.numbers > 0 or
            args.lowercase > 0 or args.uppercase > 0 or args.special_chars > 0 or
            args.total_length > 0 or args.exclude_chars or args.output_file or
            args.seed is not None):
        print("[-] All parameters cannot be applied in customized password.")
        sys.exit(1)
    if args.seed is not None:
        random.seed(args.seed)
        secrets_generator = random.Random(args.seed)
    else:
        secrets_generator = secrets.SystemRandom()
    pools = {
        'digits': string.digits if args.numbers > 0 else '',
        'lowercase': string.ascii_lowercase if args.lowercase > 0 else '',
        'uppercase': string.ascii_uppercase if args.uppercase > 0 else '',
        'special': string.punctuation if args.special_chars > 0 else ''
    }
    # Ensure at least one pool is included
    if not any(pools.values()) and not args.custom:
        pools = {
            'digits': string.digits,
            'lowercase': string.ascii_lowercase,
            'uppercase': string.ascii_uppercase,
            'special': string.punctuation
        }
    passwords = []
    for _ in range(args.amount):
        try:
            counts = {
                'digits': args.numbers,
                'lowercase': args.lowercase,
                'uppercase': args.uppercase,
                'special': args.special_chars
            }
            password = generate_password(
                counts,
                pools,
                args.exclude_chars,
                args.prefix,
                args.suffix,
                args.total_length,
                secrets_generator,
                args.custom
            )
            # Evaluate password strength
            strength = evaluate_password_strength(password)
            passwords.append(f"{password} ({strength:.1f}%)")
        except ValueError as e:
            print(f"Error generating password: {e}", file=sys.stderr)
            sys.exit(1)
    print("[+] Generated Passwords:")
    output = '\n'.join(passwords)
    if args.output_file:
        expected_extension = f".{args.output_format}"
        if not args.output_file.endswith(expected_extension):
            args.output_file += expected_extension
        if args.output_format == 'json':
            output_data = {"passwords": passwords}
            with open(args.output_file, 'w') as f:
                json.dump(output_data, f, indent=4)
                f.write('\n')
        else:
            with open(args.output_file, 'w') as f:
                f.write(output)
                if passwords:
                    f.write('\n')
    print(output)

if __name__ == "__main__":
    main()

