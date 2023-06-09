class Account:
    def __init__(self, name: str):
        self.__name = name
        self.__balance = 0

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        return self.__balance

    def get_name(self) -> str:
        return self.__name
    