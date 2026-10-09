with open("sample.txt","w") as file:
    file.write("Learning Context Manager")


# Custom Context manager

class MyResource:
    def __enter__(self):
        print("Setup")
        return self

    def process(self):
        print("processing")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource closed")
        print("Exc Type",exc_type)
        print("Exc Value", exc_value)
        print("Traceback", traceback)
        return None


with MyResource() as resource:
    resource.process()
    raise ValueError("Error during resource processing")
