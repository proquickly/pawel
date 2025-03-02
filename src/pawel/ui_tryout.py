# pip install flet
import flet
from flet import IconButton, Page, Row, TextField, Icons, MainAxisAlignment, TextAlign


def main(page: Page):
    page.title = "Flet counter example"
    page.vertical_alignment = MainAxisAlignment.CENTER

    txt_number = TextField(value="0", text_align=TextAlign.RIGHT, width=100)
    txt_name = TextField(value="Andy", text_align=TextAlign.LEFT, width=400)

    def minus_click(e):
        try:
            current_value = int(
                txt_number.value if txt_number.value is not None else "0")
            txt_number.value = str(current_value - 1)
            page.update()
        except ValueError:
            txt_number.value = "0"
            page.update()

    def plus_click(e):
        try:
            current_value = int(
                txt_number.value if txt_number.value is not None else "0")
            txt_number.value = str(current_value + 1)
            page.update()
        except ValueError:
            txt_number.value = "0"
            page.update()
        page.update()

    page.add(
        Row(
            [
                IconButton(Icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(Icons.ADD, on_click=plus_click),
                txt_name,
            ],
            alignment=MainAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    flet.app(target=main)
