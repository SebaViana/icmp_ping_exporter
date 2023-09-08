Copy code
import os
import time
import yaml
from prometheus_client import start_http_server, Gauge

# Initialize Prometheus metrics
ping_latency = Gauge('ping_latency_ms', 'Ping latency in milliseconds', ['host'])

def ping_host(host):
    try:
        # Run the ping command and capture the output
        ping_output = os.popen(f"ping -c 1 {host}").read()
        
        # Parse the output to extract the round-trip time (RTT) in milliseconds
        lines = ping_output.split('\n')
        for line in lines:
            if 'time=' in line:
                start = line.find('time=') + 5
                end = line.find(' ms', start)
                if start != -1 and end != -1:
                    rtt = float(line[start:end])
                    return rtt
        return None  # Return None if no valid RTT is found in the output
    except Exception as e:
        return None

def read_config(config_file):
    try:
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        print(f"Config file '{config_file}' not found.")
        return {}

def main():
    config_file = "default.yml"
    custom_config_file = "custom.yml"

    # Read the default configuration
    config = read_config(config_file)

    # Check for a custom configuration file
    if os.path.exists(custom_config_file):
        custom_config = read_config(custom_config_file)
        config.update(custom_config)

    host = config['host']
    ping_interval = config['ping_interval']

    # Read the HTTP server port from an environment variable or use 8080 as the default
    http_port = int(os.environ.get('HTTP_PORT', 8080))

    # Start the Prometheus HTTP server on the specified port
    start_http_server(http_port)

    while True:
        response_time = ping_host(host)
        if response_time is not None:
            ping_latency.labels(host=host).set(response_time)  # Set the actual response time
        else:
            ping_latency.labels(host=host).set(0)  # Set 0 for failed ping
        time.sleep(ping_interval)

if __name__ == "__main__":
    main()
