class Budget:
    # I use this global variable to store the  money spent since the beginning in one category
    Money_spent = 0

    # I use this global variable to calculate and store the amount in of my whole budget
    w_budget = 0

    # I use this global variable to calculate and store the whole budget since the beginning
    w_budget_b = 0

    def __init__(self, budget=0):
        """
        Our constructor class that instantiates the Budget of each category
        """

        # variable that I use to store the money I have spent in one category
        self.spent = 0

        if budget >= 0:
            self.budget = budget

            # variable that I use to store the money I have deposited in one category since the begging
            self.s_beginning = budget
        else:
            self.budget = 0
            self.s_beginning = 0

            print("Please enter a positive number")


    def deposit(self, n=0):
        """
        Deposits an amount of money in my budget
        """
        if n >= 0:
            self.budget += n

            self.s_beginning += n #!!!!

            Budget.w_budget += self.budget

            Budget.w_budget_b += self.budget
        else:
            print("U can't deposit a negative number")

    def withdraw(self, n=0):
        """
        Withdraws an amount of money in my budget
        """
        if n > self.budget:
            print(f"The sum you are trying to withdraw: {n}, is bigger than your budget")

        else:
            self.budget -= n

            self.spent += n

            Budget.Money_spent += n
            Budget.w_budget -= n

    def moneySpent(self):
        """
        Prints the money spent(withdrawn) in a category
        """

        # print(self.spent)

        return self.spent

    def moneyRemaining(self):
        """
        Prints the remaining money in a category
        """

        # print(self.budget)

        return self.budget

    def moneySpentInTotaBudget(self):
        """
        Prints the  money I spent in my total budget
        """

        # print(Budget.Money_spent)
        return Budget.Money_spent

    def moneyRemainingInTotaBudget(self):
        """
        Prints the  whole budget
        """

        # print(Budget.w_budget)
        return Budget.w_budget

    def moneyDepositedSinceBeginningInBudget(self):
        """
        Prints the whole budget since the beginning
        """

        # print(Budget.w_budget_b)
        return Budget.w_budget_b


    def moneyDepositedSinceBeginningInCategory(self):
        """
        Prints the money I have deposited in one category since the begging
        """

        # print(self.s_beginning)
        return self.s_beginning

    def percentile(self):
        """
        Prints the money spent in a category as a % of the whole category budget
        """

        # I'm storing the values of two methods in two variables
        x = Budget.moneySpent(self)
        y = Budget.moneyRemaining(self)
        if x==0 or y==0:
            print("Can't display balance in %")
            return None
        else:
            percentile = (x * 100) / (x + y)
            percentile = round(percentile, 2)

            # print(percentile)
            return percentile



    def balance(self):
        print(f'The money spent in this category: {Budget.moneySpent(self)}')
        print(f'The money remaining in this category: {Budget.moneyRemaining(self)}')
        print(f'The money spent in the total budget: {Budget.moneySpentInTotaBudget(self)}')
        print(f'The whole budget(the remaining money): {Budget.moneyRemainingInTotaBudget(self)}')
        print(f'The money deposited in the whole budget since the beginning: '
              f' {Budget.moneyDepositedSinceBeginningInBudget(self)}')
        print(f'The money deposited in this category since the beginning: '
              f'{Budget.moneyDepositedSinceBeginningInCategory(self)}')
        print(f'The money spent in this category as a % of the whole category budget: {Budget.percentile(self)} %')

        return Budget.moneySpent(self),Budget.moneyRemaining(self),Budget.moneySpentInTotaBudget(self),\
               Budget.moneyRemainingInTotaBudget(self),Budget.moneyDepositedSinceBeginningInBudget(self), \
               Budget.moneyDepositedSinceBeginningInCategory(self),Budget.percentile(self)


class Apartment (Budget):

    pass


class Food (Budget):

    pass


class Utilities (Budget):
    pass


class Automobile (Budget):
    pass


class Entertainment (Budget):
    pass


class Miscellaneous (Budget):
    pass


class Savings (Budget):
    pass


class Investment (Budget):
    pass


class EmergencyFound (Budget):
    pass

















