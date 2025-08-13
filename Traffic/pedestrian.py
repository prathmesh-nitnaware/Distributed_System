# PEDESTRIAN SERVER (PC-C)
from xmlrpc.server import SimpleXMLRPCServer
import time

def pedestrian_signal(vehicle_pair_off):
    print(f"📥 Pedestrian server received signal for Junction {vehicle_pair_off}")

    # Invert logic
    pedestrian_on = vehicle_pair_off
    pedestrian_off = 34 if vehicle_pair_off == 12 else 12

    msg1 = f"🚷 Pedestrian Signal OFF at Junction {pedestrian_off} (Vehicles going)"
    print(msg1)
    time.sleep(1)

    msg2 = f"🚶 Pedestrian Signal ON at Junction {pedestrian_on} (Vehicles stopped)"
    print(msg2)
    time.sleep(1)

    print("📤 Responding back to Signal Manipulator.")
    return [msg1, msg2]

server = SimpleXMLRPCServer(("0.0.0.0", 9000))
server.register_function(pedestrian_signal, "pedestrian_signal")
print("👣 Pedestrian Server running on port 9000...")
server.serve_forever()