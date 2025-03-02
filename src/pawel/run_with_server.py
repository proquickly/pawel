# pip install flet
import flet
from flet import IconButton, Page, Row, TextField, Icons, MainAxisAlignment, TextAlign, ElevatedButton
import requests


def main(page: Page):
    page.title = "Flet  example"
    page.vertical_alignment = MainAxisAlignment.CENTER

    txt_number = TextField(value="0", text_align=TextAlign.RIGHT, width=100)
    txt_name = TextField(value="Andy", text_align=TextAlign.LEFT, width=400)
    status_text = TextField(
        value="Ready", text_align=TextAlign.LEFT, width=400, read_only=True)

    def send_to_server():
        try:
            # Send data to the server
            response = requests.post(
                'http://localhost:5000/update',
                json={
                    'name': txt_name.value,
                    'number': txt_number.value
                }
            )

            if response.status_code == 200:
                status_text.value = "Data sent successfully!"
            else:
                status_text.value = f"Error: {response.status_code}"

            page.update()
        except Exception as e:
            status_text.value = f"Error: {str(e)}"
            page.update()

    def submit_click(e):
        status_text.value = "Submitting data..."
        page.update()
        send_to_server()

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

    # Create submit button
    submit_button = ElevatedButton(
        text="Submit",
        icon=Icons.SEND,
        on_click=submit_click
    )

    page.add(
        Row(
            [
                IconButton(Icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(Icons.ADD, on_click=plus_click),
                txt_name,
            ],
            alignment=MainAxisAlignment.CENTER,
        ),
        Row(
            [submit_button],
            alignment=MainAxisAlignment.CENTER,
        ),
        Row(
            [status_text],
            alignment=MainAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    flet.app(target=main)
