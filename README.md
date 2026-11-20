# ATM Simulator

A simple command-line ATM simulator written in Python. It lets you log in with a PIN, check your balance, withdraw and deposit money, and view a history of your transactions, all from the terminal.

Built as a beginner Python project to practice functions, loops, input handling and working with dates and JSON.

## Features

- **PIN login** with hidden input (the PIN is not shown while typing)
- **3 attempts** before the account is blocked and the program exits
- **Check balance**, shown with the date and time
- **Withdraw** money, with a check that you have enough balance
- **Deposit** money
- **Transaction history**, printed as formatted JSON
- **Look up a transaction** by type (`bal_check`, `withdraw`, `deposit`)
- Rejects invalid menu choices and negative amounts

## Requirements

- Python 3.6 or newer
- No extra packages: it uses only the Python standard library (`getpass`, `datetime`, `json`, `sys`)

## How to run

```bash
git clone https://github.com/ssn-26/atm_simulator.git
cd atm_simulator
python atm_logic.py
```

**Default PIN:** `1234`
**Starting balance:** ₹5000

> Some IDE consoles (for example IDLE or some PyCharm run windows) don't support hidden input. If the PIN prompt doesn't work there, run the script from a normal terminal.

## Menu

```
__________ ATM MENU __________
1) display balance    2) withdraw
3) deposit            4) history
5) check transaction  6) Change password
7) exit
```

| Option | What it does |
|--------|--------------|
| 1 | Shows your current balance with a timestamp |
| 2 | Withdraws an amount if it is not more than your balance |
| 3 | Deposits an amount into your account |
| 4 | Prints your transaction history |
| 5 | Finds a transaction by type |
| 6 | Change PIN (coming soon) |
| 7 | Exits the ATM |

## Example session

```
Enter the PIN:
PIN verified
__________ ATM MENU __________
1) display balance    2) withdraw
3) deposit            4) history
5) check transaction  6) Change password
7) exit
2
Enter withdraw amt: 1500
Withdrawal successful
Your balance is : ₹ 3500.0
20-11-2026 10:42:07
Would you like to go to the menu again? : y
```

## Roadmap

- [ ] Change PIN (menu option 6)
- [ ] Save balance and history to a file so they persist between runs
- [ ] Keep every transaction in history, not just the latest of each type
- [ ] Unit tests

Suggestions and pull requests are welcome.

## License

This project is licensed under the [MIT License](LICENSE).
