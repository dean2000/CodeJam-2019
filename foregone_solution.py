import math

def Two_Checks(num):
	upper = math.ceil(num-1)
	# lower = int(1)

	while ('4' in str(upper)) or ('4' in str(num-upper)):
		upper /= 2
		# lower += 1

	print(f"{upper} + {num-upper} : {num}")
	print("lenght is %d" % len(str(num)))
	print("lenght of 10^100 == %s" % len(str(10**100)))

Two_Checks(1264111111111111111111111111111112643564747656746553654754444444444444444444444444416758758757875875879587897575879)