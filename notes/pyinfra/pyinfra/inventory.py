def get_servers():
    server_list = [
        {"name": "dxblug-pyinfra", "ip": "10.1.10.111"},
    ]
    servers = []
    for vm in server_list:
        host_data = {
            "ssh_user": "root",
            "ssh_hostname": vm["ip"],
            "name": vm["name"],
            "_sudo": False,
        }
        v = ("@ssh/{}-{}".format(vm["name"], vm["ip"]), host_data)
        servers.append(v)
    return servers


hosts = get_servers()
