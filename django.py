import subprocess

def find_process_using_port(port):
    # Step 1: Identify the process using the port
    print(f"Finding the process using port {port}...")
    cmd = f"netstat -aon | findstr :{port}"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.stdout:
        print(f"Process found using port {port}:")
        print(result.stdout)
        # Extract the PID from the result (last column)
        pid = result.stdout.strip().split()[-1]
        return pid
    else:
        print(f"No process found using port {port}.")
        return None

def get_process_name(pid):
    # Step 2: Get the process name using the PID
    cmd = f"tasklist /fi \"pid eq {pid}\""
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.stdout:
        print(f"Process details for PID {pid}:")
        print(result.stdout)
    else:
        print(f"No process found with PID {pid}.")

def terminate_process(pid):
    # Step 3: Ask the user if they want to terminate the process
    terminate = input(f"Do you want to terminate the process with PID {pid}? (y/n): ").lower()

    if terminate == 'y':
        cmd = f"taskkill /F /PID {pid}"
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            print(f"Process with PID {pid} has been terminated.")
        else:
            print(f"Failed to terminate process with PID {pid}. Error: {result.stderr}")
    else:
        print("Process termination skipped.")

if __name__ == "__main__":
    port = input("Enter the port number to check: ")
    pid = find_process_using_port(port)
    
    if pid:
        get_process_name(pid)
        terminate_process(pid)
