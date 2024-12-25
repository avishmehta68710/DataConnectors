# Data Connectors

## Problem Statement
The challenge is to obtain Amazon public data without resorting to web scraping or third party proxies, which can be unreliable and cost a lot of money.

## Solution
This project provides a solution to fetch Amazon public data for any region and any brand without scraping. It leverages Amazon's public APIs and other legitimate data sources to gather the required information.

## Use Case
- **Market Analysis**: Businesses can use this data to analyze market trends and competitor performance.
- **Product Research**: Researchers can gather data on product reviews, ratings, and sales to study consumer behavior.
- **Inventory Management**: Sellers can track inventory levels and sales performance across different regions.

## Development Guidelines
1. **Setup Environment**:
    - Ensure you have Python and pip installed.
    - Clone the repository: `git clone <repository-url>`
    - Navigate to the project directory: `cd data-connectors`
    - Create a virtual environment: `python -m venv venv`
    - Activate the virtual environment:
        - On macOS/Linux: `source venv/bin/activate`
        - On Windows: `venv\Scripts\activate`
    - Install dependencies: `pip install -r requirements.txt`

2. **Database Configuration**:
    - Ensure PostgreSQL is installed and running.
    - Create a `.env` file in the project root with the following content:
        ```dotenv
        POSTGRES_DB=<your-database-name>
        POSTGRES_USER=<db-username>
        POSTGRES_PASSWORD=<db-password>
        POSTGRES_HOST=<db-host>
        POSTGRES_PORT=<db-port>
        ```
    - Create a schema named `amazon` in your PostgreSQL database.
    - Apply migrations: `python manage.py migrate`

3. **Running the Project**:
    - Start the development server: `python manage.py runserver`
    - Access the application at `http://localhost:8000`
    - The Swagger documentation is available at `http://localhost:8000/swagger-ui/`

## Contribution Guidelines
1. **Fork the Repository**: Click the "Fork" button on the repository's GitHub page.
2. **Clone Your Fork**: Clone your forked repository to your local machine.
    ```bash
    git clone <your-fork-url>
    cd data-connectors
    ```
3. **Create a Branch**: Create a new branch for your feature or bugfix.
    ```bash
    git checkout -b feature/your-feature-name
    ```
4. **Make Changes**: Implement your changes and commit them with a descriptive message.
    ```bash
    git add .
    git commit -m "Add feature: your feature description"
    ```
5. **Push Changes**: Push your changes to your forked repository.
    ```bash
    git push origin feature/your-feature-name
    ```
6. **Create a Pull Request**: Open a pull request from your forked repository to the main repository.

Please ensure your code adheres to the project's coding standards and includes appropriate tests. All contributions are welcome and appreciated!
