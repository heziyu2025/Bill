import flet as ft

from main_page import main_page


def main(page: ft.Page):
    page.title = "Bill"
    main_page(page)


# 启动 Flet 应用
ft.app(target=main)
