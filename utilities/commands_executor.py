import subprocess

class ShellCommandExecutor:
	def execute_shell_command(self, command):
		self.command = command

		try:
			proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)  
			time.sleep(1) 
			(out, err) = proc.communicate() 
		except Exception as e:
			raise e   

		return str(out)


