import flet as ft
from src.views.book_list import build_book_list_view
from src.views.add_book import build_add_book_view
from src.views.edit_book import build_edit_book_view

def main(page: ft.Page):
    page.title = "Sistema de Biblioteca"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#f6f8fa" 
    page.window.width = 450
    page.window.height = 750
    page.padding = 24

    def render(view_content: ft.Control):
        page.controls.clear()
        page.add(view_content)
        page.update()

    def show_list():
        # Passamos a página e as funções de callback necessárias
        render(build_book_list_view(page, show_add_form, show_edit_form, show_list))

    def show_add_form():
        render(build_add_book_view(page, show_list))

    def show_edit_form(book):
        render(build_edit_book_view(page, book, show_list))

    show_list()

ft.run(main)