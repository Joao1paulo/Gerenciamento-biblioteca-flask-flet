import flet as ft
from src.api import update_book

def build_edit_book_view(page: ft.Page, book: dict, on_back):
    input_style = {
        "border_color": "#d0d7de",
        "focused_border_color": "#0969da",
        "border_radius": 6,
        "text_size": 14,
        "cursor_color": "#0969da",
        "bgcolor": "#ffffff",
        "color": "#1F2328",
        "label_style": ft.TextStyle(color="#656d76")
    }

    title_input = ft.TextField(label="Título do Livro", value=book['title'], **input_style)
    author_input = ft.TextField(label="Autor", value=book['author'], **input_style)
    year_input = ft.TextField(label="Ano", value=str(book['year']), keyboard_type=ft.KeyboardType.NUMBER, **input_style)

    def show_message(message: str, color: str):
        snack = ft.SnackBar(ft.Text(message, color="#ffffff"), bgcolor=color)
        page.overlay.append(snack)
        snack.open = True
        page.update()

    def submit_edit(e):
        try:
            year_val = int(year_input.value)
        except ValueError:
            show_message("Ano deve ser numérico!", "#cf222e")
            return

        result, error = update_book(book['id'], title_input.value, author_input.value, year_val)
        
        if error:
            show_message("Erro ao atualizar. Verifique os dados.", "#cf222e")
        else:
            show_message("Livro atualizado com sucesso!", "#1f883d")
            on_back()

    return ft.Column([
        ft.Row([
            ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#656d76", on_click=lambda _: on_back()),
            ft.Text("Editar Livro", size=20, weight=ft.FontWeight.W_600, color="#1F2328"),
        ], alignment=ft.MainAxisAlignment.START),
        ft.Divider(height=15, color="#d0d7de"),
        ft.Container(
            content=ft.Column([
                title_input,
                author_input,
                year_input,
            ], spacing=16),
            # CORREÇÃO: Usando um número inteiro direto
            padding=15
        ),
        ft.Container(
            content=ft.ElevatedButton(
                "Atualizar Livro",
                on_click=submit_edit,
                width=float("inf"),
                bgcolor="#0969da",
                color="#ffffff",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=6),
                    padding=16
                )
            )
        )
    ], expand=True)