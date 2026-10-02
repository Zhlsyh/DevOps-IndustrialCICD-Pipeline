from fastapi import FastAPI, HTTPException

app = FastAPI(title="Industrial Telemetry API")

@app.get("/")
def read_root():
    return {"status": "online", "message": "Industrial IoT Gateway active"}

@app.get("/telemetry/{device_id}")
def get_telemetry(device_id: str):
    if device_id == "ESP32_01":
        return {
            "device_id": device_id,
            "temperature": 28.5,
            "status": "PASS"
        }
    raise HTTPException(status_code=404, detail="Device not found")