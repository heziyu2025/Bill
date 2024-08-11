
import flet as ft
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from typing import List
from transaction import Transaction
from flet.matplotlib_chart import MatplotlibChart

def chart_view(page: ft.Page,
               transactions: List[Transaction]):
    class State:
        toggle = True

    s = State()

    fig, axs = plt.subplots(2, 1)
    axs[0].set_xlabel("time")
    axs[0].set_ylabel("Income")
    axs[1].set_ylabel("Consumption")
    # 提取收入的 amounts 和 create_time
    income_transactions = [(transaction.amount, transaction.create_time.date())
                           for transaction in transactions if transaction.is_income]

    # 将 income_transactions 转换为 LineChartDataPoint 列表
    data_points = [
        ft.LineChartDataPoint(float(transaction[1].toordinal()), transaction[0])
        for transaction in income_transactions
    ]

    data_1 = [
        ft.LineChartData(
            data_points=data_points,
            stroke_width=5,
            color=ft.colors.CYAN,
            curved=True,
            stroke_cap_round=True,
        )
    ]

    def toggle_data(e):
        chart.data_series = data_1
        chart.interactive = True
        s.toggle = not s.toggle
        chart.update()

    # 例如：
    chart = ft.LineChart(
        lines=data_1,
        min_x=0,
        min_y=0,
    )
    page.add(ft.ElevatedButton("avg", on_click=toggle_data), chart)

    return ft.Text('1月~6月')
