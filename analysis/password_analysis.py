import matplotlib.pyplot as plt

def read_cracked_passwords(file):
    with open(file, 'r') as f:
        return [line.split(':')[1].strip() for line in f.readlines() if ':' in line]

def plot_password_strength(passwords):
    lengths = [len(p) for p in passwords if p]  # Ensure non-empty passwords
    plt.hist(lengths, bins=range(min(lengths), max(lengths) + 2), edgecolor='black')
    plt.title('Password Length Distribution')
    plt.xlabel('Password Length')
    plt.ylabel('Frequency')
    plt.xticks(range(min(lengths), max(lengths) + 1))
    plt.grid(True)
    plt.show()

# Replace 'cracked-passwords.txt' with the correct path to your file
cracked_passwords = read_cracked_passwords('cracked-passwords.txt')
plot_password_strength(cracked_passwords)
