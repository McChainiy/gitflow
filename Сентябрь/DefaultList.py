class DefaultList(list):
    def __init__(self, default):
        self.default = default

    def __getitem__(self, item):
        try:
            return list(self)[item]
        except Exception:
            return self.default
