# client.py
# VEHICLE CONTROLLER CLIENT (PC-A)
import xmlrpc.client
import random

server = xmlrpc.client.ServerProxy("http://localhost:8000/")  # Signal Manipulator

def signal_controller():
    active_pair = random.choice([12, 34])
    pair_to_turn_off = 34 if active_pair == 12 else 12

    print(f"✅ Active Junction: {active_pair}")
    print(f"🚦 Turning OFF Junction: {pair_to_turn_off}")

    response = server.signal_manipulator(pair_to_turn_off)

    print("📩 Full Response:")
    for msg in response:
        print(msg)

if __name__ == "__main__":
    signal_controller()