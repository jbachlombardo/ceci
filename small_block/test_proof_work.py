import hashlib as h
import numpy as np

def proof_of_work(old_param = np.random.randint(0, 10)) :
	new_param = 0
	valid_params = False
	while valid_params is False :
		guess = (str(old_param) + str(new_param)).encode()
		hexdigest = h.sha256(guess).hexdigest()
		print (hexdigest)
		if hexdigest[:2] == '00' :
			valid_params = True
		new_param += 1
	return old_param, new_param

a, b = proof_of_work()

print (a, b)
