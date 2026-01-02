
import time
import random

def attach_cycle(cycles=5, base_delay=2):
    for i in range(cycles):
        print(f"[GEN] Trigger ATTACH cycle {i}")
        time.sleep(base_delay + random.uniform(0.5, 1.5))
        print(f"[GEN] Trigger DETACH cycle {i}")
        time.sleep(base_delay)

if __name__ == "__main__":
    attach_cycle()
