from tkinter import ttk, constants, StringVar
from services.user_service import user_service
from services.snippet_service import snippet_service, SnippetCopiedToClipboard
import pyperclip

class SnippetListView:
    """Koodinpätkien listasta vastaava näkymä.
    """

    def __init__(self, root, snippets, handle_copy_snippet_to_clipboard, handle_remove_snippet):
        """Luokan konstruktori. Luo uuden näkymän, jossa on koodinpätkien lista.

        Args:
            root: Tkinter-elementti. Näkymä alustetaan tämän sisään.
            snippets: Lista, sisältää käyttäjän koodinpätkät Snippet-olioina.
            handle_copy_snippet_to_clipboard: Kutsutaan, kun halutaan kopioida listassa oleva koodinpätkä leikepöydälle. Saa arqumentiksi koodinpätkän sisällön.
            handle_remove_snippet: Kutsutaan, kun halutaan poistaa listassa oleva koodinpätkä. Saa argumentiksi koodinpätkän id-numeron.
        """        
        self._root = root
        self._snippets = snippets
        self._handle_copy_to_clipboard = handle_copy_snippet_to_clipboard
        self._handle_remove_sippet = handle_remove_snippet
        self._frame = None

        self._initialize()

    def pack(self):
        """Tkinter toiminnallisuus. Näyttää näkymän.
        """        
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tkinter-toiminnallisuus. Tuhoaa näkymän.
        """        
        self._frame.destroy()

    def _initialize_empty_snipped_block(self):
        """Luo tyhjästä koodinpätkien listasta ilmoittavan framen. Lisää sen näkymän "pääframeen".
        """        
        snippet_block_frame = ttk.Frame(master=self._frame)
        content_label = ttk.Label(master=snippet_block_frame, text="Nothing in here, yet!")
        content_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        snippet_block_frame.grid_columnconfigure(0, weight=1)
        snippet_block_frame.pack(fill=constants.X)

    def _initialize_snippet_block(self, snippet):
        """Luo parametrina saatavalle koodinpätkälle oman framen, ja siihen liittyville toiminnoille nappulat. Lisää sen näkymän "pääframeen".

        Args:
            snippet: Tallennettua koodinpätkää kuvaava Snippet-olio.
        """        
        snippet_block_frame = ttk.Frame(master=self._frame)
        content_label = ttk.Label(master=snippet_block_frame, text=snippet.content)
        created_at_label = ttk.Label(master=snippet_block_frame, text=f"Added at: {snippet.created_at}")

        copy_to_clipboard_button = ttk.Button(master=snippet_block_frame, text="Copy", command=lambda: self._handle_copy_to_clipboard(snippet.content))
        remove_snippet_button = ttk.Button(master=snippet_block_frame, text="Delete", command=lambda: self._handle_remove_sippet(snippet.snippet_id))

        content_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        created_at_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        copy_to_clipboard_button.grid(row=0, column=1, padx=5, pady=5)
        remove_snippet_button.grid(row=1, column=1, padx=5, pady=5)

        snippet_block_frame.grid_columnconfigure(0, weight=1)
        snippet_block_frame.pack(fill=constants.X)


    def _initialize(self):
        """Alustaa koko näkymän "pääframeen". Mikäli koodinpätkien lista on tyhjä, luo vain tyhjästä listasta ilmoittavan framen. Muussa tapauksessa luo jokaiselle koodinpätkälle oman framen.
        """
        self._frame = ttk.Frame(master=self._root)
        if not self._snippets:
            self._initialize_empty_snipped_block()
        else:
            for snippet in self._snippets:
                self._initialize_snippet_block(snippet)

class MainView:
    """Sovelluksen etusivu, päänäkymä. Sisältää listan tallennetuista koodinpätkistä, napit sovelluksen keskeisille toiminnoille ja napit sovelluksen muihin osiin siirtymiseen.
    """
    
    def __init__(self, root, handle_show_login_view, handle_show_add_snippet_view, handle_show_settings_view):
        """Luokan konstruktori. Luo päänäkymän.

        Args:
            root: TKinter toiminnalisuus. Näkymä rakennetaan tämän sisään.
            handle_show_login_view: Kutsutaan, kun halutaan siirtyä kirjautumisnäkymään.
            handle_show_add_snippet_view: Kutsutaan, kun halutaan siirtyä koodinpätkän lisäämis näkymään.
            handle_show_settings_view: Kutsutaan, kun halutaan siirtyä asetuksiin.
        """        
        self._root = root
        self._handle_show_login_view = handle_show_login_view
        self._handle_show_add_snippet_view = handle_show_add_snippet_view
        self._handle_show_settings_view = handle_show_settings_view
        self._frame = None
        self._action_feedback_variable = None
        self._action_feedback_frame = None
        self._action_buttons_frame = None
        self._action_feedback_label = None
        self._snippet_list_view = None
        self._snippet_list_frame = None

        self._initialize()

    def pack(self):
        """TKinter toiminnallisuus. Näyttää näkymän.
        """        
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tkinter toiminnallisuus. Tuhoaa näkymän.
        """        
        self._frame.destroy()

    def _show_action_feedback(self, message):
        """Näyttää käyttäjälle palautetta suorittamistaan toiminnoista.

        Args:
            message: Käyttäjälle näytettävä viesti.
        """        
        self._action_feedback_variable.set(message)
        self._action_feedback_label.grid()

    def _hide_action_feedback(self):
        self._action_feedback_label.grid_remove()

    def _handle_logout(self):
        """Uloskirjautumisen tapahtumankäsittelijä. Siirtää kirjautumisnäkymään.
        """        
        user_service.logout()
        self._handle_show_login_view()

    def _handle_copy_snippet_to_clipboard(self, snippet):
        """Koodinpätkän leikepöydälle kopioimisen tapahtumankäsittelijä. Näyttää palautteen tapahtumasta.

        Args:
            snippet: Leikepöydälle kopioitava koodinpätkä.
        """        
        try:
            snippet_service.set_clipboard_contents(snippet)
        except SnippetCopiedToClipboard as message:
            self._show_action_feedback(message)

    def _handle_remove_snippet(self, snippet_id):
        """Koodinpätkän poistamisen tapahtumankäsittelijä. Näyttää palautteen tapahtumasta.

        Args:
            snippet_id: Poistettavan koodinpätkän yksilöivä tunniste.
        """        
        snippet_service.remove(snippet_id)
        self._initialize_snippet_list()
        self._show_action_feedback("Snippet removed")

    def _initialize_snippet_list(self):
        """Alustaa tallennettujen koodinpätkien listan. Tätä kutsutaan, mikäli listan tila muuttuu esim. kirjautumisen tai pätkän poistamisen seurauksena. Tällöin tuhoaa vanhan listan.
        """        
        if self._snippet_list_view:
            self._snippet_list_view.destroy()

        self._snippet_list_view = SnippetListView(self._snippet_list_frame, snippet_service.get_snippets_list(), self._handle_copy_snippet_to_clipboard, self._handle_remove_snippet)
        self._snippet_list_view.pack()

    def _initialize_action_feedback_area(self):
        """Alustaa palautetta antavan alueen omaan frameen.
        """        
        self._action_feedback_variable = StringVar(self._action_feedback_frame)
        self._action_feedback_label = ttk.Label(
            master=self._action_feedback_frame,
            textvariable=self._action_feedback_variable,
            foreground="black"
        )

        self._action_feedback_label.grid(row=0, column=0, columnspan=2, sticky="ewns")

    def _initialize_action_buttons(self):
        """Alustaa näkymän vasemmanpuoleisessa palkissa olevat nappulat omaan frameen.
        """        
        logout_button = ttk.Button(self._action_buttons_frame, text="Logout", command=self._handle_logout)
        add_snippet_button = ttk.Button(self._action_buttons_frame, text="Add snippet", command=self._handle_show_add_snippet_view)
        settings_button = ttk.Button(self._action_buttons_frame, text="Settings", command=self._handle_show_settings_view)

        logout_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        add_snippet_button.grid(row=1, column=0,sticky="ew", padx=5, pady=5)
        settings_button.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

    def _initialize(self):
        """Alustaa ja asettelee koko päänäkymän, sijoittaa eri toiminnallisuutta sisältäväät framet näkymän "pääframeen".
        """        
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

        

        


