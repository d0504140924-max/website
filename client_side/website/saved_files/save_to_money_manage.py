from datetime import datetime
class MoneyManage:


    _current_amount: (int, float)


    def __init__(self, current_amount: (int, float)=0):
        self.current_amount = current_amount
        self.movements = [[],[]]
        self.new_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')


    @property
    def current_amount(self):
        return self._current_amount
    @current_amount.setter
    def current_amount(self, new_amount):
        assert isinstance(new_amount, (int, float))
        self.curren_amount = new_amount


    def add_money(self, amount, _from: str):
        assert isinstance(amount, (float, int))
        if amount <= 0:
            raise ValueError("amount must be positive")
        now_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        self.current_amount += amount
        self.movements[0].append([f' in {now_time} added {amount} from {_from}'])


    def withdraw(self, amount: int, _for: str, to: str=''):
        assert isinstance(amount, (float, int))
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.current_amount:
            raise ValueError("there isn't enough money")
        now_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        self.current_amount -= amount
        self.movements[1].append([f' in {now_time} deducted {amount} for {_for} to {to}'])


    def report(self):
        return self.current_amount


    def movements_record(self, type: str):
        if type == 'income':
            return self.movements[0]
        elif type == 'outcome':
            return self.movements[1]
        elif type == 'all':
            return self.movements
        else:
            raise ValueError("type must be 'income' or 'outcome' or 'all'")


    def month_report(self, month: int):
        month_add = 0
        month_withdrew = 0
        for i in self.movements[0]:
            if i.now_time.month == month:
                month_add += i.amount
        for i in self.movements[1]:
            if i.now_time.month == month:
                month_withdrew += i.amount
        return f'this month added {month_add} and deducted {month_withdrew}'
