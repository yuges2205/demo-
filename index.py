import time

for minute in range(1, 16):
    print(f"Minute {minute}: This is your message")
    time.sleep(60)  # wait for 60 seconds (1 minute)

print("15 minutes completed!")
