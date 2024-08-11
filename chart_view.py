
import flet as ft
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from typing import List
from transaction import Transaction
from flet.matplotlib_chart import MatplotlibChart

def chart_view(page: ft.Page,
               transactions: List[Transaction],
               transaction_list_tiles: List[ft.ListTile]):

    fig, axs = plt.subplots(2, 1)
    axs[0].set_xlabel("time")
    axs[0].set_ylabel("Income")
    axs[1].set_ylabel("Consumption")

    # 分别提取收入和支出的 amounts 和 create_time
    income_transactions = [(transaction.amount, transaction.create_time.date())
                           for transaction in transactions if transaction.is_income]
    print(income_transactions)

    expense_transactions = [(transaction.amount, transaction.create_time.date())
                            for transaction in transactions if not transaction.is_income]
    print(expense_transactions)

    fig, axs = plt.subplots(2, 1)
    axs[0].plot(income_transactions)
    axs[0].set_xlabel("time")
    axs[0].set_ylabel("Income")
    axs[0].grid(True)

    axs[1].plot(expense_transactions)
    axs[1].set_xlabel("time")
    axs[1].set_ylabel("Consumption")
    axs[1].grid(True)

    fig.tight_layout()

    page.add(MatplotlibChart(fig, expand=True))

    return ft.Text('1月~6月')
