from ui.register_view import RegisterView
from ui.login_view import LoginView
from ui.main_view import MainView
from ui.add_snippet_view import AddSnippetView
from ui.settings_view import SettingsView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def _show_register_view(self):
        self._hide_current_view()
        self._current_view = RegisterView(self._root, self._show_login_view, self._show_main_view)
        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(self._root, self._show_register_view, self._show_main_view)
        self._current_view.pack()

    def _show_main_view(self):
        self._hide_current_view()
        self._current_view = MainView(self._root, self._show_login_view, self._show_add_snippet_view, self._show_settings_view)
        self._current_view.pack()

    def _show_add_snippet_view(self):
        self._hide_current_view()
        self._current_view = AddSnippetView(self._root, self._show_main_view)
        self._current_view.pack()

    def _show_settings_view(self):
        self._hide_current_view()
        self._current_view = SettingsView(self._root, self._show_main_view, self._show_login_view)
        self._current_view.pack()