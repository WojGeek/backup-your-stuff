"""Exclude"""

import json


class Exclude:
    """Exclude Class | Clase Exclude :

    Parameter:
      argument (string):  File path

    """

    def __init__(self, file_path):
        self._file_path = file_path
        self._excluded_items = set()
        self.load_items()

    @property
    def file_path(self):
        """Excludes files path"""
        return self._file_path

    @file_path.setter
    def file_path(self, new_path):
        self._file_path = new_path
        self.load_items()

    def load_items(self):
        """Load excludes"""

        try:
            with open(self._file_path, "r", encoding="utf-8") as file:
                self._excluded_items = set(json.load(file))
                # self._excluded_items = set(file.read())

        except FileNotFoundError:
            print(f"El archivo {self._file_path} no existe. Se creará uno nuevo..!")

    def save_items(self):
        """Save excludes"""

        with open(self._file_path, "w", encoding="utf-8") as file:
            json.dump(list(self._excluded_items), file)
            # file.write("\n".join(self._excluded_items))

    def exclude(self, item):
        """Add exclude pattern"""
        if item in self._excluded_items:
            print(f"Exclude ya existe: {item}")
        else:
            self._excluded_items.add(item)
            print(f"Agregado a la lista de exclusión: {item}")
            self.save_items()

    def remove(self, item):
        """Remove exclude"""
        if item in self._excluded_items:
            self._excluded_items.remove(item)
            self.save_items()
            print(f"Exclude eliminado: {item} ")
        else:
            print(f"No se encontró en la lista de exclusión: {item}")

    def listing(self):
        """
        List of exclusions (sorted)
        """

        # print(type(self._excluded_items))
        print("-" * 3 + " Listado de exclusiones " + "-" * 3)
        for item in sorted(self._excluded_items):
            print(item)
