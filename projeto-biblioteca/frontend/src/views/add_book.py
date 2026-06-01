import flet as ft
from src.api import add_book

def build_add_book_view(page: ft.Page, on_back):
    title_input = ft.TextField(label="Título do Livro", border_radius=8)
    author_input = ft.TextField(label="Autor", border_radius=8)
    year_input = ft.TextField(label="Ano", keyboard_type=ft.KeyboardType.NUMBER, border_radius=8)

    # Função auxiliar criada para garantir que o SnackBar funcione em qualquer versão
    def show_message(message: str, color: str):
        snack = ft.SnackBar(ft.Text(message), bgcolor=color)
        page.overlay.append(snack)
        snack.open = True
        page.update()

    def submit_form(e):
        try:
            year_val = int(year_input.value)
        except ValueError:
            show_message("Ano deve ser numérico!", ft.Colors.ERROR)
            return

        result, error = add_book(title_input.value, author_input.value, year_val)
        
        if error:
            show_message("Erro ao cadastrar. Verifique os dados.", ft.Colors.ERROR)
        else:
            show_message("Livro cadastrado com sucesso!", ft.Colors.GREEN)
            on_back()

    return ft.Column([
        ft.Row([
            ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: on_back()),
            ft.Text("Novo Livro", size=24, weight=ft.FontWeight.W_600),
        ], alignment=ft.MainAxisAlignment.START),
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        title_input,
        author_input,
        year_input,
        ft.Container(
            content=ft.ElevatedButton(
                "Salvar Livro",
                on_click=submit_form,
                width=float("inf"),
                bgcolor=ft.Colors.PRIMARY,
                color=ft.Colors.ON_PRIMARY,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                    padding=15
                )
            ),
            padding=20
        )
    ], expand=True)