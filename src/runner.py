
from config import Config
from measurements.traceroute import TraceRoute

FUNCTIONS = {
    "traceroute": TraceRoute()
}

if __name__ == "__main__":
    print("===Executing all measurements===")

    functions = Config.MEASUREMENTS.split(",")
    for function in functions:
        if function == "all":
            for f in FUNCTIONS:
                FUNCTIONS[f].run_measurement()
            break
        elif function == "":
            raise Exception("No measurement defined!!")
        else:
            FUNCTIONS[function].run_measurement()
