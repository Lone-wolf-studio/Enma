import docker
from utilities.constants import GCP,AWS,AZURE

class DockerApi:
	def connect_client(self):
		self.client = docker.from_env()
	
	def build_image(self, image_name, tag_name):
		pass

	def build_image_and_push_to_registry(self, image_name, tag_name, cloud_name, bucket_name):
		pass