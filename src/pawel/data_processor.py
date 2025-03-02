from loguru import logger


class DataProcessor:
    def __init__(self):
        logger.info("Data processor initialized")

    def process_data(self, data):
        """Process the data when it's updated"""
        logger.info(f"Processing data: {data}")

        name = data.get('name', '')
        number = data.get('number', '0')

        # Example processing logic
        results = {
            'name_length': len(name),
            'name_uppercase': name.upper(),
            'number_value': number
        }

        # You could do more complex operations here
        try:
            num_value = int(number)
            results['is_even'] = (num_value % 2 == 0)
            results['squared'] = num_value * num_value
        except ValueError:
            results['is_even'] = False
            results['squared'] = 0

        logger.info(f"Processing results: {results}")
        return results

    def save_to_file(self, data):
        """Save the data to a file"""
        try:
            with open("data_log.txt", "a") as f:
                f.write(
                    f"Name: {data.get('name', '')}, Number: {data.get('number', '0')}\n")
            logger.info("Data saved to file successfully")
            return True
        except Exception as e:
            logger.error(f"Error saving to file: {e}")
            return False
