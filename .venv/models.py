from datetime import datetime

class Expense():

    def __init__(self, amount, discription, date):

        self.amount = amount
        self.discription = discription
        self.date = date

    def __str__(self):
        return f"Дата: {self.date.strftime('%Y-%m-%d')}, Описание: {self.discription}, Сумма: {self.amount}"

    def get_info(self):
        return f'{self.amount} потрачено на {self.discription} за {self.date}'


class ExpenseTracker():

    def __init__(self):

        self.expenses = []

    def add_expense(self, amount, discription, date):
        ex = Expense(amount, discription, date)
        self.expenses.append(ex)
        return [str(expense) for expense in self.expenses]

    def remove_expense(self, index):
        self.expenses.pop(index)
        return f'Расход был удалне'

e = ExpenseTracker()
print(e.add_expense(1000, 'Покушать', datetime.now()))
print(e.expenses)
print(e.remove_expense(0))
print(e.expenses)

