import os, sys

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('design.ui')

print(f"{form = }")
print(f"{base_path = }")
print(f"{__file__ = }")
