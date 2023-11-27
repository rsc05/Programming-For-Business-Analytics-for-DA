
def transfer_funds(sender_account, receiver_account, amount):
    if sender_account.balance >= amount:
        sender_account.withdraw(amount)
        receiver_account.deposit(amount)
        print(f"Funds transferred successfully: {amount} from {sender_account.owner} to {receiver_account.owner}")
    else:
        print(f"Transfer failed: Insufficient funds in {sender_account.owner}'s account.")


def total_balance(accounts):
    total = sum(account.balance for account in accounts)
    return total

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.partner_accounts = []  # A list to hold partner accounts


    def add_partner_account(self, partner_account):
        self.partner_accounts.append(partner_account)
        partner_account.partner_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def account_info(self):
        print(f"Account owner: {self.owner} | Current balance: {self.balance}")

    def partner_deposit(self, partner_owner, amount):
            for partner in self.partner_accounts:
                if partner.owner == partner_owner and partner.balance >= amount:
                    self.balance += amount
                    partner.balance -= amount
                    print(f"{partner_owner} deposited {amount}. New balance of {self.owner} is: {self.balance}")
                    print(f"{partner_owner}'s new balance: {partner.balance}")
                    return
            print("Either no matching partner found or insufficient funds in partner account.")
