class DataValidator:
    """A class to validate a list of user input strings, ensuring they are positive integers."""

    def validate(self, input_list):
        """Args:
            input_list: A list of strings to be validated.

        Returns:
            list: A list of valid positive integers."""
        valid_numbers = []
        for item in input_list:
            if item.isdigit() and int(item) > 0:
                valid_numbers.append(int(item))
        return valid_numbers
