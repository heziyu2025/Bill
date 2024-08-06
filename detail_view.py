import datetime
from typing import List
import flet as ft

from transaction import Transaction


def detail_view(page: ft.Page,
                transactions: List[Transaction],
                transaction_list_tiles: List[ft.ListTile]):
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
            is_income = 1 - is_income
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
                is_income=is_income,
                type_=type_dropdown.value,
                amount=float(amount.value),
                create_time=datetime.datetime.now()
            )

            transactions.append(new_transaction)
            transaction_list_tiles.append(new_transaction.to_list_tile())

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

    main_list_view = ft.ListView(transaction_list_tiles)

    return ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.ADD, on_click=add_transaction)
                ],
                alignment=ft.MainAxisAlignment.END,
            ),
            ft.Card(main_list_view),
        ],
        expand=True
    )
