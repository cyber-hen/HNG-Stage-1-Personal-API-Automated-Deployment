---

# 🚀 Personal API – Automated Deployment (HNG Stage 1)

A high‑performance **Personal API** built with **FastAPI** and deployed on an **AWS EC2** instance.  
This project demonstrates backend engineering combined with practical DevOps workflows, including **Nginx reverse proxying**, **Systemd process management**, and **SSL/TLS automation** with Certbot.

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|------------|
| **Language** | Python 3.10+ |
| **Framework** | FastAPI |
| **Server** | Uvicorn |
| **Reverse Proxy** | Nginx |
| **Infrastructure** | AWS EC2 (Ubuntu 24.04 LTS) |
| **SSL/TLS** | Certbot (Let’s Encrypt) |

---

## ⚙️ Local Development Setup

Follow the steps below to run the API locally:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/hng-stage1-api.git
cd hng-stage1-api
```

### 2. Create & Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
# Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Development Server
```bash
uvicorn main:app --reload
```

Your API will be available at:  
**`http://127.0.0.1:8000`**

---

## 📡 API Endpoints

All endpoints return `application/json` with **HTTP 200 OK**.

### **1. Root**
**GET /**  
Checks basic API availability.  
**Response:**
```json
{ "message": "API is running" }
```

### **2. Health Check**
**GET /health**  
Used for uptime monitoring.  
**Response:**
```json
{ "message": "healthy" }
```

### **3. Personal Info**
**GET /me**  
Returns developer identification details.  
**Response:**
```json
{
  "name": "Henry Awoseyi",
  "email": "your-email@example.com",
  "github": "https://github.com/yourusername"
}
```

---

## 🛠️ Production Deployment Architecture

This project is deployed on an AWS EC2 instance with a focus on **security**, **reliability**, and **automation**.

### **1. Process Management – Systemd**
A Systemd service (`/etc/systemd/system/hngapi.service`) ensures:
- Automatic startup on boot  
- Automatic restart on failure  
- Decoupling from SSH sessions  

### **2. Reverse Proxy – Nginx**
Nginx handles:
- Routing external traffic to Uvicorn (port 8000)
- Hiding internal ports from the public internet
- Logging and request handling at the edge

### **3. SSL/TLS – Certbot**
The domain is secured using **Let’s Encrypt**, with:
- Automated certificate issuance  
- Auto‑renewal  
- Forced HTTPS via 301 redirect  

---

## 🔗 Live API URL

**[https://hngdevops-henry-awoseyi.duckdns.org/](https://hngdevops-henry-awoseyi.duckdns.org/)**

---

## 📘 Key Lessons Learned

- **Persistence Matters:** Systemd ensures your application survives reboots and crashes.  
- **Reverse Proxying is Essential:** Nginx provides security, structure, and flexibility for production traffic.  
- **SSL Should Be Automated:** Certbot simplifies certificate management and enforces modern security standards.

---
