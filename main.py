from datetime import datetime, timedelta
import os

class DuplicateVisitorError(Exception):
    pass

class EarlyEntryError(Exception):
    pass

FILENAME = "visitors.txt"

def ensure_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w') as f:
            pass

def get_last_visitor():
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        return None
    
    with open(FILENAME, 'r') as f:
        lines = f.readlines()
        if not lines:
            return None
        # Parse based on the test format "Name | Timestamp"
        return lines[-1].strip().split(" | ")

def add_visitor(visitor_name):
    last_entry = get_last_visitor()
    
    # 1. Check for Duplicates (Consecutive)
    if last_entry and last_entry[0] == visitor_name:
        raise DuplicateVisitorError(f"{visitor_name} was the last visitor.")

    # Write to file
    timestamp = datetime.now().isoformat()
    with open(FILENAME, 'a') as f:
        f.write(f"{visitor_name} | {timestamp}\n")

def main():
    ensure_file()
    name = input("Enter visitor's name: ")
    try:
        add_visitor(name)
        print("Visitor added successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()