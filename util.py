from subprocess import Popen, PIPE

def get_stderr():
	p = Popen(args, stdout=log_fps["trace"], stderr=PIPE)
	_, stderr = p.communicate()
	return stderr