def configure_settings():
    # Prompt user for SSH IP address
    ssh_ip = input("Enter the SSH IP address: ")

    # Start SSH server with user-provided IP
    start_ssh_server(ssh_ip)

