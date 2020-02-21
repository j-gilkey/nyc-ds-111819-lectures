import numpy as np


class Ledger:

    def __init__(self):
        """Class with a list of companies to create bill amounts for (range of 10-1000)."""
        self.counter = 0
        self.rng = np.random
        self.co = ['WotC', 'CoolStuffInc', 'DNDBeyond', 'MiniatureMarket', 'Farm2Bowl']

    def generate(self):
        """Instance method returns a list that should contain the Company name (string) and bill amount (float)."""
        self.counter += 1
        if self.counter % 2 == 0:
            return [str(self.rng.choice(self.co, 1)[0]), str(self.rng.randint(10, 1000, 1)[0])]
        else:
            return [str(self.rng.choice(self.co, 1)[0]), int(self.rng.randint(10, 1000, 1))]


bills = Ledger()


def add_interest(bill, interest=.08):
    """Return a bill amount with added interest rate. Expecting a float or int."""
    return bill*(1+interest)


def get_bill():
    """Generate a bill using the Ledger class object. Returns a list containing the Company (str) and amount (float)."""
    bill = bills.generate()
    print(f'You need to pay {bill[0]} ${bill[1]}.')
    return bill


def get_paid(bill_list, paycheck=3000):
    """Returns nothing. Take a list of bills and subtract from a paycheck amount (default $3000)."""
    print(f'Payday! You\'ve got {paycheck} in the bank.')
    print('Actually . . .')
    for bill in bill_list:
        try:
            paycheck -= bill[1]
            print(f'${paycheck} left after paying off {bill[0]} for ${bill[1]}')
        except:
            print('Something went wrong, I guess. ¯\\_(ツ)_/¯')
    if paycheck>0:
        print(f'Time to spend the remaining ${paycheck}!')
    else:
        print(f'Gotta find ${-1*paycheck} quick . . .')
