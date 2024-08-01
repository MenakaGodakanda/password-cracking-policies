# Password Cracking Policies - Version 1

Demonstrate the importance of strong password policies by performing password cracking exercises.

## Features

### Hashing the Sample Passwords
- **Objective**: To create a file of hashed passwords that simulate the kind of data an attacker might obtain.
- **Implementation**:
  - Passwords are hashed using the SHA-256 algorithm.
  - The hashed passwords are saved to a file named `hashed-passwords.txt`.

### Cracking the Hashed Passwords
- **Objective**: To simulate a password cracking attack using tools like John the Ripper or Hashcat.
- **Implementation**:
  - Tools are used to attempt cracking the hashed passwords using the sample password list.

### Analyzing Cracked Passwords
- **Objective**: To analyze the effectiveness of different passwords and visualize the data.
- **Implementation**:
  - A script reads the cracked passwords and generates a histogram of password lengths.

### Developing Strong Password Policies
- **Objective**: To develop strong password policies based on the analysis of the cracked passwords.
- **Considerations**:
  - Minimum password length
  - Complexity requirements (use of uppercase, lowercase, numbers, special characters)
  - Avoiding common passwords
  - Implementing multi-factor authentication
  - Regular password changes

## Coding

### Password Hashes Generation (`password_hashes.py`)

#### 1. Importing Libraries
- **hashlib**: This is a built-in Python library used for secure hashes and message digests. It includes common hashing algorithms such as SHA-256, SHA-1, MD5, etc.

#### 2. Defining a Function to Hash Passwords
- **hash_password(password)**: This function takes a plaintext password as input.
  - **password.encode()**: Converts the plaintext password from a string to bytes because the `hashlib` functions work with byte data.
  - **hashlib.sha256()**: Applies the SHA-256 hash function to the encoded password bytes.
  - **hexdigest()**: Converts the resulting hash to a hexadecimal string representation, making it easier to store and compare.

#### 3. List of Passwords
- **passwords**: A list of common weak passwords to demonstrate the hashing process.

#### 4. Writing Passwords to a File
- **open('password-list.txt', 'w')**: Opens a file named `password-list.txt` in write mode. If the file doesn't exist, it will be created. If it does exist, it will be overwritten.
- **f.write(f"{password}\n")**: Writes each password from the `passwords` list to the file, each on a new line.

#### 5. Hashing Passwords and Writing to a File
- **open('hashed-passwords.txt', 'w')**: Opens a file named `hashed-passwords.txt` in write mode.
- **hash_password(password)**: Calls the previously defined function to hash the current password.
- **f.write(f"{hashed_password}\n")**: Writes each hashed password to the file, each on a new line.
- **print(...)**: Outputs a message to indicate that the hashed passwords have been successfully generated and saved to the file.

### Analyze Cracked Passwords (`password_analysis.py`)

#### 1. Importing Libraries
- **matplotlib.pyplot**: This is a collection of functions in the popular `matplotlib` library, which is used for creating static, animated, and interactive visualizations in Python. Here, it will be used to create a histogram of password lengths.

#### 2. Defining a Function to Read Cracked Passwords
- **read_cracked_passwords(file)**: This function reads a file containing cracked passwords and extracts the passwords.
  - **open(file, 'r')**: Opens the file in read mode.
  - **f.readlines()**: Reads all lines from the file into a list.
  - **if ':' in line**: Ensures that the line contains a colon : character, which is assumed to separate some identifier from the password.
  - **line.split(':')[1].strip()**:
    - **line.split(':')**: Splits the line at the colon, resulting in a list.
    - **[1]**: Takes the second element of this list, which is the password.
    - **strip()**: Removes any leading or trailing whitespace from the password.
  - The function returns a list of passwords extracted from the file.

#### 3. Defining a Function to Plot Password Strength
- **plot_password_strength(passwords)**: This function creates a histogram to visualize the distribution of password lengths.
  - **[len(p) for p in passwords if p]**: Creates a list of the lengths of the passwords, ensuring that only non-empty passwords are considered.
  - **plt.hist(lengths, bins=range(min(lengths), max(lengths) + 2), edgecolor='black')**:
    - **plt.hist()**: Creates a histogram.
    - **lengths**: The data to plot, which are the lengths of the passwords.
    - **bins=range(min(lengths), max(lengths) + 2)**: Specifies the bins for the histogram. `range(min(lengths), max(lengths) + 2)` creates a range of bin edges from the minimum to the maximum length + 1. The `+ 2` ensures an additional bin edge to capture the last length properly.
    - **edgecolor='black'**: Sets the color of the edges of the bars to black for better visibility.
  - **plt.title('Password Length Distribution')**: Sets the title of the plot.
  - **plt.xlabel('Password Length')**: Labels the x-axis as "Password Length".
  - **plt.ylabel('Frequency')**: Labels the y-axis as "Frequency".
  - **plt.xticks(range(min(lengths), max(lengths) + 1))**: Sets the ticks on the x-axis to display every password length within the range.
  - **plt.grid(True)**: Adds a grid to the plot for better readability.
  - **plt.show()**: Displays the plot.

#### 4. Main Execution
- **cracked_passwords = read_cracked_passwords('cracked-passwords.txt')**: Calls the `read_cracked_passwords` function to read and extract passwords from the specified file. Replace `'cracked-passwords.txt'` with the path to your actual file.
- **plot_password_strength(cracked_passwords)**: Calls the `plot_password_strength` function to create and display the histogram of the password lengths.
