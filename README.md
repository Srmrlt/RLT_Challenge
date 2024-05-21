# Salary Aggregation Bot

## Test Task for Python Developer Position

### Task Description
You are tasked with developing an algorithm to aggregate statistical salary data for company employees over specified time intervals. The goal is to calculate the total payments from a start date to an end date, with the data grouped by a specified period (hour, day, month). The collection of statistical data to be used is provided in the link at the end of this document.

### Requirements
- **Programming Language**: Python 3
- **Libraries**: asyncio, aiogram, motor(for asynchronous MongoDB)
- **Docker**: For containerization and deployment

### Example Task Description
The task can be summarized as: "Calculate the sum of all payments from {2022-02-28} to {2022-03-31}, grouped by {day}."

### Input
Your algorithm should accept the following inputs:
- Start date and time for aggregation in ISO format (`dt_from`)
- End date and time for aggregation in ISO format (`dt_upto`)
- Type of aggregation (`group_type`), which can be one of: `hour`, `day`, `month`

#### Example Input:
```json
{
  "dt_from": "2022-09-01T00:00:00",
  "dt_upto": "2022-12-31T23:59:00",
  "group_type": "month"
}
```

#### Output
Your algorithm should produce an output containing:
- An aggregated array of data (`dataset`)
- Labels for the values in the aggregated array in ISO format (`labels`)

#### Example Output:
```json
{
  "dataset": [5906586, 5515874, 5889803, 6092634],
  "labels": ["2022-09-01T00:00:00", "2022-10-01T00:00:00", "2022-11-01T00:00:00", "2022-12-01T00:00:00"]
}
```
