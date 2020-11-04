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
filepath_s = "/upload/website/sinfo.txt"
localpath_s = "sinfo.txt"
filePath_v = "/upload/website/vinfo.txt"
localpath_v = "vinfo.txt"


sftp.put(localpath_s, filepath_s)
sftp.put(localpath_v, filepath_v)
sleep(0.5)


# Close
if sftp: sftp.close()
if transport: transport.close()
