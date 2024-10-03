from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from geopy.geocoders import Nominatim

class GPSApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Getting GPS location...", font_size='20sp')
        self.layout.add_widget(self.label)

        # Schedule the update function to run every 10 seconds
        Clock.schedule_interval(self.update_location, 10)

        return self.layout

    def get_real_location(self):
        """
        Uses Geopy to fetch the approximate real location based on IP.
        """
        geolocator = Nominatim(user_agent="Safety Alert App")
        location = geolocator.geocode("Your City")
        if location:
            return location.latitude, location.longitude
        else:
            return None, None

    def update_location(self, dt):
        """
        Updates the displayed GPS location with real location data.
        """
        latitude, longitude = self.get_real_location()
        if latitude and longitude:
            self.label.text = f"Latitude: {latitude:.6f}, Longitude: {longitude:.6f}"
        else:
            self.label.text = "Unable to fetch location"

# Run the Kivy app
if __name__ == '__main__':
    GPSApp().run()
