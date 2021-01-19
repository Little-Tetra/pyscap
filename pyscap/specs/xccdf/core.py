class Xccdf:
    def __init__(self, file_path=None):
        self.benchmark = None
        if file_path is not None:
            self.load(file_path)

    def load(self, file_path):
        pass

    def dump(self, file_path):
        pass
