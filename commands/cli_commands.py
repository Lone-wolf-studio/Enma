from utilities.constants import INSTALLATION_CHECKER as check_installation
from utilities.constants import GCP, AWS, AZURE
from utilities.commands_executor import ShellCommandExecutor as se
from utilities.constants import (GCLOUD_SDK_CHECK, 
								 AWS_SDK_CHECK,
								 AZURE_SDK_CHECK)

class CommandsParser(object):
	
	def get_commands(self, command_type=None, cloud_name=None):
		self.cloud_name = cloud_name
		with open('commands.yml') as file:
			self.commands_dict = yaml.load(file, Loader=yaml.FullLoader)    
			if command_type == check_installation:
				if self.cloud_name == GCP:
					command = self.commands_dict[GCLOUD_SDK_CHECK]
				elif self.cloud_name == AWS:
					command = self.commands_dict[AWS_SDK_CHECK]
				elif self.cloud_name == AZURE:
					command = self.commands_dict[AZURE_SDK_CHECK]       
		
			