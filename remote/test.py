import os
import socket

# import something I don't have
import skyfield


# Print all environment variables
for key, value in os.environ.items():
    print(f"{key}={value}")

# Print hostname
print("------")
print("Hostname:", socket.gethostname())

print("------")
print("Hello, World!")
print("------")
