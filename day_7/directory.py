class Directory:
    def __init__(self, name: str, parent_directory: "Directory" = None):
        self.name = name
        self.parent_directory = parent_directory
        self._subdirectories = {}
        self._files = set()
        self.shallow_size = 0

    @property
    def subdirectories(self):
        return self._subdirectories.values()

    @property
    def total_size(self):
        if not hasattr(self, "_total_size"):
            self._total_size = self.shallow_size

            for subdirectory in self._subdirectories.values():
                self._total_size += subdirectory.total_size

        return self._total_size

    def add_subdirectory(self, name):
        try:
            self.find_subdirectory_by_name(name)
        except SubdirectoryNotFoundError:
            self._subdirectories[name] = self.__class__(
                name=name, parent_directory=self
            )

    def find_subdirectory_by_name(self, name):
        try:
            return self._subdirectories[name]
        except KeyError:
            raise SubdirectoryNotFoundError(name)

    def add_file(self, name, size):
        assert isinstance(size, int)
        file = (name, size)
        if file not in self._files:
            self._files.add((name, size))
            self.shallow_size += size


class SubdirectoryNotFoundError(Exception):
    def __init__(self, identifier):
        super(SubdirectoryNotFoundError, self).__init__(
            "Subdirectory not found: {}".format(identifier)
        )
