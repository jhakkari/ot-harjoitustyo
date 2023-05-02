from tkinter import ttk, constants, StringVar, Text
from services.snippet_service import snippet_service, InvalidInputError
import pyperclip

class AddSnippetView:
    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._snippet_content_textbox = None
        self._action_buttons_frame = None
        self._action_feedback_frame = None
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

    def _initialize_action_feedback_area(self):
        self._action_feedback_frame = ttk.Frame(master=self._frame)
        self._action_feedback_variable = StringVar(self._action_feedback_frame)
        self._action_feedback_label = ttk.Label(
            master=self._action_feedback_frame,
            textvariable=self._action_feedback_variable,
            foreground="black"
        )

    def _initialize_action_buttons(self):
        self._action_buttons_frame = ttk.Frame(master=self._frame)
        save_snippet_button = ttk.Button(self._action_buttons_frame, text="Save", command=self._handle_add_snippet)
        back_to_main_button = ttk.Button(self._action_buttons_frame, text="Cancel", command=self._handle_show_main_view)

        save_snippet_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        back_to_main_button.grid(row=1, column=0, sticky="ew", padx=5)

    def _initialize_snippet_content_textbox(self):
        self._snippet_content_textbox = Text(master=self._frame)
        self._snippet_content_textbox.insert("end-1c", snippet_service.get_clipboard_contents())
        self._show_action_feedback("Text copied from your clipboard")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_action_feedback_area()
        self._initialize_action_buttons()
        self._initialize_snippet_content_textbox()

        self._action_buttons_frame.grid(row=0, column=0, sticky="ns")
        self._snippet_content_textbox.grid(row=0, column=1, sticky="nsew")
        self._action_feedback_frame.grid(row=1, columnspan=2, padx=5, pady=5)

        self._frame.rowconfigure(0, minsize=400, weight=1)
        self._frame.rowconfigure(1, minsize=30, weight=0)
        self._frame.columnconfigure(1, minsize=400, weight=1)


