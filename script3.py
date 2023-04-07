acl= int(input("¿Cual es el numero de ACL IPV4?\n"))
if acl >= 1 and acl <= 99:
	print("ACL IPv4 estandar")
elif acl >= 100 and acl <= 199:
	print("ACL IPv4 extendida")
else:
	print("Esta ACL IPv4 no es extendida o estandar.")