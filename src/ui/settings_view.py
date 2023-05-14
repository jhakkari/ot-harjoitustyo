from tkinter import ttk, constants
from services.user_service import user_service
from services.snippet_service import snippet_service


class SettingsView:
    """Asetuksista vastaava näkymä.
    """

    def __init__(self, root, handle_show_main_view, handle_show_login_view):
        """Luokan konstruktori. Luo uuden asetukset näkymän.

        Args:
            root: TKinter toiminnallisuus. Näkymä alustetaan tämän sisään.
            handle_show_main_view: Kutsutaan, ku halutaan siirtyä sovelluksen etusivulla.
            handle_show_login_view: Kutsutaan, kun käyttäjän tiedot on poistettu ja siirrytään ulos sovelluksesta.
        """
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._handle_show_login_view = handle_show_login_view
        self._action_buttons_frame = None
        self._settings_frame = None
        self._frame = None

        self._initialize()

    def pack(self):
        """TKinter toiminnallisuus. Näyttää näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tkinter toiminnallisuus. Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _handle_back_to_main(self):
        self._handle_show_main_view()

    def _handle_delete_user_and_data(self):
        """Käyttäjän ja kaiken datan poistamisen tapahtumankäsittelijä. Siirtää lopuksi ohjelman kirjautumisnäkymään.
        """
        snippet_service.remove_all_user_snippets()
        user_service.delete_user_account()
        self._handle_show_login_view()

    def _initialize_action_buttons(self):
        """Alustaa näkymän vasemmassa reunassa olevan napin.
        """
        self._action_buttons_frame = ttk.Frame(master=self._frame)
        back_to_main_button = ttk.Button(
            self._action_buttons_frame, text="Cancel", command=self._handle_show_main_view)

        back_to_main_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

    def _initialize_settings_area(self):
        """Alustaa asetuksista vastaavan framen nappeineen ja tekstikenttineen.
        """
        self._settings_frame = ttk.Frame(master=self._frame)

        header_label = ttk.Label(
            master=self._settings_frame, text="Delete account and data")
        delete_info_label = ttk.Label(
            master=self._settings_frame, text="This action will:\nDelete all your saved snippets\nDelete your account\nLogout of this application.")
        delete_all_button = ttk.Button(
            master=self._settings_frame, text="Delete account", command=self._handle_delete_user_and_data)

        header_label.grid(row=0, column=0, sticky="ns", padx=5, pady=5)
        delete_all_button.grid(row=2, column=0, sticky="ns", padx=5, pady=5)
        delete_info_label.grid(row=4, column=0, sticky="ns", padx=5, pady=5)

    def _initialize(self):
        """Alustaa ja asettelee koko näkymän.
        """
        self._frame = ttk.Frame(master=self._root)

        self._initialize_action_buttons()
        self._initialize_settings_area()

        self._action_buttons_frame.grid(row=0, column=0, sticky="ns")
        self._settings_frame.grid(row=0, column=1, padx=5, pady=5)

        self._frame.rowconfigure(0, minsize=200, weight=1)
        self._frame.columnconfigure(1, minsize=400, weight=1)
