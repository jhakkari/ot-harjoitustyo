from tkinter import ttk, constants, StringVar
from services.user_service import user_service
from services.snippet_service import snippet_service
import pyperclip

class SnippetListView:
    def __init__(self, root, snippets, handle_copy_snippet_to_clipboard):
        self._root = root
        self._snippets = snippets
        self._handle_copy_to_clipboard = handle_copy_snippet_to_clipboard
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_empty_snipped_block(self):
        snippet_block_frame = ttk.Frame(master=self._frame)
        content_label = ttk.Label(master=snippet_block_frame, text="Nothing in here, yet!")
        content_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        snippet_block_frame.grid_columnconfigure(0, weight=1)
        snippet_block_frame.pack(fill=constants.X)

    def _initialize_snippet_block(self, snippet):
        snippet_block_frame = ttk.Frame(master=self._frame)
        content_label = ttk.Label(master=snippet_block_frame, text=snippet.content)
        created_at_label = ttk.Label(master=snippet_block_frame, text=f"Added at: {snippet.created_at}")

        copy_to_clipboard_button = ttk.Button(master=snippet_block_frame, text="Copy", command=lambda: self._handle_copy_to_clipboard(snippet.content))

        content_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        created_at_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        copy_to_clipboard_button.grid(row=1, column=2, padx=5, pady=5)

        snippet_block_frame.grid_columnconfigure(0, weight=1)
        snippet_block_frame.pack(fill=constants.X)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        if not self._snippets:
            self._initialize_empty_snipped_block()
        else:
            for snippet in self._snippets:
                self._initialize_snippet_block(snippet)

class MainView:
    def __init__(self, root, handle_show_login_view, handle_show_add_snippet_view):
        self._root = root
        self._handle_show_login_view = handle_show_login_view
        self._handle_show_add_snippet_view = handle_show_add_snippet_view
        self._frame = None
        self._action_feedback_variable = None
        self._action_feedback_frame = None
        self._action_buttons_frame = None
        self._action_feedback_label = None
        self._snippet_list_view = None
        self._snippet_list_frame = None

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

    def _handle_logout(self):
        user_service.logout()
        self._handle_show_login_view()

    def _handle_copy_snippet_to_clipboard(self, snippet):
        pyperclip.copy(snippet)
        self._show_action_feedback("Copied to clipboard!")

    def _initialize_snippet_list(self):
        if self._snippet_list_view:
            self._snippet_list_view.destroy()

        self._snippet_list_view = SnippetListView(self._snippet_list_frame, snippet_service.get_snippets_list(), self._handle_copy_snippet_to_clipboard)
        self._snippet_list_view.pack()

    def _initialize_action_feedback_area(self):
        self._action_feedback_variable = StringVar(self._action_feedback_frame)
        self._action_feedback_label = ttk.Label(
            master=self._action_feedback_frame,
            textvariable=self._action_feedback_variable,
            foreground="black"
        )

        self._action_feedback_label.grid(row=0, column=0, columnspan=2, sticky="ewns")

    def _initialize_action_buttons(self):
        logout_button = ttk.Button(self._action_buttons_frame, text="Logout", command=self._handle_logout)
        add_snippet_button = ttk.Button(self._action_buttons_frame, text="Add snippet", command=self._handle_show_add_snippet_view)

        logout_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        add_snippet_button.grid(row=1, column=0,sticky="ew", padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._snippet_list_frame = ttk.Frame(master=self._frame)
        self._action_feedback_frame = ttk.Frame(master=self._frame)
        self._action_buttons_frame = ttk.Frame(master=self._frame)

        self._initialize_action_feedback_area()
        self._initialize_snippet_list()
        self._initialize_action_buttons()

        self._action_buttons_frame.grid(row=0, column=0, sticky="ns")
        self._snippet_list_frame.grid(row=0, column=1, sticky="news")
        self._action_feedback_frame.grid(row=1,column=0, columnspan=2, padx=5, pady=5, sticky="s")

        self._frame.rowconfigure(0, minsize=200, weight=1)
        self._frame.rowconfigure(1, minsize=30, weight=0)
        self._frame.columnconfigure(1, minsize=400, weight=1)

        

        


