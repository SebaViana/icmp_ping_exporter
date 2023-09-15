# icmp_ping_exporter
## Overview
The icmp_ping_exporter is a simple tool developed for monitoring the latency of the specified hosts by sending periodic ICMP requests. It exposes the ping latency as a metric in Prometheus format over HTTP.

## Exposed port
The application exposes Prometheus metrics over HTTP, and by default, it listens on port 8085.

## Volumes
You can configure the target hosts and ping interval by specifying the following parameters:

https://github.com/SebaViana/icmp_ping_exporter/blob/519ceeb17b03d1c4ea44efaa2d230cbc7cec2d8d/default.yml#L1-L8

You can add as many hosts as you wish.
These parameters should be added to a mounted volume in the location /app/custom.yml.
