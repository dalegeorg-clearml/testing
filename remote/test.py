import os
import socket

# Print all environment variables
for key, value in os.environ.items():
    print(f"{key}={value}")

# Print hostname
print("------")
print("Hostname:", socket.gethostname())

print("------")
print("Hello, World!")
print("------")
