import paramiko
from time import sleep
paramiko.util.log_to_file("paramiko.log")

# Open a transport
host,port = "mathiaswskoglund.com",443
transport = paramiko.Transport((host,port))

# Auth
username,password = "foo","pass"
transport.connect(None,username,password)

# Go!
sftp = paramiko.SFTPClient.from_transport(transport)

# Upload
filepath = "/upload/website/info.txt"
localpath = "info.txt"


a = 0
while True:
	File_object = open("info.txt", "w+")
	File_object.write(str(a) + '\n')
	File_object.close()
	print("Written")
	a = a + 1

	sftp.put(localpath, filepath)
	print("written2")
	sleep(1)


# Close
if sftp: sftp.close()
if transport: transport.close()