class Config:
    # Functionalities - comma separated
    # Possible functions: traceroute
    MEASUREMENTS: str = "http"

    # Traceroute Parameters
    TRACEROUTE_PARAMS: dict = {
        "target": "google.com", 
        "af": 4,
        "response_timeout": 10000,
        "protocol": "UDP",
        "resolve_on_probe": "false", # we don't have this right now!
        "packets": 3,
        "size": 48, # not so important, Size of the packet
        "first_hop": 1, # Start measuring the traceroute at this hop.
        "max_hops": 32, # Stop measuring the traceroute at this hop.
        "paris": 16, # Number of different variations for paris traceroute. Set 0 for standard traceroute.
        "dont_fragment": True
    }

    # Ping Parameters
    PING_PARAMS: dict = {
        "target": "google.com",
        "af": 4,
        "packet_interval": 10,
        "resolve_on_probe": "false", # we don't have this right now!
        "packets": 3,
        "size": 48, # not so important, Size of the packet
    }

    # DNS Parameters
    DNS_PARAMS: dict = {
        "target": "google.com",
        "af": 4,
        "query_class": "IN",
        "query_type": "A",
        "use_macros": False, # we don't have this right now!
        "use_probe_resolver": False, # we don't have this right now!
        "resolve_on_probe": False, # we don't have this right now!
        "set_nsid_bit": False,
        "protocol": "UDP",
        "payload_size": 512,
        "retry": 0,
        "skip_dns_check": False, # we don't have this right now!
        "include_qbuf": False, # we don't have this right now!
        "include_abuf": False, # we don't have this right now!
        "prepend_probe_id": False, # we don't have this now!
        "set_rd_bit": True,
        "set_do_bit": True,
        "set_cd_bit": True,
        "timeout": 5000
    }

    # HTTP Paramaters
    HTTP_PARAMS: dict = {
        "target": "google.com",
        "af": 4,
        "path": "/",
        "resolve_on_probe": False, # we don't have this right now!
        "header_bytes": 0, # Add payload if needed. IGNORING FOR NOW!
        "method": "GET",
        "extended_timing": False,
        "port": 80,
        "version": "1.1",
        "more_extended_timing": False,
        "skip_dns_check": False,
        "query_string": {},
        "user_agent": None
    }
