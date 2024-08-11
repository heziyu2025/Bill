from transaction import Transaction
import flet as ft


def add_transaction_to_view(transaction: Transaction, layout: ft.Column, last_date: str | None = None) -> None:
    """Add transaction to a column layout."""
    this_date = transaction.create_time.strftime('%y.%m.%d')
    if last_date is not None:
        if this_date != last_date:
            layout.controls.insert(0,
               ft.Card(
                   ft.Column(
                       [
                           ft.Container(
                               ft.Text(this_date, size=14),
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
                           ft.Text(this_date, size=14),
                           padding=10
                       ),
                       ft.ListView(
                           [transaction.to_list_tile()]
                       )
                   ]
               )
           )
       )
