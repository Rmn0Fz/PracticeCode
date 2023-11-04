import paramiko

# Connect to the device
host_IP = input("Enter the IP address: ")
port = 22
username = input("Enter your username: ")
password = input("Password: ")

# Create an SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the device using SSH
    client.connect(host_IP, port, username, password)
    
    # Execute a command on the device 
    command = input("CMD => ") #Command you want to execute
    stdin, stdout, stderr = client.exec_command(command)
    
    # Read and print the command output
    output = stdout.read().decode()
    print(output)
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Close the SSH conection
    client.close()
    