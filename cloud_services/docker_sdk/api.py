import docker
from utilities.constants import GCP,AWS,AZURE

class DockerApi:
	def connect_client(self):
		self.client = docker.from_env()
	
	def build_image(self, image_name, tag_name, **kwargs):
		self.image_name = image_name
		self.tag_name = tag_name
		self.build_args_dict = dict()
		for key, value in kwargs.items():
			self.build_args_dict[key] = value
		self.docker_image = self.client.images.build(path=docker_file_path,
			                               tag=self.image_name,
			                               buildargs=self.build_args_dict)
		return self.docker_image


	def build_image_and_push_to_registry(self, image_name, tag_name, cloud_name, bucket_name):
		pass
