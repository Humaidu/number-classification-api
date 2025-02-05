# Number Classification API

A simple Flask API that classifies numbers based on their mathematical properties and provides fun facts using the Numbers API.

## Features
- Checks if a number is **prime**, **perfect**, or an **Armstrong number**.
- Identifies whether a number is **even** or **odd**.
- Computes the **sum of its digits**.
- Fetches a **fun fact** from the Numbers API.
- Supports **CORS** for cross-origin requests.
- Returns responses in **JSON format**.

## Launch an Ubuntu EC2 Instance
1. Go to the AWS EC2 dashboard.
2. Click Launch Instance.
3. Select Ubuntu 22.04 LTS as the Amazon Machine Image (AMI).
4. Choose an instance type (t2.micro for free tier).
5. Configure Security Group:
    *Allow SSH (port 22)
    *Allow HTTP (port 80)
    *Allow TCP (port 5000) (for Flask)
6. Launch and connect to your instance:
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-public-ip

   ```
## Installation

1. **Install Required Packages**
   Update the system and install Python:

   ```bash
   sudo apt update -y
   sudo apt install python3 python3-pip nginx -y

   ```

2. **Clone the repository**
   ```bash
   git clone https://github.com/Humaidu/number-classification-api.git
   cd number-classification-api
   ```

3. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt

   ```

## Run Flask App

   ```bash
   python3 app.py

   ```
 If successful, open in your browser:

  ```bash
   http://your-ec2-public-ip:5000/api/classify-number?number=371

  ```


