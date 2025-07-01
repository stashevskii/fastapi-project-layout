class Service:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self) -> list:
        return self.repository.get_all()
