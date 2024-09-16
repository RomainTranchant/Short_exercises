# Assign `system` to a specific operating system
# This variable represents which operating system is running

system = "OS 5"

# If OS 2 is running, then display a "no update needed" message
# Otherwise if OS 1 is running, display a "update needed" message
# Otherwise if OS 3 is running, display a "update needed" message
# Otherwise if OS 4 is running, display a "trial period" message

if system == "OS 2":
    print("no update needed")
elif system == "OS 1":
    print("update needed")
elif system == "OS 3":
    print("update needed")
elif system == "OS 4":
    print("trial period")
else:
    print("Error, OS not recognized")