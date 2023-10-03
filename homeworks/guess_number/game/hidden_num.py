class HiddenNum:
    """
    Скрывает загаданное число.
    """

    def __init__(self, num: int) -> None:
        self.__number = num
        self.count = 0

    def guess(self, num: int) -> int:
        """
        Попытка угадать число.

        Args:
            num (int): число, которое сравнивается со скрытым.

        Returns:
            0: если num совпал со скрытым;

            -1: если num меньше скрытого;

            1: если num больше скрытого.
        """
        self.count += 1
        if self.__number == num:
            return 0

        if self.__number > num:
            return -1

        return 1
