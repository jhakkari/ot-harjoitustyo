from tkinter import ttk, constants, StringVar
from services.user_service import user_service, IncorrectInputError, InvalidUserError, IncorrectCredentialsError


class LoginView:
    """Käyttäjän sisäänkirjautumisesta vastaava näkymä.
    """

    def __init__(self, root, handle_show_register_view, handle_show_main_view):
        """Luokan konstruktori. Luo sisäänkirjautumisnäkymän.

        Args:
            root: TKinter-elementti. Näkymä alustetaan tämän sisään.
            handle_show_register_view: Kutsutaan, kun halutaan siirtyä rekisteröitymisnäkymään.
            handle_show_main_view: Kutsutaan, kun halutaan siirtuä sovelluksen etusivulle.
        """

        self._root = root
        self._handle_show_register_view = handle_show_register_view
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Tkinter toiminnallisuus. näyttää näkymän.
        """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """TKinter-toiminnallisuus. Tuhoaa näkymän.
        """

        self._frame.destroy()

    def _show_error(self, error_message):
        """Näyttää parametrina annettavan vieheilmoituksen.

        Args:
            error_message: Näytettävä virheilmoitus.
        """
        self._error_variable.set(error_message)
        self._error_label.grid()

    def _hide_error(self):
        self.error_label.grid_remove()

    def _handle_login(self):
        """Kirjatumisen tapahtumankäsittelijä. Onnistuessa siitää sovelluksen etusivulle.
        """

        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            user_service.login(username, password)
        except (IncorrectInputError, IncorrectCredentialsError, InvalidUserError) as error:
            self._show_error(error)

        if user_service.login_status():
            self._handle_show_main_view()

    def _initialize_labels(self):
        """Alustaa näkymän tekstikentät.
        """

        header_label = ttk.Label(master=self._frame, text="Login")
        username_label = ttk.Label(master=self._frame, text="Username")
        password_label = ttk.Label(master=self._frame, text="Password")
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._error_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def _initialize_entry_fields(self):
        """Alustaa näkymän syötekentät,
        """

        self._username_entry = ttk.Entry(master=self._frame)
        self._password_entry = ttk.Entry(master=self._frame)

        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _initialize_buttons(self):
        """Alustaa näkymän painikkeet.
        """

        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._handle_login)
        register_button = ttk.Button(
            master=self._frame, text="Create new user", command=self._handle_show_register_view)

        login_button.grid(columnspan=4, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        register_button.grid(columnspan=5, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        """Alustaa näkymän kaikki elementit.
        """

        self._frame = ttk.Frame(master=self._root)
        self._error_variable = StringVar(self._frame)

        self._initialize_labels()
        self._initialize_entry_fields()
        self._initialize_buttons()

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)
