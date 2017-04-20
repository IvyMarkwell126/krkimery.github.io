from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.

URLs that will call the index() function if running app.py on localhost:
	http://localhost:5000/
	http://localhost:5000/index
'''
@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
	return render_template('index.html') # located in templates/
	
@app.route('/hero')
def hero():
	return render_template('hero.html')
	
@app.route('/villain')
def villain():
	return render_template('villain.html')
	
@app.route('/organization')
def organization():
	return render_template('organization.html')
	
@app.route('/about')
def about():
	dict = {'num_commits' : '129', 'num_issues' : '56'}
	return render_template('about.html', strings = dict)	

@app.route('/spiderprofile')
def spiderprofile():
	return render_template('spiderprofile.html')
	
@app.route('/flashprofile')
def flashprofile():
	return render_template('flashprofile.html')
	
@app.route('/captmericaprofile')
def captmericaprofile():
	return render_template('captmericaprofile.html')
	
@app.route('/phoenixprofile')
def phoenixprofile():
	return render_template('phoenixprofile.html')
	
@app.route('/ironmanprofile')
def ironmanprofile():
	return render_template('ironmanprofile.html')
	
@app.route('/supermanprofile')
def supermanprofile():
	return render_template('supermanprofile.html')
	
@app.route('/poisonivyprofile')
def poisonivyprofile():
	return render_template('poisonivyprofile.html')
	
@app.route('/lexlutherprofile')
def lexlutherprofile():
	return render_template('lexlutherprofile.html')
	
@app.route('/darkseidprofile')
def darkseidprofile():
	return render_template('darkseidprofile.html')
	
@app.route('/magnetoprofile')
def magnetoprofile():
	return render_template('magnetoprofile.html')
	
@app.route('/catwomanprofile')
def catwomanprofile():
	return render_template('catwomanprofile.html')
	
@app.route('/venomprofile')
def venomprofile():
	return render_template('venomprofile.html')
	
@app.route('/twofaceprofile')
def twofaceprofile():
	return render_template('twofaceprofile.html')
	
@app.route('/kingpinprofile')
def kingpinprofile():
	return render_template('kingpinprofile.html')
	
@app.route('/justiceleagueprofile')
def justiceleagueprofile():
	return render_template('justiceleagueprofile.html')
	
@app.route('/avengersprofile')
def avengersprofile():
	return render_template('avengersprofile.html')
	
@app.route('/xmenprofile')
def xmenprofile():
	return render_template('xmenprofile.html')
	
@app.route('/leagueofshadowsprofile')
def leagueofshadowsprofile():
	return render_template('leagueofshadowsprofile.html')
	
@app.route('/teentitansprofile')
def teentitansprofile():
	return render_template('teentitansprofile.html')
	
@app.route('/evilprofile')
def evilprofile():
	return render_template('evilprofile.html')
	
if __name__ == '__main__':
	app.run() # Run application