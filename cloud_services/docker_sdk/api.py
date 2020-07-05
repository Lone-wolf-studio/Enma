import docker

class DockerApi:
	def connect_client(self):
		self.client = docker.from_env()
	
	def build_image(self, image_name, tag_name):
		if tag_name:
			self.tag_name = tag_name
		self.image_name = image_name
		
	def build_image_and_push_to_registry(self, image_name, tag_name, cloud_name):
		pass	