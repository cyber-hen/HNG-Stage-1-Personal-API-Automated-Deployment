📌 Project Overview
This project is a high-performance Personal API built with Python (FastAPI) and deployed on an AWS EC2 instance. It serves as a demonstration of backend development integrated with DevOps best practices, including Reverse Proxying with Nginx, Process Management with Systemd, and SSL Encryption.

Tech Stack
Language: Python 3.10+

Framework: FastAPI

Server: Uvicorn

Proxy: Nginx

Infrastructure: AWS (Ubuntu 24.04 LTS)

SSL/TLS: Certbot (Let's Encrypt)

🚀 Local Setup & Installation
To run this project on your local machine for development:

Clone the Repository:

Bash
git clone https://github.com/yourusername/hng-stage1-api.git
cd hng-stage1-api
Create a Virtual Environment:

Bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

Bash
pip install -r requirements.txt
Run the Application:

Bash
uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000.

🛰️ API Endpoints & Expected Responses
All responses are returned in application/json format with an HTTP 200 status code.

1. Root Endpoint
GET /

Description: Basic connectivity check.

Response:

JSON
{ "message": "API is running" }
2. Health Check
GET /health

Description: Used by monitoring tools to verify service status.

Response:

JSON
{ "message": "healthy" }
3. Personal Info
GET /me

Description: Returns developer identification details.

Response:

JSON
{
  "name": "Henry Awoseyi",
  "email": "your-email@example.com",
  "github": "https://github.com/yourusername"
}
🛡️ Production Deployment Details (Step-by-Step)
This API is hosted on a VPS with a focus on Persistence and Security.

1. Process Management (Systemd)
To ensure the API stays online after server reboots or crashes, a Systemd service was configured:

Service File: /etc/systemd/system/hngapi.service

Logic: The service is configured with Restart=always and is enabled to start on boot.

2. Reverse Proxy (Nginx)
Nginx acts as the entry point for all web traffic, forwarding requests to the internal Uvicorn server running on Port 8000.

Why: This prevents direct exposure of the application port and allows for better logging and SSL termination.

3. SSL Encryption
The domain is secured using Let's Encrypt (Certbot), enforcing a 301 Permanent Redirect from HTTP to HTTPS to ensure all data in transit is encrypted.

🔗 Live Deployment URL
API Base URL: https://your-domain-name.com

🛠️ Lessons Learned
Persistence is Key: Implementing Systemd taught me the importance of decoupled process management—your code should run independently of your SSH session.

The Proxy Shield: Using Nginx as a reverse proxy highlighted how to manage traffic flow and security headers at the edge of the infrastructure.

Automated SSL: Configuring Certbot demonstrated how modern DevOps tools handle the lifecycle of security certificates automatically.
