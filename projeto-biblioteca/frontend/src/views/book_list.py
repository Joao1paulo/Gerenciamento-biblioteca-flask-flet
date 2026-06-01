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
                    # Passando a string "menu_book" diretamente:
                    leading=ft.Icon(name="menu_book", color=ft.colors.ON_SURFACE_VARIANT)
                ),
                border=ft.border.all(1, ft.colors.OUTLINE_VARIANT),
                border_radius=8,
                bgcolor=ft.colors.SURFACE,
            )
        )

    return ft.Column([
        ft.Row([
            ft.Text("Acervo da Biblioteca", size=24, weight=ft.FontWeight.W_600),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        list_items,
        ft.Container(
            content=ft.ElevatedButton(
                "Adicionar Novo Livro",
                # Passando a string "add" diretamente:
                icon="add",
                on_click=lambda _: on_add_click(),
                width=float("inf"),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                    padding=15
                )
            ),
            padding=ft.padding.only(top=20)
        )
    ], expand=True)