from pawpal_system import Task, Pet, Owner, Scheduler

mochi = Pet(name="Mochi", species="dog")
mochi.tasks.append(Task(description="Evening walk", time="18:00", frequency="daily"))
mochi.tasks.append(Task(description="Morning feeding", time="07:30", frequency="daily"))

luna = Pet(name="Luna", species="cat")
luna.tasks.append(Task(description="Medication", time="12:00", frequency="daily"))

alex = Owner(name="Alex", pets=[mochi, luna])
scheduler = Scheduler(owner=alex)

print("Today's Schedule for Alex")
print("-" * 35)
for task in scheduler.sort_by_time():
    pet_name = next(p.name for p in alex.pets if task in p.tasks)
    print(f"{task.time}  {pet_name:<8}  {task.description}")
