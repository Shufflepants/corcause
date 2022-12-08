from typing import List
from corcause.src.ClassifiedFeature import ClassifiedFeature


class BasicAgent:
    def __init__(self, events: List[ClassifiedFeature]):
        self.events = events
