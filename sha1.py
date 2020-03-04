import time
import hashlib

if __name__=="__main__":
	start=time.time()
	message="Oye hoye, ki hoya toya moya foya"
	result=hashlib.sha256(message)
	print("Message obtained : ",result.digest())
	print("Time taken :",(time.time()-start)*pow(10,3),"milliseconds")	


"""
OUTPUT:

student@student-HP-280-G2-MT:~/Desktop/sid$ python sha1.py 
('Message obtained : ', 'm\x9e\xfe\xb0\x81\xddfK\xf8b\x82\xd4\xdd\xbb\xbc\x1d"2\xc9\xa5d\xa7i\xcf\xbfD\xf6\xc5S\xf0\x14\x07')
('Time taken :', 0.053882598876953125, 'milliseconds')


"""
