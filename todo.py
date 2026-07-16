import os

FILENAME = "tasks.txt"
CATEGORIES = [
    "Morning Schedules",
    "Afternoon Routines",
    "Meetings",
    "Breaks",
    "Evening Review",
    "Rest"
]

def load_tasks():
    """Loads tasks and organizes them into category arrays."""
    # Initialize empty lists for every category
    todo_data = {cat: [] for cat in CATEGORIES}
    
    if not os.path.exists(FILENAME):
        return todo_data
        
    current_category = None
    with open(FILENAME, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            # Identify category headers
            if line.startswith("[") and line.endswith("]"):
                cat_name = line[1:-1]
                if cat_name in todo_data:
                    current_category = cat_name
            elif current_category:
                todo_data[current_category].append(line)
                
    return todo_data

def save_tasks(todo_data):
    """Saves organized tasks back into the local flat text file."""
    with open(FILENAME, "w") as file:
        for cat in CATEGORIES:
            file.write(f"[{cat}]\n")
            for task in todo_data[cat]:
                file.write(f"{task}\n")
            file.write("\n") # Add spacing between blocks

def show_tasks(todo_data):
    """Prints a structured dashboard grouped by operational time blocks."""
    print("\n================== DAILY ROUTINE SYSTEM ==================")
    has_tasks = False
    
    for cat in CATEGORIES:
        tasks = todo_data[cat]
        if tasks:
            has_tasks = True
            print(f"\n📌 {cat.upper()}")
            for idx, task in enumerate(tasks, start=1):
                print(f"  {idx}. {task}")
                
    if not has_tasks:
        print("\nYour routine dashboard is entirely clear! 🚀")
    print("\n==========================================================")

def choose_category():
    """Helper menu to select a category profile safely."""
    while True:
        print("\n--- SELECT CATEGORY ---")
        for i, cat in enumerate(CATEGORIES, start=1):
            print(f"{i}. {cat}")
        try:
            choice = int(input(f"Choose category (1-{len(CATEGORIES)}): "))
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
            print("Out of range. Try again.")
        except ValueError:
            print("Please enter a valid menu number.")

def add_task(todo_data):
    """Appends task to a chosen functional time block."""
    category = choose_category()
    task_desc = input(f"\nEnter task for {category}: ").strip()
    if task_desc:
        todo_data[category].append(task_desc)
        save_tasks(todo_data)
        print(f"✓ Successfully logged into {category}!")
    else:
        print("Task details cannot be blank.")

def delete_task(todo_data):
    """Selects and removes a task safely from a category layout."""
    category = choose_category()
    tasks = todo_data[category]
    
    if not tasks:
        print(f"\nNo tasks found inside {category} to clear.")
        return
        
    print(f"\n--- {category.upper()} TASKS ---")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")
        
    try:
        num = int(input("\nEnter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(todo_data)
            print(f"✗ Dropped: '{removed}'")
        else:
            print("Invalid entry index.")
    except ValueError:
        print("Please enter a valid numeric assignment.")

def main():
    todo_data = load_tasks()
    
    while True:
        print("\n💡 ROUTINE DASHBOARD MENU")
        print("1. View Dashboard Layout")
        print("2. Add Task to Profile")
        print("3. Clear Task from Profile")
        print("4. Terminate Engine")
        
        action = input("Select operation (1-4): ").strip()
        
        if action == "1":
            show_tasks(todo_data)
        elif action == "2":
            add_task(todo_data)
        elif action == "3":
            delete_task(todo_data)
        elif action == "4":
            print("Closing daily engine workspace. Goodbye!")
            break
        else:
            print("Invalid select instruction. Choose alternative index.")

if __name__ == "__main__":
    main()
