# Real-Time Log Dashboard

## Overview

This project is a real-time log monitoring and visualization dashboard built using Docker, Streamlit, MongoDB, and Kafka. It simulates a real-time log pipeline by generating logs from a producer and consuming those logs through a consumer, which are then displayed on a dashboard built with Streamlit.

## Features

- **Real-time Log Dashboard**: Visualize logs in real-time.
- **Filter Logs**: Filter logs by log level and service.
- **MongoDB Storage**: Logs are stored in MongoDB for persistence.
- **Kafka Message Queue**: Kafka is used to simulate a message queue between the producer and consumer.
- **Dockerized**: All components (Kafka, Zookeeper, MongoDB, Streamlit) are containerized using Docker.

## Prerequisites

Make sure you have the following installed:

- Docker
- Docker Compose

## Setup

### 1. Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/FakayejoTaiwoOlawale/realtime-log-pipeline.git
cd your-repository-name
