class Snippet:
    """Luokka, kuvaa yksittäistä koodinpätkää.
    """

    def __init__(self, id, user_id, content, created_at):
        """Luokan konstruktori, luo uuden koodinpätkän.

        Args:
            id (int): Koodinpätkän yksilöivä tunniste.
            user_id (int): Koodinpätkän omistavan käyttäjän yksilöivä tunniste.
            content (String): Koodinpätkän sisältö.
            created_at (String): Päivä ja aika, jolloin koodinpätkä luotiin.
        """

        self.id = id
        self.user_id = user_id
        self.content = content
        self.created_at = created_at
