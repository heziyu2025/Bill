import datetime

from transaction import Transaction
import flet as ft


def date_to_text(dt: datetime.datetime) -> str:
    today = datetime.date.today()
    if dt.date() == today:
        return 'Today'
    if dt.date() == today - datetime.timedelta(days=1):
        return 'Yesterday'
    if dt.date().strftime('%U') == today.strftime('%U'):
        return dt.date().strftime('%A')
    if dt.date().strftime('%Y') == today.strftime('%Y'):
        return dt.date().strftime('%B %d')
    return dt.date().strftime('%Y.%m.%d')


def add_transaction_to_view(transaction: Transaction, layout: ft.Column, last: Transaction | None = None) -> None:
    """Add transaction to a column layout."""
    if last is not None:
        if transaction.create_time.date() != last.create_time.date():
            layout.controls.insert(
                0,
                ft.Card(
                    ft.Column(
                        [
                            ft.Container(
                                ft.Text(date_to_text(transaction.create_time), size=14),
                                padding=10
                            ),
                            ft.ListView(
                                [transaction.to_list_tile()]
                            )
                        ]
                    )
                )
            )
        else:
            layout.controls[0].content.controls.insert(1, transaction.to_list_tile())
    else:
        layout.controls.append(
            ft.Card(
                ft.Column(
                    [
                        ft.Container(
                            ft.Text(date_to_text(transaction.create_time), size=14),
                            padding=10
                        ),
                        ft.ListView(
                            [transaction.to_list_tile()]
                        )
                    ]
                )
            )
        )
