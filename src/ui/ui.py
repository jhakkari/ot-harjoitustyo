from ui.register_view import RegisterView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_register_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def _show_register_view(self):
        self._hide_current_view()
        self._current_view = RegisterView(self._root)
        self._current_view.pack()
