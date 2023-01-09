class Record:

    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        if status > 0:
            self.status = 1
        else:
            self.status = 0
