from bank_account import BankAccount

def test_deposit():
    my_account = BankAccount("John", 200)
    my_account.deposit(50)
    assert my_account.balance == 250

def test_withdraw():
    my_account = BankAccount("Alice", 100)
    my_account.withdraw(20)
    assert my_account.balance == 80

def test_static_function():
    check_good_amount = BankAccount.is_valid_amount(50)
    assert check_good_amount == True
    check_bad_amount = BankAccount.is_valid_amount(-5)
    assert check_bad_amount == False