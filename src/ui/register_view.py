from tkinter import ttk, constants, StringVar
from services.user_service import user_service, UsernameAlreadyExistsError, PasswordsDoNotMatchError, IncorrectInputError


class RegisterView:
    """Uuden käyttäjän luomisesta vastaava näkymä.
    """

    def __init__(self, root, handle_show_login_view, handle_show_main_view):
        """Luokan konstruktori. Luo uuden rekisteröitymisnäkymän.

        Args:
            root: TKinter toiminnallisuus. Näkymä alustetaan tämän sisään.
            handle_show_login_view: Kutsutaan, kun halutaan siirtyä kirjautumisnäkymään.
            handle_show_main_view: kutsutaan, kun halutaan siirtyä sovelluksen etusivulle.
        """
        self._root = root
        self._handle_show_login_view = handle_show_login_view
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._password_confirmation_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """TKinter toiminnallisuus. Näyttää näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """TKinter toiminnallisuus. Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _show_error(self, error_message):
        """Näyttää parametrina annetun virheviestin.

        Args:
            error_message: Näytettävä virheviesti.
        """
        self._error_variable.set(error_message)
        self._error_label.grid()

    def _hide_error(self):
        self.error_label.grid_remove()

    def _handle_register_button_click(self):
        """Rekisteröitymisen tapahtumankäsittelijä. Vaihtaa näkymän sovelluksen etusivuksi sen onnistuessa.
        """
        username = self._username_entry.get()
        password = self._password_entry.get()
        password_confirmation = self._password_confirmation_entry.get()

        try:
            user_service.register(username, password, password_confirmation)
        except (UsernameAlreadyExistsError, PasswordsDoNotMatchError, IncorrectInputError) as error:
            self._show_error(error)

        if user_service.login_status():
            self._handle_show_main_view()

    def _initialize_labels(self):
        """Alustaa tekstikentät.
        """
        header_label = ttk.Label(master=self._frame, text="Create new user")
        new_username_label = ttk.Label(master=self._frame, text="Username")
        password_label = ttk.Label(master=self._frame, text="Password")
        confirm_password_label = ttk.Label(
            master=self._frame, text="Password again")

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        new_username_label.grid(row=1, column=0, padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        confirm_password_label.grid(row=3, column=0, padx=5, pady=5)
        self._error_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def _initialize_entry_fields(self):
        """Alustaa syötekentät.
        """
        self._username_entry = ttk.Entry(master=self._frame)
        self._password_entry = ttk.Entry(master=self._frame)
        self._password_confirmation_entry = ttk.Entry(master=self._frame)

        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._password_confirmation_entry.grid(
            row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize_buttons(self):
        """Alustaa napit
        """
        create_new_user_button = ttk.Button(
            master=self._frame, text="Create user", command=self._handle_register_button_click)
        back_to_login_button = ttk.Button(
            master=self._frame, text="Takaisin", command=self._handle_show_login_view)

        create_new_user_button.grid(columnspan=5, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        back_to_login_button.grid(columnspan=6, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        """Alustaa koko näkymän.
        """
        self._frame = ttk.Frame(master=self._root)
        self._error_variable = StringVar(self._frame)

        self._initialize_labels()
        self._initialize_entry_fields()
        self._initialize_buttons()

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)
