# Chocolate House Application

This is a simple Flask application to manage a chocolate house's seasonal flavor offerings, ingredient inventory, customer flavor suggestions, and allergy concerns.

## How to Run the Code

### Prerequisites

Make sure you have the following installed:

- Python 3.11 or higher
- pip (Python package installer)
- Docker (if using the Docker method)

### Running Locally (Without Docker)

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd chocolateHouse
   ```
2. Create a virtual environment

    ```
    python -m venv venv
    source venv/bin/activate    # On windows `venv\Scripts\activate`
    ```
3. Install dependencies
    
    ```
    pip install -r requirements.txt
    ```
4. Run the application

    ```
    python app.py
    ```
5. Open your web browser and go to http://127.0.0.1:5000 to access the application.


### Running Locally (With Docker)

1. Build the docker image

    ```bash
    docker build -t chocolate_house .
    ```
2. Run the docker container

    ```bash
    docker run -d -p 5000:5000 chocolate_house
    ```

3. Open your web browser and go to http://127.0.0.1:5000 to access the application.