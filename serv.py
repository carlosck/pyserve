from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Algo server"

@app.route("/cli/")
def cli(): 
	proc = subprocess.Popen('ls',stdout=subprocess.PIPE)	
	tmp  = proc.stdout.read()
	return tmp

if __name__=="__main__":
	app.run()
