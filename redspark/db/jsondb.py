import json

from .autosavingdict import AutoSavingDict


class JSONDB:
    def __init__(self, path='database.json'):
        self.path = path
        self._data = self._load()

    def _load(self):
        with open(self.path, 'r') as f:
            raw = json.load(f)
        return AutoSavingDict(raw, self._save, suppress_autosave=True)

    def _save(self):
        with open(self.path, 'w') as f:
            json.dump(self._data, f, indent=4)


    @property
    def data(self):
        return self._data

