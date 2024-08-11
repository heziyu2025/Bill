from typing import List

import flet as ft

from detail_view import detail_view
from chart_view import chart_view
from transaction import Transaction


def main(page: ft.Page):
    page.title = "Bill"

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.ATTACH_MONEY),
        bgcolor=ft.colors.SURFACE_VARIANT,
        title=ft.Text('Bill'),
    )

    transactions: List[Transaction] = []

    main_views = [detail_view, chart_view]

    def switch(e):
        nonlocal main_row
        main_row.controls[2] = main_views[e.control.selected_index](page, transactions)
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        on_change=switch,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.LIST,
                label='Detail',
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.BAR_CHART,
                label='Chart'
            )
        ]
    )

    main_row = ft.Row(
        controls=[
            rail,
            ft.VerticalDivider(),
            main_views[0](page, transactions)
        ],
        expand=True,
    )

    page.add(main_row)


# 启动 Flet 应用
ft.app(target=main)
