import sys

if len(sys.argv) != 2:
        print("[*] Run:\n\tjump_address.py <jump_point_address>")
        sys.exit(1)

address = sys.argv[1]

n1 = address[0:2]
n2 = address[2:4]
n3 = address[4:6]
n4 = address[6:8]
 
print("\nretn =  " + "\\x" + n4 + "\\x" + n3 +"\\x" + n2 +"\\x" + n1)

