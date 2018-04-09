"""
Units in context are phones with added phonemic context. 

For example, a diphone is a phone with a "left context" in that it is a /u/ vowel but as it sounds with a preceding /p/ for example.

Coarticulation is the variance in a phone's acoustic features due to the dynamics of the oral cavity. 

This simple Python script allows you to generate a sequence of these "units in context" from half phones to septphones (seven-context_phones).

Can be useful in work to do with Speech Synthesis database design, when guaging unit coverage in the database. 

"""
def unit(x, int):
	"""Takes a list of phones and an int referring to how many contexts"""
	unit_in_context = []
	for idx, phone in enumerate(x):
		if int == 5:
			if idx < len(x)-4:
				central_phone = x[idx+2]
				left_phone = x[idx+1]
				leftleft_phone = x[idx]
				right_phone = x[idx+3]
				rightright_phone = x[idx+4]

				quinphone = leftleft_phone +"_"+ left_phone +"_"+ central_phone +"_"+ right_phone + "_"+rightright_phone
				unit_in_context.append(quinphone)
		elif int == 7:
			if idx < len(x)-6:
				central_phone = x[idx+3]
				left_phone = x[idx+2]
				leftleft_phone = x[idx+1]
				leftleftleft_phone = x[idx]
				right_phone = x[idx+4]
				rightright_phone = x[idx+5]
				rightrightright_phone = x[idx+6]

				septphone = leftleftleft_phone +"_"+ leftleft_phone +"_"+ left_phone +"_"+ central_phone +"_"+ right_phone + "_"+rightright_phone +"_"+rightrightright_phone
				unit_in_context.append(septphone)
		elif int == 3:
			if idx < len(x)-2:
				central_phone = x[idx+1]
				left_phone = x[idx]
				right_phone = x[idx+2]

				unit_phone = left_phone +"_"+ central_phone +"_"+ right_phone
				unit_in_context.append(unit_phone)
		elif int == 2:
			if idx < len(x)-1:
				central_phone = x[idx+1]
				left_phone = x[idx]

				unit_phone = left_phone +"_"+ central_phone
				unit_in_context.append(unit_phone)
		elif int == 0.5:
			if idx < len(x)-1:
				central_halfphone = x[idx]
				left_halfphone = x[idx]
				unit_phone = left_halfphone +"_"+ central_halfphone
				unit_in_context.append(unit_phone)
				central_halfphone = x[idx+1]
				left_halfphone = x[idx]
				unit_phone = left_halfphone +"_"+ central_halfphone
				unit_in_context.append(unit_phone)
		else:
			pass
	return unit_in_context

def quinphone(x):
	""""return a list of phones as quinphones"""
	return unit(x,5)

def triphone(x):
	""" Return a list of phones as triphones"""
	return unit(x,3)

def diphone(x):
	"""Return a list of phones as diphones"""
	return unit(x,2)

def septphone(x):
	"""Return a list of phones as septphones"""
	return unit(x,7)

def sevenphone(x):
	"""Return a list of phones as sevenphones"""
	return unit(x,7)

def halfphone(x):
	"""Return a list of phones as halfphones"""
	return unit(x,0.5)
