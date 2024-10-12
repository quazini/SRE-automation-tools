# Using Cortex Latency SLO in Grafana Dashboard

This document explains how to incorporate the Cortex Latency SLO into a Grafana dashboard for effective monitoring and visualization.

## Prerequisites

- Access to a Grafana instance
- Prometheus data source configured in Grafana
- Access to the Cortex metrics in Prometheus

## Steps to Create the Dashboard

1. **Create a New Dashboard**
   - Log into Grafana
   - Click on the "+" icon in the left sidebar
   - Select "Dashboard"

2. **Add a New Panel**
   - Click "Add new panel"
   - Select "Graph" as the visualization type

3. **Configure the Panel Query**
   - In the Query tab, select your Prometheus data source
   - Paste the following PromQL query into the query field:

     ```
     sum(
       increase(
         cortex_response_speed_within_threshold{
           cluster="prod",
           threshold_ms="190.73486328125"
         }[1h]
       )
     ) * 100 / 
     sum(
       increase(
         cortex_total_response_count{
           cluster="prod"
         }[1h]
       )
     )
     ```

4. **Set Panel Display Options**
   - In the "Panel" tab:
     - Set the title to "Cortex Latency SLO"
     - Set the description to "Percentage of responses within 190.73ms threshold"
   - In the "Visualization" tab:
     - Set the Y-axis min to 0 and max to 100
     - Enable "Percentage" unit in the "Standard options"

5. **Configure Thresholds**
   - In the "Threshold" section of the "Visualization" tab:
     - Add a threshold at 99.9 with yellow color (warning)
     - Add a threshold at 99.5 with red color (critical)

6. **Add Annotations**
   - In the dashboard settings, add annotations for important events (e.g., deployments, config changes) to correlate with SLO changes

7. **Create Alert**
   - In the "Alert" tab of the panel:
     - Set condition: "WHEN last() OF query(A,5m,now) IS BELOW 99.5"
     - Set notification channel as per your setup

## Dashboard Layout Suggestions

- Place this SLO panel at the top of your Cortex monitoring dashboard
- Add complementary panels below:
  - Request rate
  - Error rate
  - 95th and 99th percentile latencies
  - Resource utilization (CPU, Memory, Disk I/O)

## Best Practices

1. **Regular Review**: Schedule monthly reviews of the SLO performance and adjust thresholds if necessary.
2. **Alerting**: Ensure that alerts based on this SLO are actionable and directed to the appropriate team.
3. **Documentation**: Keep this documentation updated with any changes to the query or dashboard setup.
4. **Correlation**: Use Grafana's built-in tools to correlate this SLO with other metrics for comprehensive analysis.

## Troubleshooting

If the SLO graph shows unexpected drops:
1. Check for any correlating spikes in error rates or resource utilization
2. Review recent changes or deployments
3. Investigate logs for any anomalies during the affected time period

Remember to adapt this dashboard and documentation to your specific Cortex setup and organizational needs.