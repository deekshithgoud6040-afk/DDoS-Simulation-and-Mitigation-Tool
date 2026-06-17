print("DDoS Simulation and Mitigation Tool")
print()

max_requests = 10
request_count = 0

for i in range(1, 51):
    request_count += 1
    print("Request received:", request_count)

    if request_count > max_requests:
        print("System overload detected")
        print("Activating mitigation: Rate limiting applied")
        break

print()
print("Simulation completed")
print("In real systems, firewalls and rate limiting are used to prevent DDoS attacks")