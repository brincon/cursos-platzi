# pregunta por el sistema operativo
import sys
print(sys.path)

# para expresiones regulares
import re
text = "Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte es 3"
result = re.findall('[0-9]+', text)
print(result)

# tiempo
import time
#hora actual en formato de computadora
timestamp = time.time()
print(timestamp)

#Indica la hora local
local = time.localtime()
#Indica la hora local
result = time.asctime(local)
print(result)

# para listas
import collections
numbers = [1,1,2,1,2,1,4,5,3,3,2,1]
counter = collections.Counter(numbers)
print(counter)
