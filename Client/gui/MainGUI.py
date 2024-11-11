import flet as ft
import os

def gui(page: ft.Page):
    page.title = f"CoraChat Client"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    ## Chat ##
    chat = ft.Column()
    new_message = ft.TextField()

    ## Funcs ##
    def send_click(e):
        chat.controls.append(ft.Text(new_message.value))
        new_message.value = ""
        page.update()

    page.add(
        chat,
        ft.Row(
            [
                new_message,
                ft.ElevatedButton("Send", on_click=send_click)
            ]
        )
    )

def initGui():  
    ft.app(gui)