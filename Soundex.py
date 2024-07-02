def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def remove_non_initial_vowels(name):
    vowels = "AEIOUYHW"
    return name[0] + ''.join(c for c in name[1:] if c.upper() not in vowels)

def encode(name):
    return ''.join(get_soundex_code(c) for c in name)

def remove_consecutive_duplicates(encoded_name):
    result = [encoded_name[0]]
    for i in range(1, len(encoded_name)):
        if encoded_name[i] != encoded_name[i - 1]:
            result.append(encoded_name[i])
    return ''.join(result)

def generate_soundex(name):
    if not isinstance(name, str) or not name:
        return ""
    
    name = name.upper()
    name = remove_non_initial_vowels(name)
    encoded_name = encode(name)
    encoded_name = remove_consecutive_duplicates(encoded_name)
    
    # Retain the first letter and pad with zeros if necessary
    soundex = name[0] + encoded_name[1:4].ljust(3, '0')
    
    return soundex

# Example usage
if __name__ == "__main__":
    name = "Example"
    print(f"Soundex code for {name}: {generate_soundex(name)}")
