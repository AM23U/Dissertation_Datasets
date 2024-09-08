import pandas as pd
import random
import uuid
from faker import Faker

fake = Faker()

# Constants
NUM_ASSETS = 100  # Number of assets to generate

import uuid
import random
from faker import Faker

fake = Faker()

def generate_infrastructure_data(num_assets):
    infrastructure_data = []
    for _ in range(num_assets):
        asset_id = str(uuid.uuid4())
        asset_class = random.choice(["Application Server", "Control Server", "Data Gateway", "Data Historian", "Field I/O",
                                     "Human-Machine Interface (HMI)", "Intelligent Electronic Device (IED)", "Jump Host",
                                     "Programmable Logic Controller (PLC)", "Remote Terminal Unit (RTU)", "Router",
                                     "Safety Controller", "Virtual Private Network (VPN) Server", "Workstation"])

        ip_address = fake.ipv4()
        mac_address = fake.mac_address()
        operating_system = random.choice(["Windows Server", "Embedded Linux", "Windows 10", "IOS", "Linux", "Embedded RTOS"])
        
        # Assign OS Version based on Operating System
        if operating_system == "Windows Server":
            os_version = random.choice(["2019", "2016"])
        elif operating_system == "Windows 10":
            os_version = random.choice(["21H1", "20H2"])
        elif operating_system == "IOS":
            os_version = random.choice(["15.2", "14.4"])
        elif operating_system == "Linux":
            os_version = random.choice(["Ubuntu 20.04", "Ubuntu 18.04", "Debian 10", "CentOS 7"])
        elif operating_system == "Embedded Linux":
            os_version = random.choice(["4.19", "5.4", "3.10"])
        elif operating_system == "Embedded RTOS":
            os_version = random.choice(["3.5", "4.0", "4.1"])
        else:
            os_version = "Unknown"
        
        hostname = fake.hostname()
        location = fake.city()
        manufacturer = random.choice(["Dell", "HP", "Cisco", "IBM", "Siemens", "Schneider Electric", "GE", "Rockwell Automation", "Emerson", "Honeywell", "Fortinet"])
        
        # Assign Firmware Version based on Manufacturer
        if manufacturer in ["Siemens", "Schneider Electric", "Rockwell Automation", "Emerson", "Honeywell"]:
            firmware_version = random.choice(["v1.0", "v1.1", "v2.0", "v3.5"])
        else:
            firmware_version = fake.bothify(text="v#.#")
        
        services = random.choice(["Web Hosting", "Database", "Control Systems", "Protocol Translation", "Data Storage", "Sensor Data", "Operator Interface", "Protection and Control", "Remote Access", "Process Control", "Data Aggregation", "Routing", "Safety Control", "VPN", "User Interface"])
        ports = random.sample(range(20, 50000), 5)

        infrastructure_data.append({
            "Asset ID": asset_id,
            "Asset Class": asset_class,
            "Domain": "IT",
            "IP Address": ip_address,
            "MAC Address": mac_address,
            "Operating System": operating_system,
            "OS Version": os_version,
            "Hostname": hostname,
            "Location": location,
            "Manufacturer": manufacturer,
            "Firmware Version": firmware_version,
            "Services": services,
            "Ports": ', '.join(map(str, ports))
        })
    return infrastructure_data



# Generate random application data
def generate_application_data(infrastructure_data):
    application_data = []
    app_versions = {
        "Apache HTTP Server": "2.4.48",
        "Log4j": "2.14.1",
        "MySQL": "8.0.25",
        "SCADA System": "3.1.4",
        "Custom Gateway Software": "1.3.2",
        "Data Historian Software": "5.6.0",
        "Field I/O Firmware": "4.2.1",
        "HMI Software": "4.8.0",
        "IED Control Software": "2.1.7",
        "Remote Access Tools": "1.0.0",
        "PLC Control Logic": "1.5.3",
        "RTU Control Software": "6.3.1",
        "Router Firmware": "12.4",
        "Safety Control Software": "3.2.8",
        "OpenVPN": "2.5.1",
        "Engineering Software": "10.3.4"
    }
    print(app_versions["Custom Gateway Software"])
    for asset in infrastructure_data:
        asset_id = asset["Asset ID"]
        applications = random.choice(["Apache HTTP Server, Log4j, MySQL", "SCADA System, Log4j", "Custom Gateway Software, Log4j",
                                      "Data Historian Software, Log4j", "Field I/O Firmware", "HMI Software, Log4j", "IED Control Software",
                                      "Remote Access Tools, Log4j", "PLC Control Logic", "RTU Control Software, Log4j", "Router Firmware",
                                      "Safety Control Software", "OpenVPN, Log4j", "Engineering Software, Log4j"])
        app_versions_used = ', '.join([f"{app} {app_versions[app]}" for app in applications.split(', ')])
        programming_languages = random.choice(["Java, Python", "C#, Python", "C, Python", "Java, SQL", "C", "C#, VBScript", "Embedded C", "Python, PowerShell", "Ladder Logic", "Shell Script"])
        libraries = random.choice(["Log4j, Spring Framework", "Log4j, DNP3", "Log4j, Protocol Buffers", "Log4j, JDBC", "RTOS Libraries", ".NET Framework", "Embedded Libraries", "Paramiko", "Modbus Libraries", "IOS Libraries", "Safety Libraries", "OpenSSL", "Matplotlib"])
        extensions = random.choice(["mod_ssl, mod_rewrite", "N/A", "Protocol Buffers", "N/A", "RTOS Extensions", "N/A", "Embedded Extensions", "N/A"])

        application_data.append({
            "Asset ID": asset_id,
            "Applications": app_versions_used,
            "Programming Languages": programming_languages,
            "Libraries": libraries,
            "Extensions": extensions
        })
    return application_data

# Hardcoded CVE to TTP mappings
def generate_cve_ttp_mappings():
    cve_ttp_data = [
        {"CVE ID": "CVE-2021-44228", "CVE Description": "Apache Log4j2 Remote Code Execution", "TTP ID": "T1210", "TTP Description": "Exploitation of Remote Services", "Application": "Log4j", "Version": "2.14.1"},
        {"CVE ID": "CVE-2017-5638", "CVE Description": "Apache Struts2 Remote Code Execution", "TTP ID": "T1203", "TTP Description": "Exploitation for Client Execution", "Application": "Apache Struts2", "Version": "2.3.31"},
        {"CVE ID": "CVE-2018-7600", "CVE Description": "Drupal Remote Code Execution", "TTP ID": "T1190", "TTP Description": "Exploit Public-Facing Application", "Application": "Drupal", "Version": "7.x"},
        {"CVE ID": "CVE-2020-0601", "CVE Description": "Windows CryptoAPI Spoofing Vulnerability", "TTP ID": "T1071", "TTP Description": "Application Layer Protocol", "Application": "Windows", "Version": "10"},
        {"CVE ID": "CVE-2019-0708", "CVE Description": "BlueKeep Remote Desktop Services Remote Code Execution", "TTP ID": "T1071", "TTP Description": "Application Layer Protocol", "Application": "Remote Desktop Services", "Version": "2008"},
        {"CVE ID": "CVE-2021-26855", "CVE Description": "Microsoft Exchange Server Remote Code Execution", "TTP ID": "T1190", "TTP Description": "Exploit Public-Facing Application", "Application": "Microsoft Exchange", "Version": "2019"},
        {"CVE ID": "CVE-2017-0144", "CVE Description": "EternalBlue SMB Remote Code Execution", "TTP ID": "T1071", "TTP Description": "Application Layer Protocol", "Application": "SMB", "Version": "1.0"},
        {"CVE ID": "CVE-2014-0160", "CVE Description": "OpenSSL Heartbleed", "TTP ID": "T1071", "TTP Description": "Application Layer Protocol", "Application": "OpenSSL", "Version": "1.0.1"},
        {"CVE ID": "CVE-2015-4852", "CVE Description": "Oracle WebLogic Server Remote Code Execution", "TTP ID": "T1210", "TTP Description": "Exploitation of Remote Services", "Application": "Oracle WebLogic", "Version": "10.3.6.0"},
        {"CVE ID": "CVE-2020-0796", "CVE Description": "SMBGhost Remote Code Execution", "TTP ID": "T1071", "TTP Description": "Application Layer Protocol", "Application": "SMB", "Version": "3.0"}
    ]
    return cve_ttp_data

# Generate the datasets
infrastructure_data = generate_infrastructure_data(NUM_ASSETS)
application_data = generate_application_data(infrastructure_data)
cve_ttp_data = generate_cve_ttp_mappings()

# Create DataFrames for each table
df_infrastructure = pd.DataFrame(infrastructure_data)
df_applications = pd.DataFrame(application_data)
df_cve_ttp = pd.DataFrame(cve_ttp_data)

# Merge the infrastructure and application data
df_combined = pd.merge(df_infrastructure, df_applications, on="Asset ID")

# Save to CSV files
df_applications.head()
df_infrastructure.to_csv("large_university_infrastructure.csv", index=False)
df_applications.to_csv("large_university_applications.csv", index=False)