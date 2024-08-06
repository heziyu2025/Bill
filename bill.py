import flet as ft

from detail_page import detail_page
from chart_page import chart_page


def main(page: ft.Page):
    page.title = "Bill"

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.ATTACH_MONEY),
        bgcolor=ft.colors.SURFACE_VARIANT,
        title=ft.Text('Bill'),
    )

    right_pages = [detail_page, chart_page]

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
            right_pages[0](page)
        ],
        expand=True,
    )

    page.add(main_row)


# 启动 Flet 应用
ft.app(target=main)
