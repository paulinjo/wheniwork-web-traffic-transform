class PathVisit:
    def __init__(self, user_id, path, length):
        self.user_id = user_id
        self.path = path
        self.length = length

    def __eq__(self, other) -> bool:
        return self.user_id == other.user_id and \
               self.path == other.path and \
               self.length == other.length


CombinedVisit = dict[str, dict[str, int]]


def add_visit(visits: CombinedVisit, path_visit: PathVisit):
    """

    Add an additional visit to the dictionary of already processed visits. Mutates the `visits` dictionary.

    :param visits: Dictionary that maps a user_id to a set of paths => lengths
    :param path_visit:
    """
    if path_visit.user_id not in visits:
        visits[path_visit.user_id] = {}

    if path_visit.path not in visits[path_visit.user_id]:
        visits[path_visit.user_id][path_visit.path] = path_visit.length
    else:
        visits[path_visit.user_id][path_visit.path] += path_visit.length
