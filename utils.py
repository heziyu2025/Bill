from transaction import Transaction
import flet as ft


def add_transaction_to_view(transaction: Transaction, layout: ft.Column, last_date: str | None = None) -> None:
    """Add transaction to a column layout."""
    if last_date is not None:
        if transaction.create_time.strftime('%y%m%d') != last_date:
            layout.controls.insert(0,
                ft.Card(
                    ft.ListView(
                        [transaction.to_list_tile()]
                    )
                )
            )
        else:
            layout.controls[0].content.controls.insert(0, transaction.to_list_tile())
    else:
        layout.controls.insert(0,
            ft.Card(
                ft.ListView(
                    [transaction.to_list_tile()]
                )
            )
        )
