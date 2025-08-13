# SIGNAL MANIPULATOR SERVER (PC-B)
import time
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer

# Connect to Pedestrian Server (PC-C)
pedestrian_server = xmlrpc.client.ServerProxy("http://localhost:9000/")

def signal_manipulator(pair):
    print(f"📥 Received request to turn off Junction {pair}")
    messages = []

    msg1 = f"🟡 Junction {pair} is now YELLOW."
    print(msg1)
    messages.append(msg1)
    time.sleep(1)

    msg2 = f"🔴 Junction {pair} is now RED. Vehicles must stop."
    print(msg2)
    messages.append(msg2)
    time.sleep(1)

    other = 34 if pair == 12 else 12
    msg3 = f"🟢 Junction {other} is now GREEN. Vehicles can go."
    print(msg3)
    messages.append(msg3)
    time.sleep(1)

    # 🧠 Call Pedestrian Server
    print("📞 Calling Pedestrian Server...")
    pedestrian_msgs = pedestrian_server.pedestrian_signal(pair)

    # Combine and return all messages
    full_response = messages + pedestrian_msgs
    print("📤 Sending combined response to Vehicle Client.")
    return full_response

server = SimpleXMLRPCServer(("0.0.0.0", 8000))
server.register_function(signal_manipulator, "signal_manipulator")
print("🚦 Signal Manipulator Server running on port 8000...")
server.serve_forever()
