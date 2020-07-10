from utilities.constants import GCP,AWS,AZURE
from commands.cli_commands import CommandsParser 
from utilities.commands_executor import ShellCommandExecutor
from utilities.constants import INSTALLATION_CHECKER 

class CheckPrerequisites:
	def check_installation(self, cloud_name):
		import pdb; pdb.set_trace()
		command = CommandsParser.get_commands(INSTALLATION_CHECKER, cloud_name=cloud_name)
		installed = ShellCommandExecutor.execute_shell_command(command)
		if installed[1] == None:
			print("{0} sdk not installed".format(self.cloud_name))
		else:
			if self.cloud_name == GCP:
				return str(installed).split('\\')[0].split('b')[1]       	
						

