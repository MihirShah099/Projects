from enum import Enum

class SortByValues(str, Enum):
    id = "id"
    reads = "reads"
    likes = "likes"
    popularity = "popularity"