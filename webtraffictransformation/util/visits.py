class Visit:
    def __init__(self, user_id, path, length):
        self.user_id = user_id
        self.path = path
        self.length = length

    def __eq__(self, other) -> bool:
        return self.user_id == other.user_id and \
               self.path == other.path and \
               self.length == other.length


class CombinedVisits:
    data = {}

    def __init__(self) -> None:
        super().__init__()

    def add(self, visit: Visit):
        if visit.user_id not in self.data:
            self.data[visit.user_id] = {}

        if visit.path not in self.data[visit.user_id]:
            self.data[visit.user_id][visit.path] = visit.length
        else:
            self.data[visit.user_id][visit.path] += visit.length
