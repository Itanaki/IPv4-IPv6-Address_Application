import tkinter as tk
import requests
from PIL import Image, ImageTk

# Function to fetch IP information
def fetch_ip_info():
    # URL of the public API (replace with your actual API key)
    api_key = "at_0NzHsrw4nnVqZehpZKPYTezgFGNh2"  # Replace with your actual API key
    url = f"https://geo.ipify.org/api/v1?apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json()
        
        # Extract information
        ipv4 = data.get('ip', 'N/A')
        ipv6 = data.get('ip', 'N/A') if ':' in data.get('ip', '') else 'N/A'  # Check if it's an IPv6 address
        location = data.get('location', {})
        city = location.get('city', 'N/A')
        region = location.get('region', 'N/A')
        country = location.get('country', 'N/A')
        isp = data.get('isp', 'N/A')
        asn = data.get('as', {}).get('asn', 'N/A')
        
        # Update the GUI with IP information
        result_text.set(f"IPv4 Address: {ipv4}\nIPv6 Address: {ipv6}\nCity: {city}\nRegion: {region}\nCountry: {country}\nISP: {isp}\nASN: {asn}")

    except requests.exceptions.RequestException as e:
        result_text.set(f"Error fetching data: {e}")




# Initialize the main window
root = tk.Tk()
root.title("IP Address Information")
root.geometry("400x450")
root.configure(bg="white")

# Container frame for image and header
frame_top = tk.Frame(root, bg="white")
frame_top.pack(pady=5, padx=5, fill="x")

# Load and display an image
img = Image.open("dheboys.png")  # Replace with the actual path to your image
img = img.resize((200, 200), Image.LANCZOS)  # Updated resizing method

global img_tk  # Ensure img_tk is global to prevent garbage collection
img_tk = ImageTk.PhotoImage(img)
img_label = tk.Label(frame_top, image=img_tk, bg="white")
img_label.pack(side="left", padx=100)



# Header Label
header_label = tk.Label(root, text="IP Address Information Checker", font=("Helvetica", 16, "bold"), pady=10,bg="white")
header_label.pack()

# Ip Address Info
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", anchor="nw",bg='white')
result_label.pack(padx=30, pady=10, fill="both", expand=True)


#Button for fetching IP
fetch_button = tk.Button(root, text="Fetch IP Information", command=fetch_ip_info, )
fetch_button.pack(pady=20)



#start gui
root.mainloop()
