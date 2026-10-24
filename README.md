# Robotica

Teaching material from Uni Junior (University of Porto summer programme). I used it to teach 14-17 year olds how a small robotic production line works: one line-following AGV and 8 robotic arms, each driven by a Raspberry Pi and coordinated over MQTT.

## What is here

| File | Purpose |
|---|---|
| `PUBLISH.py` / `SUBSCRIBE.py` | Minimal MQTT chat over a public broker (`broker.emqx.io`). Each student publishes on a topic named after themselves and subscribes to a classmate's topic. This was the first exercise in how the machines on the line talk to each other. |
| `AGV_CONTROL2.py` | Event-driven controller for the AGV (two motors, two IR line sensors, `gpiozero`). It is deliberately incomplete: the blanks marked `____` were filled in by the students during the session. |
| `guião 12ºano final.docx` | Step-by-step guide (in Portuguese) for assembling and running the full line. |

## How to run the MQTT exercise

```bash
pip install paho-mqtt
python PUBLISH.py     # terminal 1: enter your name
python SUBSCRIBE.py   # terminal 2: enter the other person's name
```

The scripts use the paho-mqtt 1.x client API. `AGV_CONTROL2.py` only runs on a Raspberry Pi wired to the AGV.

## Context

The MQTT scripts are adapted from a standard paho-mqtt example and simplified for the students. My own work was understanding the line's control code and Raspberry Pi OS setup well enough to explain it to a class, turning the AGV controller into a fill-in exercise, and writing the guide.
