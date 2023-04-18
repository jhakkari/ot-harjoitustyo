from tkinter import ttk, constants, StringVar
from services.user_service import user_service

class MainView:
    def __init__(self, root, handle_show_login_view):
        self._root = root
        self._handle_show_login_view = handle_show_login_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_logout(self):
        user_service.logout()
        self._handle_show_login_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(master=self._frame, text="Nothing in here, yet!")
        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        logout_button = ttk.Button(master=self._frame, text="Logout", command=self._handle_logout)
        logout_button.grid(row=1, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)



        


