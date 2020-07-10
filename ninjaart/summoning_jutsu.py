from exceptions.generic.generic_exceptions import CloudNameError
from utilities.constants import (GCP,
	                             AWS,
	                             AZURE)
from utilities.prerequisites_checker import CheckPrerequisites
from ninjaart.base import EnmaBase 

class Enma(EnmaBase):
	def __init__(self, cloud_name):
		self.cloud_name = cloud_name
		if self.cloud_name != GCP and AWS and AZURE:
			raise CloudNameError("Unknown cloud provider")
		self.check_installation(self.cloud_name)	
