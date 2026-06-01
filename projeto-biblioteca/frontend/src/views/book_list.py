import flet as ft
from src.api import get_books

def build_book_list_view(on_add_click):
    books = get_books()
    list_items = ft.Column(spacing=15, scroll=ft.ScrollMode.AUTO, expand=True)

    for book in books:
        list_items.controls.append(
            ft.Container(
                content=ft.ListTile(
                    title=ft.Text(book['title'], weight=ft.FontWeight.BOLD),
                    subtitle=ft.Text(f"{book['author']} • {book['year']}"),
                    leading=ft.Icon(ft.Icons.MENU_BOOK, color=ft.Colors.ON_SURFACE_VARIANT)
                ),
                border=ft.Border.all(1, ft.Colors.OUTLINE_VARIANT),
                border_radius=8,
                bgcolor=ft.Colors.SURFACE,
            )
        )

    return ft.Column([
        ft.Row([
            ft.Text("Acervo da Biblioteca", size=24, weight=ft.FontWeight.W_600),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        list_items,
        ft.Container(
            content=ft.ElevatedButton(
                "Adicionar Novo Livro",
                icon=ft.Icons.ADD,
                on_click=lambda _: on_add_click(),
                width=float("inf"),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                    padding=15
                )
            ),
            padding=20
        )
    ], expand=True)