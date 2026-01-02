import time

def burst(count=10, interval=0.3):
    for i in range(count):
        print(f"[GEN] Registration attempt {i}")
        time.sleep(interval)

if __name__ == "__main__":
    burst()
