import time
import hashlib

if __name__=="__main__":
	start=time.time()
	message="Oye hoye, ki hoya toya moya foya"
	result=hashlib.md5(message)
	print("Message obtained : ",result.digest())
	print("Time taken :",(time.time()-start)*pow(10,3),"milliseconds")	

"""
OUTPUT:

student@student-HP-280-G2-MT:~/Desktop$ cd sid/
student@student-HP-280-G2-MT:~/Desktop/sid$ python md5.py 
('Message obtained : ', 's\x18\xf5j?\xb6\xe7K(\xd2\xb0\x07\x15\xbb\x80\x89')
('Time taken :', 0.050067901611328125, 'milliseconds')
"""
