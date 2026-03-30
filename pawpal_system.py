from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    description: str
    time: str          # time-of-day in "HH:MM" format
    frequency: str     # e.g. "daily", "weekly"
    is_complete: bool = False


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)


@dataclass
class Scheduler:
    owner: Owner

    def sort_by_time(self) -> List[Task]:
        """Return all tasks across all pets sorted by time-of-day (ascending)."""
        all_tasks = [task for pet in self.owner.pets for task in pet.tasks]
        return sorted(all_tasks, key=lambda t: t.time)

    def filter_by_status(self, is_complete: bool) -> List[Task]:
        """Return all tasks across all pets matching the given completion status."""
        all_tasks = [task for pet in self.owner.pets for task in pet.tasks]
        return [t for t in all_tasks if t.is_complete == is_complete]
