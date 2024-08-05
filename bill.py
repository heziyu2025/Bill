import datetime
from typing import List

import flet as ft


class Bill:
    def __init__(self, is_income: bool, type_: str, amount: float, create_time: datetime):
        self.is_income = is_income
        self.type_ = type_
        self.amount = amount
        self.create_time = create_time

    def to_list_tile(self):
        icon_type = ft.icons.ARROW_UPWARD if self.is_income else ft.icons.ARROW_DOWNWARD
        return ft.ListTile(
            leading=ft.Icon(icon_type),
            title=ft.Text(str(self.amount)),
            subtitle=ft.Text(self.type_),
            trailing=ft.Text(self.create_time.strftime('%Y-%m-%d %H:%M:%S'))
        )


def main(page: ft.Page):
    page.title = "Bill"

    def add_bill(e):
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
            try:
                new_bill = Bill(
                    is_income=is_income,
                    type_=type_dropdown.value,
                    amount=float(amount.value),
                    create_time=datetime.datetime.now()
                )

                bills.append(new_bill)
                bill_rows.append(new_bill.to_list_tile())
                main_list_view.controls.append(new_bill.to_list_tile())

                page.update()

            except:
                page.open(ft.AlertDialog(
                    bgcolor=ft.colors.RED_ACCENT,
                    icon=ft.Icon(ft.icons.ERROR),
                    title=ft.Text('Error'),
                    content=ft.Text('Please enter valid amount.')
                ))

        dialog = ft.AlertDialog(
            title=ft.Text('New Bill'),
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

    bills: List[Bill] = []
    bill_rows: List[ft.ListTile] = []

    main_list_view = ft.ListView()

    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.ADD, on_click=add_bill)
                    ],
                    alignment=ft.MainAxisAlignment.END
                ),
                ft.Card(main_list_view)
            ]
        )
    )


# 启动 Flet 应用
ft.app(target=main)
