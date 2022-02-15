import paramiko
paramiko.util.log_to_file("paramiko.log")

# Open a transport
# 변수를 선언해주고 초기 설정을 합니다.
host = "192.168.1.39" # example,실제 접속할 주소를 입력하세요
port = 22 # 그냥 22넣어주면 됩니다.
transprot = paramiko.transport.Transport(host,port)
userId = "ngcc"  # example
password = '2020ngcc' # example

# 연결
transprot.connect(username = userId, password = password)
sftp = paramiko.SFTPClient.from_transport(transprot)

# Go!
sftp = paramiko.SFTPClient.from_transport(transport)

# Upload
filepath = "C:\test\2022-2_NGCC.txt"
localpath = "C:\test\2022-2_NGCC.txt"
sftp.put(localpath,filepath)



