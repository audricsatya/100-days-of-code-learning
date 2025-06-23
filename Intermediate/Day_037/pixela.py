import requests
import datetime as dt

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

class Pixela:
    """Class to interact with the Pixela API.

    This class provides methods to create users and graphs on the Pixela service,
    allowing for easy integration and management of Pixela's pixel tracking features.
    """

    def __init__(self, username=None, token=None):
        """
        Initializes the Pixela instance with optional username and token.

        Args:
            username (str, optional): The Pixela username. Defaults to None.
            token (str, optional): The Pixela user token. Defaults to None.
        """
        self.pixela_endpoint = PIXELA_ENDPOINT
        self.username = username
        self.token = token

    def create_user(self, username, token):
        """
        Creates a new user on Pixela.

        Args:
            username (str): The desired Pixela username.
            token (str): The desired Pixela user token.

        Raises:
            HTTPError: If the request to create the user fails.

        Prints:
            Success or failure message based on the response from the Pixela API.
        """
        user_params = {
            "token": token,
            "username": username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }
        response = requests.post(self.pixela_endpoint, json=user_params)
        response.raise_for_status()
        if response.status_code == 200:
            print("User created successfully.")
            self.username = username
            self.token = token
        else:
            print(f"Failed to create user: {response.status_code} - {response.text}")
    
    def update_user_profile(self, display_name=None, timezone=None, url=None, pinned_graphs=None):
        """ Updates the user's profile on Pixela.
        Args:
            display_name (str, optional): The display name for the user.
            timezone (str, optional): The timezone for the user.
            url (str, optional): A URL associated with the user.
            pinned_graphs (list, optional): A list of graph IDs to pin on the user's profile.
        Raises:
            ValueError: If username or token is not set.
        Prints:
            Success or failure message based on the response from the Pixela API.
        """
        if self.username is None or self.token is None:
            raise ValueError("Username and token must be set before updating the profile.")
        
        profile_endpoint = f"https://pixe.la/@{self.username}"
        headers = {
            "X-USER-TOKEN": self.token
        }
        profile_params = {}
        if display_name:
            profile_params["displayName"] = display_name
        if timezone:
            profile_params["timezone"] = timezone
        if url:
            profile_params["url"] = url
        if pinned_graphs:
            profile_params["pinnedGraphs"] = pinned_graphs
        response = requests.put(profile_endpoint, json=profile_params, headers=headers)
        print(response.text)
        # response.raise_for_status()
        if response.status_code == 200:
            print("User profile updated successfully.")
        else:
            print(f"Failed to update user profile: {response.status_code} - {response.text}")
    
    def create_graph(self, graph_id, name, unit, data_type, color, timezone="Asia/Jakarta"):
        """
        Creates a new graph for the user in the Pixela service.

        Args:
            graph_id (str): Unique identifier for the graph.
            name (str): Name of the graph.
            unit (str): Unit of measurement for the graph (e.g., "km", "hours").
            data_type (str): Type of data to be recorded ("int" or "float").
            color (str): Color code for the graph (e.g., "shibafu", "momiji").

        Raises:
            HTTPError: If the request to create the graph fails.

        Prints:
            Success or failure message based on the response from the Pixela API.
        """
        """Create a new graph for the user."""
        if self.username is None or self.token is None:
            raise ValueError("Username and token must be set before creating a graph.")
        graph_endpoint = f"{self.pixela_endpoint}/{self.username}/graphs"
        headers = {
            "X-USER-TOKEN": self.token
        }
        graph_params = {
            "id": graph_id,
            "name": name,
            "unit": unit,
            "type": data_type,
            "color": color,
            "timezone": timezone  # Set your timezone
        }
        response = requests.post(graph_endpoint, json=graph_params, headers=headers)
        print(response.text)
        response.raise_for_status()
        if response.status_code == 200:
            print("Graph created successfully.")
            print(f"Graph URL: https://pixe.la/v1/users/{self.username}/graphs/{graph_id}.html")
        else:
            print(f"Failed to create graph: {response.status_code} - {response.text}")

    def delete_graph(self, graph_id):
        """
        Deletes a graph from the Pixela service.

        Args:
            graph_id (str): The ID of the graph to be deleted.

        Raises:
            HTTPError: If the request to delete the graph fails.

        Prints:
            Success or failure message based on the response from the Pixela API.
        """
        if self.username is None or self.token is None:
            raise ValueError("Username and token must be set before deleting a graph.")
        graph_endpoint = f"{self.pixela_endpoint}/{self.username}/graphs/{graph_id}"
        headers = {
            "X-USER-TOKEN": self.token
        }
        response = requests.delete(graph_endpoint, headers=headers)
        response.raise_for_status()
        if response.status_code == 200:
            print("Graph deleted successfully.")
        else:
            print(f"Failed to delete graph: {response.status_code} - {response.text}")

    def create_pixel(self, graph_id, quantity, date=None):
        """
        Creates a new pixel for the specified graph.

        Args:
            graph_id (str): The ID of the graph to which the pixel will be added.
            quantity (float): The value of the pixel to be added.
            date (str, optional): The date for the pixel in YYYYMMDD format. Defaults to today.

        Raises:
            HTTPError: If the request to create the pixel fails.

        Prints:
            Success or failure message based on the response from the Pixela API.
        """

        if self.username is None or self.token is None:
            raise ValueError("Username and token must be set before creating a pixel.")
        pixel_endpoint = f"{self.pixela_endpoint}/{self.username}/graphs/{graph_id}"
        headers = {
            "X-USER-TOKEN": self.token
        }
        if date is None:
            date = dt.datetime.now().strftime("%Y%m%d")
        pixel_params = {
            "date": date,
            "quantity": str(quantity)
        }
        response = requests.post(pixel_endpoint, json=pixel_params, headers=headers)
        response.raise_for_status()
        if response.status_code == 200:
            print("Pixel created successfully.")
        else:
            print(f"Failed to create pixel: {response.status_code} - {response.text}")

    def create_multiple_pixels(self, graph_id, pixels):
        """
        Creates multiple pixels for the specified graph.

        Args:
            graph_id (str): The ID of the graph to which the pixels will be added.
            pixels (list): A list of dictionaries, each containing 'quantity' and optional 'date'.

        Raises:
            HTTPError: If the request to create the pixels fails.

        Prints:
            Success or failure message based on the response from the Pixela API.
        """
        if self.username is None or self.token is None:
            raise ValueError("Username and token must be set before creating multiple pixels.")
        
        for pixel in pixels:
            self.create_pixel(graph_id, pixel['quantity'], pixel.get('date'))

    def update_pixel(self, graph_id, quantity, date=None):
        """
        Updates an existing pixel for the specified graph.

        Args:
            graph_id (str): The ID of the graph containing the pixel to be updated.
            quantity (float): The new value for the pixel.
            date (str, optional): The date for the pixel in YYYYMMDD format. Defaults to today.

        Raises:
            HTTPError: If the request to update the pixel fails.

        Prints:
            Success or failure message based on the response from the Pixela API.
        """
        if self.username is None or self.token is None:
            raise ValueError("Username and token must be set before updating a pixel.")
        if date is None:
            date = dt.datetime.now().strftime("%Y%m%d")
        pixel_endpoint = f"{self.pixela_endpoint}/{self.username}/graphs/{graph_id}/{date}"
        headers = {
            "X-USER-TOKEN": self.token
        }
        pixel_params = {
            "quantity": str(quantity)
        }
        response = requests.put(pixel_endpoint, json=pixel_params, headers=headers)
        response.raise_for_status()
        if response.status_code == 200:
            print("Pixel updated successfully.")
        else:
            print(f"Failed to update pixel: {response.status_code} - {response.text}")
    
 