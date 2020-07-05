import docker
from ..utilities.constants import GCP,AWS,AZURE

class DockerApi:
	def connect_client(self):
		self.client = docker.from_env()
	
	def build_image(self, image_name, tag_name):
		if tag_name:
			self.tag_name = tag_name
		self.image_name = image_name
		
	def build_image_and_push_to_registry(self, image_name, tag_name, cloud_name, bucket_name):
		if tag_name:
			self.tag_name = tag_name
		else:
			self.tag_name = None	
		self.image_name = image_name
		self.bucket_name = bucket_name
		if cloud_name == 