🚀 Personal API – Automated Deployment (HNG Stage 1)
A lightweight, high‑performance Personal API built with FastAPI and deployed on an AWS EC2 instance.
This project demonstrates practical backend engineering and DevOps workflows, including:

Nginx reverse proxying

Systemd service management

Automated SSL/TLS with Certbot

Production‑grade deployment structure

🧰 Tech Stack
Layer	Technology
Language	Python 3.10+
Framework	FastAPI
Server	Uvicorn
Reverse Proxy	Nginx
Infrastructure	AWS EC2 (Ubuntu 24.04 LTS)
SSL/TLS	Certbot (Let’s Encrypt)
⚡ Local Development Setup
Follow the steps below to run the API locally.

1. Clone the Repository
bash
git clone https://github.com/yourusername/hng-stage1-api.git
cd hng-stage1-api
2. Create & Activate a Virtual Environment
bash
python3 -m venv venv
source venv/bin/activate
# Windows:
# venv\Scripts\activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Start the Development Server
bash
uvicorn main:app --reload
Your API will be available at:

Code
http://127.0.0.1:8000
📡 API Endpoints
All endpoints return application/json with HTTP 200 OK.

GET /
Returns API availability status.

json
{ "message": "API is running" }
GET /health
Used for uptime and monitoring.

json
{ "message": "healthy" }
GET /me
Returns developer identification details.

json
{
  "name": "Henry Awoseyi",
  "email": "your-email@example.com",
  "github": "https://github.com/yourusername"
}
🏗️ Production Deployment Architecture
This API is deployed on an AWS EC2 instance with a focus on security, reliability, and automation.

Systemd Process Management
A custom service file (/etc/systemd/system/hngapi.service) ensures:

Automatic startup on boot

Automatic restart on failure

Decoupling from SSH sessions

Nginx Reverse Proxy
Nginx handles:

Routing external traffic to Uvicorn

Protecting internal ports

Adding custom headers for monitoring

Acting as the public-facing entry point

SSL/TLS with Certbot
The domain is secured using Let’s Encrypt:

Automated certificate issuance

Auto‑renewal

Enforced HTTPS via 301 redirect

🔗 Live API URL
Code
https://your-domain-name.com
📘 Key Lessons Learned
Systemd provides resilience — your app survives crashes and reboots.

Nginx is essential for secure, structured production traffic.

SSL automation matters — Certbot simplifies certificate management and enforces modern security standards.
