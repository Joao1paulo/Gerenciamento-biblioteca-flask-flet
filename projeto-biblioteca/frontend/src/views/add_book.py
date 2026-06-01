import flet as ft
from src.api import add_book

def build_add_book_view(page: ft.Page, on_back):
    title_input = ft.TextField(label="Título do Livro", border_radius=8)
    author_input = ft.TextField(label="Autor", border_radius=8)
    year_input = ft.TextField(label="Ano", keyboard_type=ft.KeyboardType.NUMBER, border_radius=8)

    def submit_form(e):
        try:
            year_val = int(year_input.value)
        except ValueError:
            page.show_snack_bar(ft.SnackBar(ft.Text("Ano deve ser numérico!"), bgcolor=ft.colors.ERROR))
            return

        result, error = add_book(title_input.value, author_input.value, year_val)
        
        if error:
            page.show_snack_bar(ft.SnackBar(ft.Text("Erro ao cadastrar. Verifique os dados."), bgcolor=ft.colors.ERROR))
        else:
            page.show_snack_bar(ft.SnackBar(ft.Text("Livro cadastrado com sucesso!"), bgcolor=ft.colors.GREEN))
            on_back()

    return ft.Column([
        ft.Row([
            ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: on_back()),
            ft.Text("Novo Livro", size=24, weight=ft.FontWeight.W_600),
        ], alignment=ft.MainAxisAlignment.START),
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        title_input,
        author_input,
        year_input,
        ft.Container(
            content=ft.ElevatedButton(
                "Salvar Livro",
                on_click=submit_form,
                width=float("inf"),
                bgcolor=ft.colors.PRIMARY,
                color=ft.colors.ON_PRIMARY,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                    padding=15
                )
            ),
            padding=ft.padding.only(top=20)
        )
    ], expand=True)