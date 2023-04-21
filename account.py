class Account:
    def __init__(self, name: str):
        """Initialize an Account object with the given name and a balance of 0."""
        self.__name = name
        self.__balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Increment the account balance by the specified amount.

        :param amount: The amount to be deposited.
        :return: True if the deposit transaction is successful, False otherwise.
        """
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        """
        Decrement the account balance by the specified amount.

        :param amount: The amount to be withdrawn.
        :return: True if the withdrawal transaction is successful, False otherwise.
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        """Return the account balance."""
        return self.__balance

    def get_name(self) -> str:
        """Return the account name."""
        return self.__name
