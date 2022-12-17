from src.measurement import Measurement
from src.config import Config
from src.utils import Utils

class DNS(Measurement):
    def __init__(self) -> None:
        super().__init__(name="dns")

    def run_measurement(self):
        params = Config.DNS_PARAMS
        target = Utils.cleanup(params["target"])

        if target == "":
            raise Exception("Invalid HostName!!")

        cmd = []
        if params["protocol"] == "TCP":
            cmd.append("+tcp")
        
        if params["set_nsid_bit"] is False:
            cmd.append("+nsid")
        
        if params["set_rd_bit"] is False:
            cmd.append("+recurse")
        
        if params["set_do_bit"] is False:
            cmd.append("+dnssec")
        
        if params["set_cd_bit"] is False:
            cmd.append("+cdflag")

        dig_commands = ["dig", target, "-c", params["query_class"], "-t", params["query_type"], f"-{params['af']}", f"+retry={params['retry']}", f"+time={params['timeout']}"] + cmd
        Utils.run(dig_commands, timeout=300)
