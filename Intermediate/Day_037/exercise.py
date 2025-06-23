from pixela import Pixela

USERNAME = "YOUR_USERNAME_HERE"  # Replace with your actual username
TOKEN = "YOUR_TOKEN_HERE"  # Replace with your actual token

pixela = Pixela(username=USERNAME, token=TOKEN)

# Create a new user if it doesn't exist
# Uncomment the following line to create a new user. This should only be done once.
pixela.create_user(username=USERNAME, token=TOKEN)

# Update user profile
pixela.update_user_profile(
    display_name="YOUR_DISPLAY_NAME",  # Replace with your actual display name
    timezone="YOUR_TIMEZONE",  # Replace with your actual timezone, e.g., "Asia/Jakarta"
    url="YOUR_URL",  # Replace with your actual URL, e.g., "https://yourwebsite.com"
    pinned_graphs=["GRAPH_ID_1", "GRAPH_ID_2"]  # Replace with your actual graph IDs
)

# Delete the graph if it exists (optional, for cleanup)
pixela.delete_graph("GRAPH_ID")  # Replace with your actual graph ID

# Create a new graph for tracking Python study hours. This should only be done once.
pixela.create_graph(
    graph_id="YOUR_GRAPH_ID",  # Replace with your actual graph ID
    name="NAME_OF_YOUR_GRAPH",  # Replace with your actual graph name
    unit="UNIT_OF_YOUR_GRAPH",  # Replace with your actual unit, e.g., "hours"
    data_type="float",  # Use "int" for integer values or "float" for decimal values
    color="shibafu",  # Replace with your preferred color, e.g., "shibafu", "momiji"
)

# Add a new pixel to the graph for today's date with 4 hours of study
pixela.create_pixel(
    graph_id="YOUR_GRAPH",
    quantity="4.0",  # Replace with the actual quantity, e.g., "4.0" for 4 hours
    date="YYYYMMDD"  # Defaults to today's date
)

# Add multiple pixels to the graph
pixela.create_multiple_pixels(
    graph_id="python-graph",
    pixels=[
        {"date": "YYYYMMDD", "quantity": "VALUE"},
        {"date": "YYYYMMDD", "quantity": "VALUE"},
        {"date": "YYYYMMDD", "quantity": "VALUE"}
    ]
)

# Update a pixel for a specific date
pixela.update_pixel(
    graph_id="YOUR_GRAPH",
    date=None,  # Defaults to today's date
    quantity=8.0  # New value for the pixel
)


# Delete a pixel for a specific date
pixela.delete_pixel(
    graph_id="YOUR_GRAPH",
    date="YYYYMMDD"  # Replace with the actual date in YYYYMMDD format
)