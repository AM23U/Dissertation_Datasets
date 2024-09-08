import pandas as pd
import random
from datetime import datetime, timedelta

# Constants for dataset generation
NUM_DEPARTMENTS = 5
NUM_ROLES = 10
NUM_EMPLOYEES = 100
NUM_CONSULTANTS = 10
NUM_INCIDENT_RESPONSES = 50
NUM_SYSTEM_REMEDIATIONS = 50
NUM_COST_ENTRIES = 200

# Helper functions
def random_date(start_date, end_date):
    """Generate a random date between two dates."""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def random_cost():
    """Generate a random cost for cost entries."""
    return round(random.uniform(100, 10000), 2)

# Generate Departments DataFrame
departments_data = {
    'department_id': range(1, NUM_DEPARTMENTS + 1),
    'name': [f'Department {i}' for i in range(1, NUM_DEPARTMENTS + 1)],
    'head': [f'Head {i}' for i in range(1, NUM_DEPARTMENTS + 1)]
}
departments_df = pd.DataFrame(departments_data)

# Generate Roles DataFrame
roles_data = {
    'role_id': range(1, NUM_ROLES + 1),
    'role_name': [f'Role {i}' for i in range(1, NUM_ROLES + 1)],
    'description': [f'Description for Role {i}' for i in range(1, NUM_ROLES + 1)]
}
roles_df = pd.DataFrame(roles_data)

# Generate Employees DataFrame
employees_data = {
    'employee_id': range(1, NUM_EMPLOYEES + 1),
    'name': [f'Employee {i}' for i in range(1, NUM_EMPLOYEES + 1)],
    'department_id': [random.randint(1, NUM_DEPARTMENTS) for _ in range(NUM_EMPLOYEES)],
    'role_id': [random.randint(1, NUM_ROLES) for _ in range(NUM_EMPLOYEES)],
    'salary': [round(random.uniform(30000, 70000), 2) for _ in range(NUM_EMPLOYEES)],
    'hourly_rate': [round(random.uniform(15, 50), 2) for _ in range(NUM_EMPLOYEES)],
    'hire_date': [random_date(datetime(2010, 1, 1), datetime(2024, 1, 1)).date() for _ in range(NUM_EMPLOYEES)]
}
employees_df = pd.DataFrame(employees_data)

# Generate Consultants DataFrame
consultants_data = {
    'consultant_id': range(1, NUM_CONSULTANTS + 1),
    'name': [f'Consultant {i}' for i in range(1, NUM_CONSULTANTS + 1)],
    'rate_per_hour': [round(random.uniform(100, 500), 2) for _ in range(NUM_CONSULTANTS)],
    'expertise_area': [f'Expertise Area {i}' for i in range(1, NUM_CONSULTANTS + 1)]
}
consultants_df = pd.DataFrame(consultants_data)

# Generate Incident Response Costs DataFrame
incident_response_data = {
    'response_id': range(1, NUM_INCIDENT_RESPONSES + 1),
    'employee_id': [random.randint(1, NUM_EMPLOYEES) for _ in range(NUM_INCIDENT_RESPONSES)],
    'hours_worked': [round(random.uniform(5, 20), 2) for _ in range(NUM_INCIDENT_RESPONSES)],
    'overtime_hours': [round(random.uniform(0, 10), 2) for _ in range(NUM_INCIDENT_RESPONSES)],
    'total_cost': [random_cost() for _ in range(NUM_INCIDENT_RESPONSES)],
    'date_logged': [random_date(datetime(2020, 1, 1), datetime(2024, 1, 1)).date() for _ in range(NUM_INCIDENT_RESPONSES)]
}
incident_response_df = pd.DataFrame(incident_response_data)

# Generate System Remediation Costs DataFrame
system_remediation_data = {
    'remediation_id': range(1, NUM_SYSTEM_REMEDIATIONS + 1),
    'employee_id': [random.randint(1, NUM_EMPLOYEES) for _ in range(NUM_SYSTEM_REMEDIATIONS)],
    'hours_spent': [round(random.uniform(10, 50), 2) for _ in range(NUM_SYSTEM_REMEDIATIONS)],
    'task_description': [f'Remediation Task {i}' for i in range(1, NUM_SYSTEM_REMEDIATIONS + 1)],
    'total_cost': [random_cost() for _ in range(NUM_SYSTEM_REMEDIATIONS)],
    'date_logged': [random_date(datetime(2020, 1, 1), datetime(2024, 1, 1)).date() for _ in range(NUM_SYSTEM_REMEDIATIONS)]
}
system_remediation_df = pd.DataFrame(system_remediation_data)

# Generate Cost Types DataFrame
cost_types_data = {
    'cost_type_id': [1, 2, 3],
    'name': ['Salary', 'Overtime', 'Consulting Fees'],
    'description': ['Cost related to salary payments', 'Cost related to overtime payments', 'Cost related to consulting fees']
}
cost_types_df = pd.DataFrame(cost_types_data)

# Generate Cost Entries DataFrame
cost_entries_data = {
    'cost_entry_id': range(1, NUM_COST_ENTRIES + 1),
    'employee_id': [random.randint(1, NUM_EMPLOYEES) for _ in range(NUM_COST_ENTRIES)],
    'consultant_id': [random.choice([None, random.randint(1, NUM_CONSULTANTS)]) for _ in range(NUM_COST_ENTRIES)],
    'cost_type_id': [random.randint(1, 3) for _ in range(NUM_COST_ENTRIES)],
    'amount': [random_cost() for _ in range(NUM_COST_ENTRIES)],
    'description': [f'Cost Entry {i}' for i in range(1, NUM_COST_ENTRIES + 1)],
    'date_logged': [random_date(datetime(2020, 1, 1), datetime(2024, 1, 1)).date() for _ in range(NUM_COST_ENTRIES)]
}
cost_entries_df = pd.DataFrame(cost_entries_data)

# Export all DataFrames to CSV
departments_df.to_csv('Departments.csv', index=False)
roles_df.to_csv('Roles.csv', index=False)
employees_df.to_csv('Employees.csv', index=False)
consultants_df.to_csv('Consultants.csv', index=False)
incident_response_df.to_csv('Incident_Response_Costs.csv', index=False)
system_remediation_df.to_csv('System_Remediation_Costs.csv', index=False)
cost_types_df.to_csv('Cost_Types.csv', index=False)
cost_entries_df.to_csv('Cost_Entries.csv', index=False)

print("Datasets generated and exported to CSV files successfully!")
