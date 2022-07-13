class Category:
  def __init__(self,name) :
    self.name = name
    self.ledger = []

  def __str__(self):
    title = str(self.name.center(30,"*")) + "\n"
    item_list=""
    total_amount = 0
    for i in self.ledger:
      item_list +=f"{i['description'][0:23]:23}"+f"{i['amount']:7.2f}" + "\n"
      total_amount += i["amount"]

    string = title + item_list + "Total: " + str(total_amount)

    return string

  def deposit(self,amount,description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self,amount,description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False


  def transfer(self,amount,transfer_name):
    if self.check_funds(amount) == True:
      self.withdraw(amount,f"Transfer to {transfer_name.name}")
      transfer_name.deposit(amount,f"Transfer from {self.name}")
      return True
    else:
      return False


  def get_balance(self):
    current_balance=0
    for i in self.ledger:
      current_balance += i["amount"]
    return current_balance

  def check_funds(self,amount):
    if amount > self.get_balance():
      return False
    else:
      return True

  
def create_spend_chart(categories):
    category_list = []
    spend_amount = []
    total_amount = 0
    percent_amount = []
    for category in categories:
        category_list.append(category.name)

        amount = 0
        for i in category.ledger:
            if i["amount"] < 0:

                amount += abs(i["amount"])
        spend_amount.append(amount)
        total_amount += amount
    for i in spend_amount:

        percent_amount= list(map(lambda amount: int((((amount / total_amount) * 10) // 1) * 10), spend_amount))
    Line = "Percentage spent by category\n"

    for value in reversed(range(0, 101, 10)):
        if value == 0:
            string = "  " + str(value) + "|"
        elif value < 100:
            string = " " + str(value) + "|"
        else:
            string = str(value) + "|"
        for i in percent_amount:
            if i >= value :
                string += " o "
            else:
                string += "   "

        Line += string + ' \n'

    dashLength = len(spend_amount) * 3 + 1
    Line += "    " + "-" * dashLength + '\n'

    longestStr = max(category_list, key=len)
    longestStrNum = len(longestStr)
    
    for value in range(0, longestStrNum):
        Line += "    "
        number = 1
        for category in category_list:
            
            if len(category) > value:

                Line += (" " + category[value] + " ")
                if number == len(category_list):
                    Line+=" "
                

            else:
                Line += "   "
              
            number+=1
        Line += "\n"
    Line = Line.rstrip()
    Line += "  "

    return Line
