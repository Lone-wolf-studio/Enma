from exceptions.generic.generic_exceptions import CloudNameError
from utilities.constants import (GCP,
	                             AWS,
	                             AZURE)

class Enma:
	def __init__(self, cloud_name):
		self.cloud_name = cloud_name
		if self.cloud_name != GCP and AWS and AZURE:
			raise CloudNameError("Unknown cloud provider")

	def create_bucket(bucket_name):
		self.bucket_name = bucket_name
		
	def create_instance(instance_name):
		self.instance_name = instance_name		