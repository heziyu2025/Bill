import datetime
import pickle
from typing import List
import flet as ft

from transaction import Transaction
from utils import add_transaction_to_view


def detail_view(page: ft.Page,
                transactions: List[Transaction]):
    def add_transaction(e):
        income_types = ['Salary', 'Bonus', 'Interest', 'Stock', 'Rent']
        disburse_types = ['Rent']

        type_dropdown = ft.Dropdown(
            value=income_types[0],
            options=[ft.dropdown.Option(type_i) for type_i in income_types]
        )

        is_income = True

        def switch(e):
            nonlocal type_dropdown
            nonlocal is_income
            is_income = not is_income
            types_list = income_types if e.data == 'income' else disburse_types
            type_dropdown.value = types_list[0]
            type_dropdown.options = [ft.dropdown.Option(type_i) for type_i in types_list]
            page.update()

        def check_number(e):
            allowed_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-']
            nonlocal amount
            amount.value = ''.join([char for char in e.data if char in allowed_chars])
            while True:
                if '.' in amount.value and len(amount.value.split('.')[1]) > 2:
                    amount.value = amount.value[0:-1]
                    continue

                try:
                    float(amount.value)
                except:
                    amount.value = amount.value[0:-1]
                else:
                    break

            page.update()

        amount = ft.TextField(
            label='Amount',
            prefix_text='$',
            keyboard_type=ft.KeyboardType.NUMBER,
            on_change=check_number,
        )

        def cancel(e):
            page.close(dialog)

        def confirm(e):
            page.close(dialog)
            new_transaction = Transaction(
                index=len(transactions),
                is_income=is_income,
                type_=type_dropdown.value,
                amount=float(amount.value),
                create_time=datetime.datetime.now()
            )

            if len(transactions) == 0:
                add_transaction_to_view(new_transaction, main_layout)
            else:
                add_transaction_to_view(new_transaction, main_layout, transactions[-1])
            transactions.append(new_transaction)

            with open('bill.pkl', 'wb') as f:
                pickle.dump(transactions, f)

            page.update()

        dialog = ft.AlertDialog(
            title=ft.Text('New Transaction'),
            content=ft.Column(
                controls=[
                    ft.RadioGroup(
                        value='income',
                        on_change=switch,
                        content=ft.Column(
                            controls=[
                                ft.Radio(value='income', label='Income'),
                                ft.Radio(value='disburse', label='Disburse'),
                            ]
                        )
                    ),
                    type_dropdown,
                    amount,
                    ft.Container(expand=True),
                    ft.Row(
                        controls=[
                            ft.TextButton('Cancel', on_click=cancel),
                            ft.TextButton('Confirm', on_click=confirm),
                        ],
                        alignment=ft.MainAxisAlignment.END
                    )
                ]
            )
        )

        page.open(dialog)
        page.update()

    main_layout = ft.Column()
    last = None
    for transaction in transactions:
        add_transaction_to_view(transaction, main_layout, last)
        last = transaction

    return ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.ADD, on_click=add_transaction)
                ],
                alignment=ft.MainAxisAlignment.END,
            ),
            main_layout,
        ],
        expand=True
    )
