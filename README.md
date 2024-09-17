# Django - Port Liberator 

Django checks if a specific port on your Windows machine is in use, identifies the process using that port, and allows you to terminate the process if needed. It automates common `netstat` and `tasklist` commands to make it easier to manage port-related issues.

## Features

- Prompts the user to enter a port number.
- Identifies the process ID (PID) using the specified port.
- Displays the process details (name and PID).
- Optionally terminates the process that is using the port.

## Prerequisites

- This script is designed to run on **Windows**.
- You need to have **Python 3** installed on your system.
- The script uses the Windows commands `netstat` and `tasklist`, so it must be run with appropriate permissions (e.g., Command Prompt with administrator privileges).

## How to Use

1. **Clone or Download** this repository:

   ```bash
   git clone https://costargroup@dev.azure.com/costargroup/Apartments/_git/django-port-checker-process-killer

2. **Navigate to the directory** where the script is located:

    ```bash
    cd <path_to_script>

3. **Run the script** using Python:

    ```bash
    python django.py

4. **Follow the on-screen instructions**:
    - Enter the port number that you want to check when prompted.
    - The script will display the process ID (PID) using that port, if found.
    - The script will also display details about the process.
    - You will be asked if you want to terminate the process. Type y to terminate or n to skip.

## Example Usage

    Enter the port number to check: 4201
    Finding the process using port 4201...
    Process found using port 4201:
    TCP    0.0.0.0:4201         0.0.0.0:0            LISTENING       1234
    Process details for PID 1234:
    Image Name                     PID Session Name        Session#    Mem Usage
    ========================= ======== ================ =========== ============
    MyApp.exe                      1234 Console                    1    10,000 K
    Do you want to terminate the process with PID 1234? (y/n): y
    Process with PID 1234 has been terminated.


## Notes
- **Administrator Permissions**: To use this script effectively, you may need to run the command prompt as an administrator since terminating processes and checking port usage may require elevated privileges.
- **Modifying Port Numbers**: If you do not wish to terminate a process, you can change your application to use a different port instead of the blocked port.

## License
This script is open-source and free to use. Feel free to modify it to fit your needs.

## Support
If you encounter any issues or have any questions, feel free to reach out by emailing achandra@costar.com.