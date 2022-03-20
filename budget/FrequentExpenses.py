# from Expense import *
# import collections
# import matplotlib.pyplot as plt
# Expenses = Expense.Expense()
# expenses = Expenses.read_expenses("data/spending_data.csv")
# spending_categories = []
# for expense in expenses.list:
#     spending_categories.append(expense.category)

# #for i in spending_categories:
# spending_counter = collections.Counter(spending_categories) 

# top5 = spending_counter.most_common(5)
# categories, count = zip(*top5)
# fig,ax = plt.subplots()
# ax.bar(categories, count)
# ax.set_title('# of Purchases by Category')
# plt.show()
# print(spending_counter)