# Multi-Proccessing-And-Edge-Detection

## Camera stream

`fps.py`, `fpsthread.py` and `main.py` read the camera's RTSP link from the `RTSP_URL` environment variable, so the camera password is never written into the code.

Windows (PowerShell):

```powershell
$env:RTSP_URL = "rtsp://user:password@camera-ip:554/Streaming/channels/1001"
python fpsthread.py
```

Linux / macOS:

```bash
export RTSP_URL="rtsp://user:password@camera-ip:554/Streaming/channels/1001"
python fpsthread.py
```
