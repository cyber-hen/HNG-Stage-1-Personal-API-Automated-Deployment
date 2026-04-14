# 🚀 Personal API – Automated Deployment (HNG Stage 1)

A high‑performance **Personal API** built with **FastAPI** and deployed on an **AWS EC2** instance.  
This project demonstrates practical backend engineering and DevOps workflows, including:

- Nginx reverse proxying  
- Systemd process management  
- SSL/TLS automation with Certbot  
- Automated local startup using a `run.sh` script  

---

## 🧰 Tech Stack

| Layer             | Technology                |
|------------------|---------------------------|
| **Language**      | Python 3.10+             |
| **Framework**     | FastAPI                  |
| **Server**        | Uvicorn                  |
| **Reverse Proxy** | Nginx                    |
| **Infrastructure**| AWS EC2 (Ubuntu 24.04)   |
| **SSL/TLS**       | Certbot (Let’s Encrypt)  |

---

## ⚡ Quick Start (Auto‑Run Enabled)

This project includes a `run.sh` script that automatically:

- Creates a virtual environment  
- Installs dependencies  
- Starts the FastAPI server  

### **1. Clone the repository**

```bash
git clone https://github.com/cyber-hen/HNG-Stage-1-Personal-API-Automated-Deployment.git
cd HNG-Stage-1-Personal-API-Automated-Deployment

```
2. Make the script executable (first time only)
bash
chmod +x run.sh

3. Run the API
bash
./run.sh
Your API will be available at:

Code
http://127.0.0.1:8000

🛠️ Auto‑Run Script (run.sh)
bash
#!/bin/bash

# Create venv if missing
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the API
uvicorn main:app --host 0.0.0.0 --port 8000

⚙️ Local Development Setup (Manual Option)
If you prefer running manually:

1. Clone the repository
bash
git clone https://github.com/yourusername/hng-stage1-api.git
cd hng-stage1-api

2. Create & activate a virtual environment
bash
python3 -m venv venv
source venv/bin/activate
# Windows:
# venv\Scripts\activate

3. Install dependencies
bash
pip install -r requirements.txt

4. Start the development server
bash
uvicorn main:app --reload

📡 API Endpoints
All endpoints return application/json with HTTP 200 OK.

GET /
Returns API availability status.

json
{ "message": "API is running" }

GET /health
Used for uptime monitoring.

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

1. Systemd Process Management
A Systemd service (/etc/systemd/system/hngapi.service) ensures:

Automatic startup on boot

Automatic restart on failure

Decoupling from SSH sessions

2. Nginx Reverse Proxy
Nginx is configured to:

Route external traffic to Uvicorn (port 8000)

Hide internal ports from the public internet

Handle logging and request processing at the edge

3. SSL/TLS with Certbot
The domain is secured using Let’s Encrypt, providing:

Automated certificate issuance

Auto‑renewal

Enforced HTTPS via 301 redirect

🔗 Live API URL
Code
https://hngdevops-henry-awoseyi.duckdns.org/

📘 Key Lessons Learned
Persistence matters: Systemd ensures the application survives reboots and crashes.

Reverse proxying is essential: Nginx provides security, structure, and flexibility for production traffic.

SSL should be automated: Certbot simplifies certificate management and enforces modern security standards.
