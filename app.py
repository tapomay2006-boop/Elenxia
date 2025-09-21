from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def index():
    """Renders the main page of the website."""
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)