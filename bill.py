import flet as ft

from bill_page import bill_page
from chart_page import chart_page


def main(page: ft.Page):
    page.title = "Bill"

    right_pages = [bill_page, chart_page]

    def switch(e):
        nonlocal main_row
        main_row.controls[2] = right_pages[e.control.selected_index](page)
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        on_change=switch,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.LIST,
                label='Bill',
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
            right_pages[0](page)
        ],
        expand=True,
    )

    page.add(main_row)


# 启动 Flet 应用
ft.app(target=main)
