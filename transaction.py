import datetime
import flet as ft


class Transaction:
    def __init__(self, index: int, is_income: bool, type_: str, amount: float, create_time: datetime):
        self.index = index
        self.is_income = is_income
        self.type_ = type_
        self.amount = amount
        self.create_time = create_time

    def to_list_tile(self):
        icon_type = ft.icons.ARROW_UPWARD if self.is_income else ft.icons.ARROW_DOWNWARD
        return ft.ListTile(
            leading=ft.Icon(icon_type),
            title=ft.Text(
                str(self.amount),
                no_wrap=True,
                width=200
            ),
            subtitle=ft.Text(
                self.type_,
                width=200
            ),
            trailing=ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem('Delete', icon=ft.icons.DELETE)
                ]
            )
        )
