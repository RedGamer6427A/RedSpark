class AutoSavingDict(dict):
    def __init__(self, initial, on_change, suppress_autosave=False):
        super().__init__()
        self._on_change = on_change
        self._suppress_autosave = suppress_autosave

        for key, value in initial.items():
            # Use direct assignment to avoid __setitem__ triggering save
            super().__setitem__(key, self._wrap(value))
        self._suppress_autosave = False

    def _wrap(self, value):
        if isinstance(value, dict):
            return AutoSavingDict(value, self._on_change)
        return value

    def __setitem__(self, key, value):
        value = self._wrap(value)
        super().__setitem__(key, value)
        if not getattr(self, '_suppress_autosave', False):
            self._on_change()


    def __delitem__(self, key):
        super().__delitem__(key)
        self._on_change()

    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).items():
            self[k] = self._wrap(v)
        self._on_change()

    def clear(self):
        super().clear()
        self._on_change()

    def pop(self, *args, **kwargs):
        result = super().pop(*args, **kwargs)
        self._on_change()
        return result

    def popitem(self):
        result = super().popitem()
        self._on_change()
        return result

    def setdefault(self, key, default=None):
        if key not in self:
            self._on_change()
        return super().setdefault(key, self._wrap(default))
