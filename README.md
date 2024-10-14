# motion sensor_project
# **Setup and Deployment Instructions**

## **Installation and Configuration**
```bash
sudo apt update && sudo apt install python3-picamera && sudo pip3 install RPi.GPIO
sudo raspi-config
```
- Navigate to **Interfacing Options** → **Camera** → **Enable**

## **Python Script Setup**
1. Save the provided script as `motion_sensor.py`
2. Replace the placeholders with your credentials:
   ```python
   'your_email@gmail.com'
   'your_password'
   'recipient_email@gmail.com'
   ```

## **Running the Script**
```bash
python3 motion_sensor.py
```
