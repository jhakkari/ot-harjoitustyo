from tkinter import ttk, constants, StringVar, Text
from services.snippet_service import snippet_service, InvalidInputError
import pyperclip

class AddSnippetView:
    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._snippet_content_textbox = None
        self._action_feedback_variable = None
        self._action_feedback_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_action_feedback(self, message):
        self._action_feedback_variable.set(message)
        self._action_feedback_label.grid()

    def _hide_action_feedback(self):
        self._action_feedback_label.grid_remove()

    def _handle_add_snippet(self):
        content = self._snippet_content_textbox.get("1.0",'end-1c')
        try:
            snippet_service.create_new(content)
        except InvalidInputError as error:
            self._show_action_feedback("Nothing to save!")
            return

        self._handle_show_main_view()

    def _handle_back_to_main(self):
        self._handle_show_main_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.rowconfigure(0, minsize=400, weight=1)
        self._frame.rowconfigure(1, minsize=30, weight=0)
        self._frame.columnconfigure(1, minsize=400, weight=1)

        action_feedback_area = ttk.Frame(master=self._frame)
        self._action_feedback_variable = StringVar(action_feedback_area)
        self._action_feedback_label = ttk.Label(
            master=action_feedback_area,
            textvariable=self._action_feedback_variable,
            foreground="black"
        )

        self._snippet_content_textbox = Text(master=self._frame)
        self._snippet_content_textbox.insert("end-1c", pyperclip.paste())
        self._snippet_content_textbox.grid(row=0, column=1)

        buttons = ttk.Frame(master=self._frame)
        save_snippet_button = ttk.Button(buttons, text="Save", command=self._handle_add_snippet)
        save_snippet_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        back_to_main_button = ttk.Button(buttons, text="Cancel", command=self._handle_show_main_view)
        back_to_main_button.grid(row=1, column=0, sticky="ew", padx=5)

        buttons.grid(row=0, column=0, sticky="ns")
        self._snippet_content_textbox.grid(row=0, column=1, sticky="nsew")

        action_feedback_area.grid(row=1, columnspan=2, padx=5, pady=5)
        self._show_action_feedback("Text copied from your clipboard")


