# Password-Generator
import random
import string
import pyperclip   # install with: pip install pyperclip

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True, exclude_similar=True):
    # Base character set
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/|`~" if use_symbols else ""
    
    # Combine character set
    all_chars = lower + upper + digits + symbols

    # Exclude similar characters (optional)
    if exclude_similar:
        for ch in "O0Il1":
            all_chars = all_chars.replace(ch, "")
    
    if not all_chars:
        raise ValueError("No characters available for password generation!")
    
    # Ensure password contains at least one from each selected category
    password = []
    if use_upper:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))
    
    # Fill the rest with random choices
    while len(password) < length:
        password.append(random.choice(all_chars))
    
    # Shuffle for randomness
    random.shuffle(password)
    return "".join(password)

# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    print("🔐 Advanced Password Generator 🔐")
    length = int(input("Enter password length (default 12): ") or 12)
    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"
    exclude_similar = input("Exclude similar characters (O/0, l/1)? (y/n): ").lower() == "y"
    
    password = generate_password(length, use_upper, use_digits, use_symbols, exclude_similar)
    
    print(f"\n✅ Your secure password is: {password}")
    
    # Copy to clipboard
    pyperclip.copy(password)
    print("📋 Password copied to clipboard!")
    
    # Save to file
    with open("generated_passwords.txt", "a") as f:
        f.write(password + "\n")
    print("💾 Password saved to generated_passwords.txt")
