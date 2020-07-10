from cloud_services.docker_sdk.api import DockerApi
from utilities.prerequisites_checker import CheckPrerequisites

# Just a base class to inherit all the sub classes which will be inherited by Enma main class
class EnmaBase(DockerApi, CheckPrerequisites):
	def __init__(self):
		print ("Work in progress")
