from datetime import datetime

date = datetime.now()

class Expense():

    def __init__(self, amount, discription, date):

        self.amount = amount
        self.discription = discription
        self.date = date

    def __str__(self):
        return f"Дата: {self.date.strftime('%Y-%m-%d')}, Описание: {self.discription}, Сумма: {self.amount}"

    def _get_info(self):
        return f'{self.amount} потрачено на {self.discription} за {self.date}'


class ExpenseTracker():

    def __init__(self):

        self.expenses = []

    def add_expense(self, amount, discription, date):

        ex = Expense(amount, discription, date)
        self.expenses.append(ex)
        return 'расход был добавлен'

    def _remove_expense(self, index):

        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
        else:
            return 'Ошибка: индекс вне деапозона!'
        return 'Расход был удален!'

    def _total_expenses(self):

        total = sum(expense.amount for expense in self.expenses)
        return f'Общая сумма расходов: {total}'

    def _get_expenses(self):

        return [str(expense) for expense in self.expenses]



# e = ExpenseTracker()
# print(e.add_expense(1000, 'Покушать', datetime.now()))
# print(e.get_expenses())
# print(e.add_expense(5000, 'Путешествия', date))
# print(e.add_expense(5034, 'Дом', date))
# print(e.remove_expense(0))
# print(e.get_expenses())
# print(e.total_expenses())


