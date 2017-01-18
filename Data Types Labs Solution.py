Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
def data_type(a):
	"""Takes one input and returns a value in respect to data type of the input  """
	a_type =type(a)
	if a_type == str:
		return len(a)
	elif a_type ==bool:
		return a
	elif a_type ==int:
		if a == 100:
			return 'equal to 100'
		elif a < 100:
			return 'less than 100'

		else:
			return 'more than 100'

	elif a_type ==list:
		try:
			if a[2]:
				return a[2]
		except(IndexError):
			return None
	else:
		return 'no value'
