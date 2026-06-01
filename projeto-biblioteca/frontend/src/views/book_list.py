import flet as ft
from src.api import get_books, delete_book

def build_book_list_view(page: ft.Page, on_add_click, on_edit_click, on_refresh):
    books = get_books()
    list_items = ft.Column(spacing=12, scroll=ft.ScrollMode.AUTO, expand=True)

    def show_message(message: str, color: str):
        snack = ft.SnackBar(ft.Text(message, color="#ffffff"), bgcolor=color)
        page.overlay.append(snack)
        snack.open = True
        page.update()

    def handle_delete(book_id):
        success, error = delete_book(book_id)
        if success:
            show_message("Livro apagado com sucesso!", "#cf222e")
            on_refresh()
        else:
            show_message("Erro ao apagar livro.", "#cf222e")

    for book in books:
        list_items.controls.append(
            ft.Container(
                content=ft.ListTile(
                    title=ft.Text(book['title'], color="#0969da", weight=ft.FontWeight.W_600, size=15),
                    subtitle=ft.Text(f"{book['author']} • {book['year']}", color="#656d76", size=13),
                    leading=ft.Icon(ft.Icons.MENU_BOOK, color="#656d76", size=20),
                    trailing=ft.Row([
                        ft.IconButton(ft.Icons.EDIT, icon_color="#656d76", tooltip="Editar", on_click=lambda e, b=book: on_edit_click(b)),
                        ft.IconButton(ft.Icons.DELETE, icon_color="#cf222e", tooltip="Apagar", on_click=lambda e, b_id=book['id']: handle_delete(b_id))
                    ], tight=True)
                ),
                border=ft.Border.all(1, "#d0d7de"),
                border_radius=6,
                bgcolor="#ffffff",
                padding=8
            )
        )

    return ft.Column([
        # CORREÇÃO: Título na esquerda e Botão Verde na direita (Padrão GitHub)
        ft.Row([
            ft.Text("Acervo da Biblioteca", size=20, weight=ft.FontWeight.W_600, color="#1F2328"),
            ft.ElevatedButton(
                "Novo Livro",
                icon=ft.Icons.ADD,
                on_click=lambda _: on_add_click(),
                bgcolor="#1f883d",
                color="#ffffff",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=6),
                    padding=16
                )
            )
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        
        ft.Divider(height=15, color="transparent"),
        list_items
    ], expand=True)