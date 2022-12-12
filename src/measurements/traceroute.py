import dns.resolver
from typing import Optional

from src.measurement import Measurement
from src.config import Config
from src.utils import Utils

class TraceRoute(Measurement):
    def __init__(self, name: Optional[str] = None) -> None:
        super().__init__(name)

    def run_measurement(self):
        params = Config.TRACEROUTE_PARAMS
        target = Utils.cleanup(params["target"])

        if target == "":
            raise Exception("Invalid HostName!!")

        if Utils.is_hostname(target):
            result = []
            if params["af"] == 4:
                result = dns.resolver.query(target, "A")
            elif params["af"] == 6:
                result = dns.resolver.query(target, "AAAA")
            else:
                raise Exception("Unable to resolve hostname!!!")

        if not result:
            raise Exception("No resolved IP addresses")

        ip_addr = result[0].to_text()
        result = Utils.run(["sudo", "scamper", "-i", ip_addr], timeout=60)


if __name__ == "__main__":
    a = TraceRoute(name="temp")
    a.run_measurement()
