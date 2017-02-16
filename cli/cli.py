from flask import Flask
import subprocess
from git import Repo
from git import RemoteProgress

from var_dump import var_dump

app = Flask(__name__)

@app.route("/")
def hello():
	return "Algo server"

@app.route("/cli/")
def cli():  
	proc = subprocess.Popen(["git", "status"],stdout=subprocess.PIPE,cwd='/Users/Seca/Public/wworks/2016/FIAT/fca/VVV/www/mitsubishi/htdocs')   
	tmp  = proc.stdout.read()
	return tmp

@app.route("/pull/")
def pull():  
	proc = subprocess.Popen(["git", "pull","stage","develop"],stdout=subprocess.PIPE,cwd='/Users/Seca/Public/wworks/2016/FIAT/fca/VVV/www/mitsubishi/htdocs')   
	tmp  = proc.stdout.read()
	return tmp

@app.route("/git/push")
def gitPush():  	
	repo = Repo('/Users/Seca/Public/wworks/test/polemica/polemica/cmks/cms')	
	print("tres")
	try:		
		o = repo.remotes.heroku
		
		este= o.push()
		var_dump(list(este))
			#print("Updated %s to %s" % (fetch_info.ref, fetch_info.commit))		
	except:

		return "mal"	

	return "bien"

@app.route("/git/pull")
def git():  
	#repo = Repo('/Users/Seca/Public/wworks/2016/FIAT/fca/VVV/www/mitsubishi/htdocs')
	repo = Repo('/Users/Seca/Public/wworks/test/polemica/polemica/cmks/cms')
	#o = repo.remotes.origin
	#var_dump(list(repo.remotes))
	print("uno")
	var_dump(repo.remotes.heroku)
	var_dump(list(repo.refs))
	
	try:
		#o = repo.remotes.origin
		#o = repo.remotes.origin
		o = repo.remotes.heroku
		#var_dump(list(repo.remotes))
		for fetch_info in o.pull(repo.refs[0],progress=MyProgressPrinter()):
			print("Updated %s to %s" % (fetch_info.ref, fetch_info.commit))
		#tmp = o.pull()
	except:

		return "mal"
	
	#print(list(o))

	return "bien"


class MyProgressPrinter(RemoteProgress):
	def update(self, op_code, cur_count, max_count=None, message=''):
		print(op_code, cur_count, max_count, cur_count / (max_count or 100.0), message or "NO MESSAGE")

if __name__=="__main__":
	print("dos")
	app.run()
	#repo = Repo('/Users/Seca/Public/wworks/2016/FIAT/fca/VVV/www/mitsubishi/htdocs')
	#o = repo.remotes.stage
	#var_dump(repo.remotes.stage.refs.master)
	
	
	#proc = subprocess.Popen(["git", "status"],stdout=subprocess.PIPE,cwd='/Users/Seca/Public/wworks/2016/FIAT/fca/VVV/www/mitsubishi/htdocs')  

	
#proc = subprocess.Popen('cd ../../../../Public/wworks/2016/FIAT/fca/VVV/www/mitsubishi/htdocs',stdout=subprocess.PIPE) 