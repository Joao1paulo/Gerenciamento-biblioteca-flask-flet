import flet as ft
from src.views.book_list import build_book_list_view
from src.views.add_book import build_add_book_view
from src.views.edit_book import build_edit_book_view

def main(page: ft.Page):
    page.title = "Sistema de Biblioteca"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#f6f8fa" 
    # CORREÇÃO: Centraliza o conteúdo horizontalmente no navegador
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0

    def render(view_content: ft.Control):
        page.controls.clear()
        # CORREÇÃO: Limita a largura a 750px para não esticar em monitores grandes
        page.add(
            ft.Container(
                content=view_content,
                width=750,
                padding=24,
                expand=True
            )
        )
        page.update()

    def show_list():
        render(build_book_list_view(page, show_add_form, show_edit_form, show_list))

    def show_add_form():
        render(build_add_book_view(page, show_list))

    def show_edit_form(book):
        render(build_edit_book_view(page, book, show_list))

    show_list()

ft.run(main)