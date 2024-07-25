# Real-time Crypto Price Tracker

A real-time Django application designed to track the price of your preferred cryptocurrency.

## Technologies Used

- **Django**: Employed as the full-stack framework.
- **Django Rest Framework**: Used to create API endpoints.
- **Celery**: Implemented for scheduling and updating prices at regular intervals.
- **Redis**: Utilized to manage Celery tasks.
- **PostgreSQL**: Used as the database to store crypto and price data.
- **Docker and Docker Compose**: Used to containerize the entire deployment and running process.

## Getting Started

### Prerequisites

Ensure that Docker and Docker Compose are installed on your system.

- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/shubRaj/realtime-crypto-price-tracker.git
    cd realtime-crypto-price-tracker
    ```

2. **Build and start the containers:**
    ```bash
    docker-compose up --build -d
    ```

3. The application should now be live at: [http://localhost:8000](http://localhost:8000).
