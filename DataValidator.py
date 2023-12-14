class DataValidator:
    """This class provides functionality to validate a list of strings by checking if each is a positive integer.
    It is useful in scenarios where user input needs to be validated for numerical processing."""

    def validate(self, input_list):
        """Processes a list of strings, validating each as a positive integer. Non integer and negative values
        are ignored.

        Args:
            input_list (str list): User input strings.

        Returns:
            list of int: Validated positive integers from the input."""
        valid_numbers = []
        for item in input_list:
            # Validate if each item is a digit and positive
            if item.isdigit() and int(item) > 0:
                valid_numbers.append(int(item))
        return valid_numbers
