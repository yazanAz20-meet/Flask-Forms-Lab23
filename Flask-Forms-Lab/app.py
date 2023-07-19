from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


users={"guy":"111","said":"222", "yazan":"333"}
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]


@app.route('/', methods=['GET','POST'])  # '/' for the default page
def login():
		if request.method == 'GET':
			return render_template('login.html')

		else:
			if request.form['username'].lower() in users.keys()  and request.form['password'] in users.values():
				return redirect(url_for('home'))

@app.route('/home')
def home():
	return render_template('home.html', friends = facebook_friends)



@app.route('/friend_exists/<string:fr_exists>' ,methods=['GET','POST'])
def friend_exists(fr_exists):
	check = False
	if fr_exists in facebook_friends:
		check = True
	return render_template('friend_exists.html', fr = friend_exists, ch = check )





if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
