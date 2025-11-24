import flet as ft
from utils.db_utils import create_users_table, add_user, verify_user

def main(page: ft.Page):
    page.title = "Login System"
    page.theme_mode = "dark"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#0d0d0d"

    create_users_table()

    # ---------------- TELA DE LOGIN ----------------
    username = ft.TextField(label="Usuário", width=300)
    password = ft.TextField(label="Senha", password=True, width=300)

    def login(e):
        if verify_user(username.value, password.value):
            open_home()
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("Usuário ou senha incorretos!", color="white"),
                bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()

    def open_register(e=None):
        page.clean()
        page.add(register_view)

    login_btn = ft.ElevatedButton("Entrar", on_click=login, width=300)
    go_register_btn = ft.TextButton("Criar conta", on_click=open_register)

    login_view = ft.Column(
        [
            ft.Text("LOGIN", size=32, weight="bold", color="white"),
            username,
            password,
            ft.Container(height=20),
            login_btn,
            go_register_btn,
        ],
        horizontal_alignment="center",
    )

    # ---------------- TELA DE CADASTRO ----------------
    reg_user = ft.TextField(label="Novo usuário", width=300)
    reg_pass = ft.TextField(label="Nova senha", password=True, width=300)

    def register(e):
        if reg_user.value.strip() == "" or reg_pass.value.strip() == "":
            page.snack_bar = ft.SnackBar(
                ft.Text("Preencha tudo!", color="white"),
                bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()
            return

        if add_user(reg_user.value, reg_pass.value):
            page.snack_bar = ft.SnackBar(
                ft.Text("Conta criada!", color="white"),
                bgcolor="green"
            )
            page.snack_bar.open = True
            open_login()
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("Usuário já existe!", color="white"),
                bgcolor="red"
            )
            page.snack_bar.open = True

        page.update()

    def open_login(e=None):
        page.clean()
        page.add(login_view)

    register_btn = ft.ElevatedButton("Criar conta", on_click=register, width=300)
    back_btn = ft.TextButton("Voltar", on_click=open_login)

    register_view = ft.Column(
        [
            ft.Text("CRIAR CONTA", size=32, weight="bold", color="white"),
            reg_user,
            reg_pass,
            ft.Container(height=20),
            register_btn,
            back_btn,
        ],
        horizontal_alignment="center",
    )

    # ---------------- TELA APÓS LOGIN ----------------
    def open_home():
        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Text("Bem-vindo!", size=40, weight="bold", color="white"),
                    ft.Text("Login realizado com sucesso!", color="white"),
                ],
                horizontal_alignment="center",
            )
        )

    # Carregar login ao iniciar
    page.add(login_view)

# Rodar como site web
ft.app(target=main, view=ft.WEB_BROWSER)
