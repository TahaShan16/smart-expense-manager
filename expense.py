class Expense:
    def __init__ (self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,  
            "date": self.date,
            "description": self.description
        }