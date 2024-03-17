from modules.note import Note

class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, title: str, text: str):
        self.notes.append(Note(title, text))

    def edit_note(self, title: str, new_text: str):
        for i in self.notes:
            if i.title == title:
                i.text = new_text

    def remove_note(self, title: str):
        for i in self.notes:
            if i.title == title:
                self.notes.remove(i)

    def find_by_title(self, title: str) -> Note:
        """Find and return a note by its title."""
        for note in self.notes:
            if title in note.title:
                return note
            
    def to_json(self) -> dict:
        """ A function that converts the object to a JSON dictionary. """
        res = {}
        for item in self.notes:
            res.update({item.title: item.text})
        return res
