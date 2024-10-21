import requests
import tkinter as tk
from tkinter import messagebox

def get_ipv4():
    try:
        response = requests.get('https://api.ipify.org?format=json').json()
        return response["ip"]
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch IPv4 address: {e}")
        return None

def get_ipv6():
    try:
        response = requests.get('https://api64.ipify.org?format=json').json()
        ipv6 = response["ip"]
        # If the response is an IPv4-mapped IPv6 address, skip showing it
        if ':' in ipv6:  # Simple check for IPv6 formatting
            return ipv6
        else:
            return None
    except Exception as e:
        return None  # Return None if IPv6 is not available or API fails

def get_location(ip_address):
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        location_data = {
            "IP Address": ip_address, 
            "City": response.get("city", "N/A"),
            "Region": response.get("region", "N/A"),
            "Country": response.get("country_name", "N/A")
        }
        return location_data
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch location data: {e}")
        return None

def show_location():
    ipv4 = get_ipv4()
    ipv6 = get_ipv6()
    
    if ipv4:
        location_v4 = get_location(ipv4)
        ipv4_location = (f"IPv4 Address: {location_v4['IP Address']}\n"
                         f"City: {location_v4['City']}\n"
                         f"Region: {location_v4['Region']}\n"
                         f"Country: {location_v4['Country']}\n\n")
    else:
        ipv4_location = "IPv4 Address: Not available\n\n"
    
    if ipv6:
        location_v6 = get_location(ipv6)
        ipv6_location = (f"IPv6 Address: {location_v6['IP Address']}\n"
                         f"City: {location_v6['City']}\n"
                         f"Region: {location_v6['Region']}\n"
                         f"Country: {location_v6['Country']}\n")
    else:
        ipv6_location = "No IPv6 address detected"

    result_text.set(ipv4_location + ipv6_location)

# Initialize the main window
root = tk.Tk()
root.title("IP Location Finder")
root.geometry("400x400")

# Label and Button widgets
label = tk.Label(root, text="Click the button to get your IPv4/IPv6 address and location:", padx=20, pady=20)
label.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", padx=10, pady=10)
result_label.pack()

button = tk.Button(root, text="Get Location", command=show_location, padx=10, pady=5)
button.pack()

# Run the application
root.mainloop()
