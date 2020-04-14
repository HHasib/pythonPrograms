
#need to use nested for loops

# 
# |""""""""""|
#  \::::::::/
#   \::::::/
#    \::::/
#     \::/
#      ||
#     /::\
#    /::::\
#   /::::::\
#  /::::::::\
# |""""""""""|



def hourglass():
	
	for i in range(2):
		
		if i==1:
			print("      ||")

		print("|","\""*10,"|")
		
		for n in range(4,0,-1):
			print(" "*n,"/",":"*(8-2*n),"\\")	
			


hourglass()

