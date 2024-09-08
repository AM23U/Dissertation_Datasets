import pandas as pd
import numpy as np
import random
from faker import Faker

# Initialize Faker for generating random names and locations
fake = Faker('en_GB')

# Constants
NUM_DEVICES = 1000  # Example number of affected devices
NUM_SOFTWARES = 300  # Example number of software applications affected
NUM_IT_STAFF = 50  # Number of IT staff involved
NUM_RECOVERY_OPERATIONS = 200  # Number of recovery operations needed

# Generate Dataset for Hardware Replacement Costs
def generate_hardware_replacement_data():
    data = {
        'Device_ID': [f'Device_{i+1}' for i in range(NUM_DEVICES)],
        'Device_Type': random.choices(['Laptop', 'Desktop', 'Server', 'Network Device'], k=NUM_DEVICES),
        'Replacement_Cost': [round(random.uniform(500, 5000), 2) for _ in range(NUM_DEVICES)],
        'Labor_Cost': [round(random.uniform(50, 200), 2) for _ in range(NUM_DEVICES)],
        'Replacement_Time_Hours': [round(random.uniform(1, 8), 1) for _ in range(NUM_DEVICES)],
        'Location': [fake.city() for _ in range(NUM_DEVICES)]
    }
    return pd.DataFrame(data)

# Generate Dataset for Software Reinstallation Costs
def generate_software_reinstallation_data():
    data = {
        'Software_ID': [f'Software_{i+1}' for i in range(NUM_SOFTWARES)],
        'Software_Name': [fake.bs() for _ in range(NUM_SOFTWARES)],
        'License_Cost': [round(random.uniform(100, 2000), 2) for _ in range(NUM_SOFTWARES)],
        'Installation_Time_Hours': [round(random.uniform(0.5, 3), 1) for _ in range(NUM_SOFTWARES)],
        'Labor_Cost': [round(random.uniform(50, 150), 2) for _ in range(NUM_SOFTWARES)]
    }
    return pd.DataFrame(data)

# Generate Dataset for Data Recovery Costs
def generate_data_recovery_data():
    data = {
        'Operation_ID': [f'Recovery_{i+1}' for i in range(NUM_RECOVERY_OPERATIONS)],
        'Data_Type': random.choices(['Student Records', 'Research Data', 'Financial Data', 'Administrative Data'], k=NUM_RECOVERY_OPERATIONS),
        'Data_Volume_GB': [round(random.uniform(10, 1000), 1) for _ in range(NUM_RECOVERY_OPERATIONS)],
        'Recovery_Time_Hours': [round(random.uniform(1, 24), 1) for _ in range(NUM_RECOVERY_OPERATIONS)],
        'Labor_Cost': [round(random.uniform(100, 500), 2) for _ in range(NUM_RECOVERY_OPERATIONS)],
        'Tool_Cost': [round(random.uniform(50, 300), 2) for _ in range(NUM_RECOVERY_OPERATIONS)]
    }
    return pd.DataFrame(data)

# Generate Dataset for Security Measures
def generate_security_measures_data():
    data = {
        'Measure_ID': [f'Security_{i+1}' for i in range(10)],
        'Measure_Description': ['Install New Firewalls', 'Update Anti-virus Software', 'Upgrade Intrusion Detection Systems', 'Conduct Employee Training', 'Implement Multi-Factor Authentication', 'Set up New VPN', 'Patch Management', 'Log Monitoring Setup', 'Threat Intelligence Subscription', 'Penetration Testing'],
        'Implementation_Cost': [round(random.uniform(1000, 10000), 2) for _ in range(10)],
        'Ongoing_Maintenance_Cost_Per_Year': [round(random.uniform(500, 5000), 2) for _ in range(10)],
        'Training_Cost_Per_Employee': [round(random.uniform(100, 500), 2) for _ in range(10)],
        'Number_of_Employees_Trained': [random.randint(10, NUM_IT_STAFF) for _ in range(10)]
    }
    return pd.DataFrame(data)

# Generate all datasets
hardware_replacement_df = generate_hardware_replacement_data()
software_reinstallation_df = generate_software_reinstallation_data()
data_recovery_df = generate_data_recovery_data()
security_measures_df = generate_security_measures_data()

# Save to CSV files
hardware_replacement_df.to_csv('hardware_replacement_costs.csv', index=False)
software_reinstallation_df.to_csv('software_reinstallation_costs.csv', index=False)
data_recovery_df.to_csv('data_recovery_costs.csv', index=False)
security_measures_df.to_csv('security_measures_costs.csv', index=False)

print("Datasets generated and saved to CSV files.")
