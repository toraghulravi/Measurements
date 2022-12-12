import dns.resolver

from src.measurement import Measurement
from src.config import Config
from src.utils import Utils

class TraceRoute(Measurement):
    def __init__(self) -> None:
        super().__init__(name="traceroute")

    def run_measurement(self):
        params = Config.TRACEROUTE_PARAMS
        target = Utils.cleanup(params["target"])

        if target == "":
            raise Exception("Invalid HostName!!")

        if Utils.is_hostname(target):
            result = []
            if params["af"] == 4:
                result = dns.resolver.resolve(target, "A")
            elif params["af"] == 6:
                result = dns.resolver.resolve(target, "AAAA")
            else:
                raise Exception("Unable to resolve hostname!!!")

        if not result:
            raise Exception("No resolved IP addresses")

        ip_addr = result[0].to_text()
        cmd = " ".join(["trace", "-M", "-w", str(params["response_timeout"] // 1000), "-P", params["protocol"], "-f", str(params["first_hop"]), "-m", str(params["max_hops"])])
        result = Utils.run(["scamper", "-c", cmd, "-i", ip_addr], timeout=60)
