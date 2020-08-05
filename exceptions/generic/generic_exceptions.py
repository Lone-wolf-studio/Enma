# exception for unknown cloud name/ typo errors
class CloudNameError(Exception):
	def __init__(self, error_message=None):
		if error_message:
			self.error_message = error_message
		else:
			self.error_message = None

	def __str__(self):
		if self.error_message:
			return '{0}'.format(self.error_message)
		else:
			return 'CloudNameError Occurred'				

# exception for client sdk not installed
class ClientNotFound(Exception):
	def __init__(self, error_message=None):
		if error_message:
			self.error_message = error_message
		else:
			self.error_message = None

	def __str__(self):
		if self.error_message:
			return '{0}'.format(self.error_message)
		else:
			return 'ClientNotFound Occurred'
