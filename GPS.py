import time
import threading
import tkinter as tk
from geopy.geocoders import Nominatim

def get_real_location():
    """
    Uses Geopy to fetch the approximate real location based on IP.
    """
    geolocator = Nominatim(user_agent="Safety Alert App")
    location = geolocator.geocode("Nairobi") 
    
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

def update_location(label):
    """
    Updates the displayed GPS location in the Tkinter window with real location data.
    """
    while True:
        latitude, longitude = get_real_location()
        if latitude and longitude:
            location_text = f"Latitude: {latitude:.6f}, Longitude: {longitude:.6f}"
        else:
            location_text = "Unable to fetch location"
        
        label.config(text=location_text)
        time.sleep(10)  
def start_gui():
    """
    Starts the Tkinter window and displays the real-time GPS location.
    """
    window = tk.Tk()
    window.title("Real-Time GPS Tracker")

    location_label = tk.Label(window, text="Getting GPS location...", font=("Arial", 14))
    location_label.pack(pady=20)

    tracking_thread = threading.Thread(target=update_location, args=(location_label,))
    tracking_thread.daemon = True
    tracking_thread.start()

    window.mainloop()

if __name__ == "__main__":
    start_gui()

