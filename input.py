import time
import random
import signal
import sys
import json
import os

CONFIG_FILE = "config.json"

def load_alert_messages():
    """
    Load alert messages from a configuration file (config.json).
    If the file doesn't exist, return a default list of messages.
    """
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            data = json.load(f)
            return data.get("alert_messages", [])
    else:
        return [
            "Fire hazard! Evacuate the building!",
            "Danger! High voltage!",
            "Emergency! Contact authorities immediately!"
        ]

def save_alert_messages(alert_messages):
    """
    Save the alert messages to the configuration file (config.json).
    """
    with open(CONFIG_FILE, 'w') as f:
        json.dump({"alert_messages": alert_messages}, f, indent=4)

def display_alert(message):
    """
    Displays a safety alert message and plays an alert sound.

    Args:
        message (str): The message to display.
    """
    print("\a" * 3) 
    print(f"SAFETY ALERT: {message}")

def signal_handler(sig, frame):
    """
    Gracefully handle script termination (e.g., on Ctrl+C).
    """
    print("\nExiting safety alert system...")
    sys.exit(0)

def start_alert_system(alert_messages):
    """
    Starts the alert system that displays random alert messages at random intervals.
    
    Args:
        alert_messages (list): A list of safety alert messages.
    """
    try:
        while True:
            time.sleep(random.randint(5, 15))  
            display_alert(random.choice(alert_messages))
    except KeyboardInterrupt:
        print("\nPaused. Press Enter to resume or type 'exit' to quit.")
        user_input = input("> ").strip().lower()
        if user_input == 'exit':
            sys.exit(0)

def main_menu():
    """
    Displays the main menu for the safety alert application.
    """
    alert_messages = load_alert_messages()

    print("Welcome to the Safety Alert System")

    while True:
        print("\nMenu:")
        print("1. Start Alert System")
        print("2. Add Custom Alert Message")
        print("3. View All Alert Messages")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            print("Starting the alert system...")
            start_alert_system(alert_messages)

        elif choice == '2':
            new_message = input("Enter your custom alert message: ").strip()
            if new_message:
                alert_messages.append(new_message)
                save_alert_messages(alert_messages)
                print("Custom alert message added and saved.")

        elif choice == '3':
            print("Current Alert Messages:")
            for idx, message in enumerate(alert_messages, 1):
                print(f"{idx}. {message}")

        elif choice == '4':
            print("Exiting the application.")
            sys.exit(0)

        else:
            print("Invalid option. Please choose a valid number.")

if __name__ == "__main__":

    signal.signal(signal.SIGINT, signal_handler)

    main_menu()
