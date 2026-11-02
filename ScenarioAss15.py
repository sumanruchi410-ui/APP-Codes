import gc
import time

class Demo:
    def __init__(self, name):
        self.name = name
        self.ref = None

# Check garbage collection status
print("Garbage Collection Enabled:", gc.isenabled())

# Create objects
a = Demo("Object 1")
b = Demo("Object 2")

# Create circular reference
a.ref = b
b.ref = a

# Delete references
del a
del b

print("Garbage before collection:", gc.garbage)

# Measure automatic garbage collection
start = time.time()
gc.collect()
end = time.time()

print("Garbage Collection Completed")
print("Time taken:", end - start)

# Disable automatic garbage collection
gc.disable()
print("Automatic Garbage Collection Disabled")

# Enable automatic garbage collection
gc.enable()
print("Automatic Garbage Collection Enabled")

print("Garbage Collection Statistics:", gc.get_stats())

