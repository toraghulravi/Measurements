class Config:
    # Functionalities - comma separated
    # Possible functions: traceroute
    MEASUREMENTS: str = "all"

    # Traceroute Parameters
    TRACEROUTE_PARAMS: dict = {
        "target": "google.com", 
        "af": 4,
        "response_timeout": 4000,
        "protocol": "UDP-Paris",
        "resolve_on_probe": "false", # we don't have this right now!
        "packets": 3,
        "size": 48, # not so important, Size of the packet
        "first_hop": 1, # Start measuring the traceroute at this hop.
        "max_hops": 32, # Stop measuring the traceroute at this hop.
        "paris": 16, # Number of different variations for paris traceroute. Set 0 for standard traceroute.
        "dont_fragment": True
    }
