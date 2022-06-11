# this is a comment PATH = "literature/piece de stockage.md"

from flox import Flox

class Obsidian(Flox):

    def query(self, query):
        self.add_item(
            title=query,
            subtitle=f"ajouter",
            method="add_to_obsidian",
            parameters=[query]
        )

    def context_menu(self, data):
        pass 

    def add_to_obsidian(self, query):
        with open('C:/Users/Lenovo/Documents/obsidian_vault/vault/literature/piece de stockage.md', 'a+', encoding='utf-8') as f:
            f.write('\n- ')
            f.write(query)
            f.close()


