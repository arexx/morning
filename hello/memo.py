import datetime


MAX_AGE = datetime.timedelta(hours=1)

__memo = {}

class Entry(object):
	def __init__(self, value):
		self.value = value
		self.time = datetime.datetime.now()

	def expired(self):
		return datetime.datetime.now() - self.time > MAX_AGE

def memo(key, func):
	if key in __memo:
		entry = __memo[key]
		if not entry.expired():
			return entry.value

	# There was no entry or it was stale.
	value = func()
	__memo[key] = Entry(value)
	return value

def clear():
	__memo = {}