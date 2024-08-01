# password-cracking-policies
Demonstrate the importance of strong password policies by performing password-cracking exercises.<br>
<a href="https://github.com/MenakaGodakanda/password-cracking-policies/blob/main/Project_Description.md">Project Description</a>

## Overview
<img width="1285" alt="Screenshot 2024-08-01 at 2 56 40 PM" src="https://github.com/user-attachments/assets/b4b1dc57-81f5-4878-8e2c-c8675a71dfb8">

### Explanation:

#### 1. Password List Creation:
- Create a list of sample passwords and save it in `password-list.txt`.

#### 2. Password Hashes Generation:
- Use `password_hashes.py` to generate SHA-256 hashes of the passwords and save them in `hashed-passwords.txt`.

#### 3. Cracking Passwords:
- Use `John the Ripper` to crack the hashed passwords and save them in `cracked-passwords.txt`.
- Alternatively, use `Hashcat` to crack the hashed passwords and save them in `cracked-passwords.txt`.

#### 4. Analysis:
- Use `password_analysis.py` to analyze the cracked passwords and generate a histogram of password lengths.

#### 5. Policy Development:
- Based on the analysis, develop strong password policies and document them in `policy/password_policy.md`.

## Setting Up the Project

### 1. Clone the repository:
```bash
git clone https://github.com/MenakaGodakanda/password-cracking-policies.git
cd password-cracking-policies
```

### 2. Install Tools:

1. **Python**: For scripting and analysis.
```
sudo apt install python3 python3-pip
```

2. **John the Ripper**: An open-source password cracking software tool.
```
sudo apt install john
```

3. **Hashcat**: Another open-source password cracking software tool.
```
sudo apt install hashcat
```

### 3. Password List Creation:
- Created a list of sample passwords and saved it in `password-list.txt`. <br>
![Screenshot 2024-08-01 155158](https://github.com/user-attachments/assets/25aee8ea-4659-4b91-b1fc-66e1371e38f4)

### 4. Password Hashes Generation:
```
python3 password_hashes.py
```
![Screenshot 2024-08-01 040316](https://github.com/user-attachments/assets/ec4ad2b1-518e-4b4e-bdf1-156126e4a286)
- Verify the password hashes are generated.
![Screenshot 2024-08-01 042906](https://github.com/user-attachments/assets/e0edda94-716a-48c6-8d1f-3bae1aa99c92)

### 5. Cracking Passwords:
- Crack Passwords with `John the Ripper`:
```sh
john --format=raw-sha256 --wordlist=password-list.txt hashed-passwords.txt
john --show hashed-passwords.txt
```
![Screenshot 2024-08-01 041445](https://github.com/user-attachments/assets/a9bbe278-b69a-4bac-a29d-1ecbb6ba2fc2)
![Screenshot 2024-08-01 041737](https://github.com/user-attachments/assets/574e8496-b931-4e65-9f53-085aeefc1909)

- Alternatively, crack Passwords with `Hashcat`:
```sh
hashcat -m 1400 -a 0 hashed-passwords.txt password-list.txt -o cracked-passwords.txt
```
![Screenshot 2024-08-01 042150](https://github.com/user-attachments/assets/daa1d91e-895d-4d4c-96d5-96c05fbd26b1)
![Screenshot 2024-08-01 042214](https://github.com/user-attachments/assets/d06a8919-061a-4d11-8e81-d60e7dea8cd6)
- Verify the the passwords has been successfully cracked (`cracked-passwords.txt`).
![Screenshot 2024-08-01 042851](https://github.com/user-attachments/assets/96b3ea5a-9e34-4359-b9e9-1a2ee3882094)

### 6. Analyze Cracked Passwords:
- The `password_analysis.py` script produces a histogram of password lengths. 
- This histogram shows the frequency distribution of password lengths among the cracked passwords.
- Run the script:
```sh
python3 analysis/password_analysis.py
```

### 7. Policy Development:
- Develop strong password policies based on findings and save them in `policy/password_policy.md`.

## Troubleshooting

### Installing John the Ripper from Source
- Some versions of John the Ripper might not support the `--list=formats` option. This could be due to using an outdated version or a different distribution that doesn't include this functionality.
- Install the bleeding-edge version of `John the Ripper` from the GitHub repository to have the latest and most feature-complete version.

#### Step 1 - Install dependencies:
```sh
sudo apt-get update
sudo apt-get install -y git build-essential libssl-dev
```

#### Step 2 - Clone the John the Ripper repository:
```sh
git clone https://github.com/openwall/john.git
cd john/src
```

#### Step 3 - Configure and build John the Ripper:
```sh
./configure
make -s clean && make -sj4
```

#### Step 4 - Verify installation and check formats:
- After the build is complete, you can use the john command from the `run` directory.
```sh
cd ../run
./john --list=formats
```

#### Step 5 - Cracking Passwords:
- Place the `password-list.txt` and  `hashed-passwords.txt` inside the `run` directory.
- Crack Passwords with `John the Ripper`:
```sh
john --format=raw-sha256 --wordlist=password-list.txt hashed-passwords.txt
john --show hashed-passwords.txt
```

## Project Structure
```
password-cracking-policies/
├── password-list.txt
├── cracked-passwords.txt
├── hashed-passwords.txt
├── analysis/
│   ├── analysis.md
│   ├── password_analysis.py
├── policy/
│   ├── password_policy.md
├── password_hashes.py
├── README.md
```

## License
This project is licensed under the MIT License.
