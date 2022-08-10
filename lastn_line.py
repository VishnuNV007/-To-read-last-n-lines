a_file = open ("nline.txt", "r")
lines= a_file.readline()
last_lines= lines[-5:]
print (last_lines)
a_file.close()