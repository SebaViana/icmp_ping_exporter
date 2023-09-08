# icmp_ping_exporter
## Overview
The icmp_ping_exporter is a simple tool developed for monitoring the latency of a specific host by sending periodic ICMP requests. It exposes the ping latency as a metric in Prometheus format over HTTP.

## Exposed port
The application exposes Prometheus metrics over HTTP, and by default, it listens on port 8085.

## Volumes
You can configure the target host and ping interval by specifying the following parameters:

> host: Replace your_custom_host with the target host you want to monitor.
> ping_interval: Replace your_custom_ping_interval with the desired ping interval in seconds.

These parameters should be added to a mounted volume in the location /app/custom.yml.
