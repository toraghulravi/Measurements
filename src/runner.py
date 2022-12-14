
from config import Config
from measurements.traceroute import TraceRoute
from measurements.ping import Ping

FUNCTIONS = {
    "traceroute": TraceRoute(),
    "ping": Ping()
}

if __name__ == "__main__":
    functions = Config.MEASUREMENTS.split(",")
    for function in functions:
        if function == "all":
            for f in FUNCTIONS:
                print(f"*** Executing {FUNCTIONS[f].name} *****")
                FUNCTIONS[f].run_measurement()
            break
        elif function == "":
            raise Exception("No measurement defined!!")
        else:
            print(f"*** Executing {FUNCTIONS[function].name} *****")
            FUNCTIONS[function].run_measurement()
