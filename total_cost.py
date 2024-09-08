import pandas as pd

# Load CSV data
data_recovery_df = pd.read_csv('data_recovery_costs.csv')
incident_response_df = pd.read_csv('Incident_Response_Costs.csv')
hardware_replacement_df = pd.read_csv('hardware_replacement_costs.csv')
employees_df = pd.read_csv('Employees.csv')

# Calculate Data Recovery Costs
total_recovery_time = data_recovery_df['Recovery_Time_Hours'].sum()
average_labor_cost = data_recovery_df['Labor_Cost'].mean()
total_tool_cost = data_recovery_df['Tool_Cost'].sum()

data_recovery_total_cost = (total_recovery_time * average_labor_cost + total_tool_cost)

# Print Data Recovery Costs Details
print(f"Total Recovery Time (Hours): {total_recovery_time:.2f}")
print(f"Average Labor Cost per Hour: ${average_labor_cost:,.2f}")
print(f"Total Tool Cost: ${total_tool_cost:,.2f}")
print(f"Data Recovery Total Cost: ${data_recovery_total_cost:,.2f}")

# Calculate Incident Response Costs
incident_response_total_cost = incident_response_df['total_cost'].sum()
print(f"Incident Response Total Cost: ${incident_response_total_cost:,.2f}")

# Calculate Hardware Replacement Costs (if applicable)
total_replacement_cost = hardware_replacement_df['Replacement_Cost'].sum()
total_labor_cost = hardware_replacement_df['Labor_Cost'].sum()

hardware_replacement_total_cost = total_replacement_cost + total_labor_cost

# Print Hardware Replacement Costs Details
print(f"Total Replacement Cost: ${total_replacement_cost:,.2f}")
print(f"Total Labor Cost for Replacement: ${total_labor_cost:,.2f}")
print(f"Hardware Replacement Total Cost: ${hardware_replacement_total_cost:,.2f}")

# Calculate Employee Labor Costs for Incident
average_hourly_rate = employees_df['hourly_rate'].mean()
employee_labor_costs = average_hourly_rate * 48  # Assuming 48 hours of work

# Print Employee Labor Costs Details
print(f"Average Hourly Rate: ${average_hourly_rate:,.2f}")
print(f"Employee Labor Costs for Incident (48 hours): ${employee_labor_costs:,.2f}")

# Cyber Insurance Costs
cyber_insurance_costs = {
    'Breach Coach': 75000,
    'Forensics': 150000,
    'Crisis Management': 75000,
    'Notification': 73000,
    'Call Center': 50000,
    'Credit Monitoring': 69000,
    'Regulatory Fines & Defense': 420000,
    'Class Action Settlements & Defense': 1100000
}

# Print Cyber Insurance Costs
print("\nCyber Insurance Costs:")
for key, value in cyber_insurance_costs.items():
    print(f"{key}: ${value:,.2f}")

total_cyber_insurance_cost = sum(cyber_insurance_costs.values())
print(f"Total Cyber Insurance Cost: ${total_cyber_insurance_cost:,.2f}")

# Calculate Total Costs
total_cost = (
    data_recovery_total_cost 
    + incident_response_total_cost 
    + hardware_replacement_total_cost 
    + employee_labor_costs 
    + total_cyber_insurance_cost
)

print(f"\nTotal Estimated Cost for the Incident: ${total_cost:,.2f}")
