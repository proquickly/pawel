from flask import Flask, request, jsonify
from loguru import logger
from data_processor import DataProcessor


class DataStore:
    def __init__(self):
        self.current_values = {
            "name": "",
            "number": "0"
        }


def create_app():
    app = Flask(__name__)
    data_store = DataStore()
    # Create a processor instance
    data_processor = DataProcessor()

    @app.route('/update', methods=['POST'])
    def update_values():
        try:
            data = request.json
            logger.info(f"Received data: {data}")

            if 'name' in data:
                data_store.current_values['name'] = data['name']

            if 'number' in data:
                data_store.current_values['number'] = data['number']

            processing_results = data_processor.process_data(
                data_store.current_values)

            data_processor.save_to_file(data_store.current_values)

            logger.info(f"Updated values: {data_store.current_values}")
            return jsonify({
                "status": "success",
                "data": data_store.current_values,
                "processing_results": processing_results
            }), 200

        except Exception as e:
            logger.error(f"Error processing request: {e}")
            return jsonify({"status": "error", "message": str(e)}), 500

    @app.route('/values', methods=['GET'])
    def get_values():
        return jsonify(data_store.current_values), 200

    return app


if __name__ == '__main__':
    app = create_app()
    logger.info("Starting server on port 5000...")
    app.run(debug=True, host='0.0.0.0', port=5000)
