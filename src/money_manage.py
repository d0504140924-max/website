from src.money_manage_Abc import MoneyManagerAbc


class MoneyManager(MoneyManagerAbc):


    def __init__(self, current_amount=0):

        self.current_amount = current_amount

