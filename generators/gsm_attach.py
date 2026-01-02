import random
import time

def generate_attach(imsi):
    return {
        "event": "GSM.ATTACH",
        "imsi": f"imsi-{hash(imsi) % 10000}",
        "lac": random.randint(1000, 2000),
        "cell_id": random.randint(1, 128),
        "timestamp": time.time()
    }

if __name__ == "__main__":
    for i in range(5):
        print(generate_attach(f"00101{i}"))
        time.sleep(1)
