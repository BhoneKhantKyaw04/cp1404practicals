class Monitor:
    """
    A class to represent a computer monitor with a specific model, width, and height.

    Attributes:
        model (str): The model name of the monitor.
        width (int): The width resolution of the monitor in pixels.
        height (int): The height resolution of the monitor in pixels.
    """

    def __init__(self, model, width, height):
        """
        Initialize a Monitor instance with model, width, and height.

        Args:
            model: The model name of the monitor.
            width: The width resolution in pixels.
            height: The height resolution in pixels.
        """
        self.model = model
        self.width = width
        self.height = height

    def get_resolution(self):
        """
        Returns the resolution of the monitor as a tuple (width, height).

        Returns:
            A tuple containing (width, height).
        """
        return (self.width, self.height)

    def get_total_pixels(self):
        """
        Calculates and returns the total number of pixels on the monitor.

        Returns:
            The total pixels (width * height).
        """
        return self.width * self.height

    def __eq__(self, other):
        """
        Checks if two Monitor objects are equal based on width and height.

        Args:
            other: Another Monitor object to compare with.

        Returns:
            True if both monitors have the same width and height, False otherwise.
        """
        if not isinstance(other, Monitor):
            return False
        return self.width == other.width and self.height == other.height
