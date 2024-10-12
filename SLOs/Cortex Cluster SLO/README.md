# Cortex Latency SLO

This README describes a Service Level Objective (SLO) query for monitoring the response latency of a Cortex cluster.

## Overview

This latency SLO measures the percentage of responses that fall within a specified latency threshold over a given time period. It's designed to help monitor and maintain the performance of a Cortex cluster, ensuring that a high percentage of requests are processed within an acceptable time frame.

## SLO Query

Check cortex_latency_SLO.yml for the query

## Query Explanation

1. The query calculates the percentage of responses that were faster than 190.73 ms over the last hour.
2. It does this by comparing the count of responses within the threshold to the total number of responses.
3. The result is a percentage value representing how well the system is meeting the latency target.

## Usage

1. This query is intended to be used with a Prometheus-compatible monitoring system that scrapes metrics from your Cortex cluster.
2. You can set up an alert based on this SLO, for example, triggering if the percentage falls below a certain level (e.g., 99.9%).
3. Regularly review this SLO to ensure your Cortex cluster is meeting performance expectations.

## Customization

- Adjust the `threshold_ms` value to change the latency threshold as needed for your specific use case.
- Modify the `cluster` label to match your environment (e.g., "prod", "staging", etc.).
- Change the time range `[1h]` if you want to measure over a different period.

## Metrics Required

Ensure your Cortex cluster is exporting the following metrics:

1. `cortex_response_speed_within_threshold`: A histogram metric tracking responses within various latency buckets.
2. `cortex_total_response_count`: A counter of total responses.

## Best Practices

1. Set realistic thresholds based on your system's capabilities and user expectations.
2. Monitor this SLO alongside other performance metrics for a comprehensive view of system health.
3. Regularly review and adjust the SLO as your system evolves or requirements change.

## Troubleshooting

If the SLO percentage drops:
1. Check for any recent changes or deployments.
2. Investigate system resources (CPU, memory, network) for bottlenecks.
3. Analyze logs for any error patterns or slow queries.

Remember, this SLO is a high-level indicator. Always correlate with other metrics and logs for a complete understanding of system performance.