import webbrowser
import urllib.parse

PATH = "literature/piece de stockage"

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
        path = PATH.replace("/", "%2F").replace(" ", "%20")
        text = f"- {query}"
        encoded_text = text.replace(" ", "%20")

        url = f"advanced-uri?vault=vault&filepath={path}.md&data={encoded_text}&mode=append"
        self.logger.info(url)
        webbrowser.open(f"obsidian://{url}")
        

if __name__ == "__main__":
    Obsidian()
