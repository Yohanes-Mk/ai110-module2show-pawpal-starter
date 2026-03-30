import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pawpal_system import Task, Pet, Owner, Scheduler


def test_adding_task_increases_pet_task_count():
    pet = Pet(name="Mochi", species="dog")
    assert len(pet.tasks) == 0
    pet.tasks.append(Task(description="Morning walk", time="08:00", frequency="daily"))
    assert len(pet.tasks) == 1


def test_sort_by_time_returns_chronological_order():
    pet = Pet(name="Luna", species="cat")
    pet.tasks.append(Task(description="Dinner", time="18:00", frequency="daily"))
    pet.tasks.append(Task(description="Breakfast", time="07:00", frequency="daily"))
    pet.tasks.append(Task(description="Medication", time="12:00", frequency="daily"))

    owner = Owner(name="Alex", pets=[pet])
    scheduler = Scheduler(owner=owner)

    sorted_tasks = scheduler.sort_by_time()
    times = [t.time for t in sorted_tasks]
    assert times == ["07:00", "12:00", "18:00"]
