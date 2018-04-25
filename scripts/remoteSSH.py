from paramiko import SSHClient
client = SSHClient()
client.load_system_host_keys()
client.connect("hostname", username="user")
stdin, stdout, stderr = client.exec_command('program')
print "stderr: ", stderr.readlines()
print "pwd: ", stdout.readlines()