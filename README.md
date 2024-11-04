 # My Python Site

This is a simple one-page website 
## Prerequisites

- Docker
- Docker Compose

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/anyviewww/my_site.git
    cd my_site
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

3. Open your browser and navigate to `http://localhost` to see the website.

## Project Structure

- `app.py`: The main Flask application.
- `requirements.txt`: List of Python dependencies.
- `Dockerfile`: Docker configuration for the Flask application.
- `docker-compose.yml`: Docker Compose configuration.
- `templates/index.html`: The HTML template for the home page.
- `static/style.css`: Custom CSS styles.
- `nginx.conf`: Nginx configuration file.
- `logs.json`: Log file for application events.

## Contributing

Feel free to open issues or pull requests if you have any suggestions or improvements.
