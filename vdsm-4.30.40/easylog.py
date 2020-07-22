
import os
import sys
import datetime
import glob

class easylog:

    	def __init__(self, info_file):
    	    	self.info_file = open(info_file, 'a+')

    	def info(self, text):
    	    	if self.info_file:
    	        	time_now = datetime.datetime.now()
    	        	self.info_file.write(time_now.strftime('%Y-%m-%d %H:%M:%S'))
    	        	self.info_file.write('-----')
    	        	self.info_file.write(text)
    	        	self.info_file.write('\n')

	def release(self):
		if self.info_file:
			self.info_file.close()


def get_file_size(file_path):
	file_size = os.path.getsize(file_path)
	file_size = file_size/float(1024 * 1024)
	return round(file_size, 2)

def repo_info_log():
	glob_file = '/tmp/vgpuinfo.*.log'
	repo_file = '/tmp/vgpuinfo.{}.log'
	move_cmd = 'mv /tmp/vgpuinfo.log {}'.format(repo_file)
	similar_list = glob.glob(glob_file)
	postfix = len(similar_list) + 1
	while 1:
		if os.path.exists(repo_file.format(postfix)):
			postfix += 1
		else:
			break
	os.system(move_cmd.format(postfix))

def repo_warn_log():
	glob_file = '/tmp/vgpuwarn.*.log'
	repo_file = '/tmp/vgpuwarn.{}.log'
	move_cmd = 'mv /tmp/vgpuwarn.log {}'.format(repo_file)
	similar_list = glob.glob(glob_file)
	postfix = len(similar_list) + 1
	while 1:
		if os.path.exists(repo_file.format(postfix)):
			postfix += 1
		else:
			break
	os.system(move_cmd.format(postfix))

def get_session():
	info_log_path = '/tmp/vgpuinfo.log'
	warn_log_path = '/tmp/vgpuwarn.log'
	if os.path.exists(info_log_path):
		info_log_size = get_file_size(info_log_path)
		if info_log_size > 20.0:
			repo_info_log()
	if os.path.exists(warn_log_path):
		warn_log_size = get_file_size(warn_log_path)
		if warn_log_size > 20.0:
			repo_warn_log()
	return easylog(info_log_path, warn_log_path)
	
def close_session(log_obj):
	if log_obj:
		log_obj.release()
