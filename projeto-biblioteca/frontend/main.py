import flet as ft
from src.views.book_list import build_book_list_view
from src.views.add_book import build_add_book_view

def main(page: ft.Page):
    page.title = "Sistema de Biblioteca"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 420
    page.window.height = 750
    page.padding = 24

    def render(view_content: ft.Control):
        page.controls.clear()
        page.add(view_content)
        page.update()

    def show_list():
        render(build_book_list_view(show_add_form))

    def show_add_form():
        render(build_add_book_view(page, show_list))

    show_list()

ft.app(target=main)