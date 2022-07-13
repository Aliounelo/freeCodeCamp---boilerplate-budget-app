# freeCodeCamp-boilerplate-budget-app

Complete the <b>Category</b> class in <b>budget.py</b>. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called <b>ledger</b> that is a list. The class should also contain the following methods:

<p>
<ul>
    <li>A <b>deposit</b> method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of <b>{"amount": amount, "description": description}</b>.
    <li>A <b>withdraw</b> method that is similar to the <b>deposit</b> method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return <b>True</b> if the withdrawal took place, and <b>False</b> otherwise.
    <li>A <b>get_balance</b> method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    <li>A <b>transfer</b> method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return <b>True</b> if the transfer took place, and <b>False</b> otherwise.
    <li>A <b>check_funds</b> method that accepts an amount as an argument. It returns <b>False</b> if the amount is greater than the balance of the budget category and returns <b>True</b> otherwise. This method should be used by both the <b>withdraw</b> method and <b>transfer</b> method.
</ul>

When the budget object is printed it should display: 

<ul>
    <li>A title line of 30 characters where the name of the category is centered in a line of <b>*</b> characters.
    <li>A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    <li>A line displaying the category total.
</ul>

Here is an example of the output:
</p>

![image](https://user-images.githubusercontent.com/53930501/178739351-665f112e-5204-420c-8c13-8dad3c9fcf44.png)

<p>
Besides the <b>Category</b> class, create a function (outside of the class) called <b>create_spend_chart</b> that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.
</p>

![image](https://user-images.githubusercontent.com/53930501/178739734-3e76d031-3cd3-4e14-9a33-a09a59a32c96.png)


The unit tests for this project are in <b>test_module.py</b>.

# Development

Write your code in <b>budget.py</b>. For development, you can use <b>main.py</b> to test your <b>Category</b> class. Click the "run" button and <b>main.py</b> will run.

# Testing

We imported the tests from <b>test_module.py</b> to <b>main.py</b> for your convenience. The tests will run automatically whenever you hit the "run" button.


