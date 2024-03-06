import base64
import os, sys


#encode .txt file joylashuvi
joylashuv_txt = '/storage/emulated/0/image_encoder/py_to_py.txt'
#decode .jpg file joylashuvi
joylashuv_jpg = '/storage/emulated/0/image_encoder/py_to_py.jpg'
# .jpg hamda .txt fileni delete qilish uchun
file_for_delete = "test.py"
# rasm nomi: exemple.jpg
image_name = "janob.jpg"
# text file .txt file nomi
txt_name = "darknet.txt"

py_to_py = input("""
image encode 

1) encode
2) decode
3) delete 
: """)

#decode

if py_to_py=="2":  
	file = open(joylashuv_txt, 'rb')
	byte = file.read()
	file.close()
	print("shifrdan chiqarildi")
	decodeit = open(image_name, 'wb')
	decodeit.write(base64.b64decode((byte)))
	decodeit.close()
	
# encode	

elif py_to_py == "1":	
	with open(joylashuv_jpg, "rb") as image2string:
		
		converted_string = base64.b64encode(image2string.read())
		print("shifrlandi")
			  
	with open(txt_name, "wb") as file:
	    file.write(converted_string)
	    
# delete

elif py_to_py == "3":
	os.system("rm -rf "+ file_for_delete)
	print("file ochirildi")
else:
	print("hato(")
