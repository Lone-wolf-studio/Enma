class AirflowConfigNotFound(Exception):
    def __init__(self, error_message):
        if error_message:
            self.error_message = error_message
        else:
            self.error_message = None


    def __str__(self):
        if self.error_message:
            return '{0}'.format(self.error_message)
        else:
            return 'AirflowConfigNotFound Occured'
