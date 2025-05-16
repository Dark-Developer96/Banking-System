🏦 Orbit Bank - Simple Banking System in Python
Orbit Bank is a command-line based banking system built using Python. It simulates basic banking operations such as opening an account, checking balance, depositing, withdrawing money, changing PIN, and deleting accounts. All account data is stored securely in a local JSON file.

🚀 Features
• 📁 Persistent account storage using data.json

• 🔐 PIN-protected operations

• 💸 Deposit and withdrawal with minimum transaction limits

• 🔄 Change your PIN securely

• ❌ Account deletion with verification

• ✅ Auto-generated unique 10-digit account numbers

🛠️ Technologies Used
• Python 3

• JSON for data storage

• Standard libraries: os, json, random

⚙️ How It Works
• On first run, a data.json file is created to store account data.

• Users can interact via numbered menu options.

• Each account is protected with a 4-digit numeric PIN.

• Deposits and withdrawals require minimum amounts for security.

• Changes are saved after every successful operation.

📋 Menu Options
• Open an account

• Show balance

• Deposit money

• Withdraw money

• Change PIN

• Delete account

• Exit

🧪 Example Usage
bash
Copy
Edit
$ python orbit_bank.py

Welcome To Orbit Bank
Enter 1 to open an account
Enter 2 to show balance
...
🔐 Account & PIN Rules
• Account numbers are randomly generated (10 digits).

• PIN must be 4 digits only and numeric.

• Minimum deposit and withdrawal: ₹500

📂 Files
• main.py - Main Python script.

•data.json - Stores all user account data in JSON format.

📌 Note
This project is for learning purposes and not suitable for real banking applications.

