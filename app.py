from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Movie model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(200), nullable=False)
    movie_year = db.Column(db.Integer, nullable=False)
    movie_url = db.Column(db.String(500), nullable=False)
    movie_genre = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    movies = Movie.query.all()
    print(movies)
print(movies)
# Route to display and add movies
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        movie_url = request.form.get('movie_url')
        genre = request.form.get('genre')

        print(f"Received data: {title}, {year}, {movie_url}, {genre}")  # Debug print

        if title and year and year.isdigit() and movie_url and genre:
            new_movie = Movie(movie_title=title, movie_year=int(year), movie_genre=genre, movie_url=movie_url)
            db.session.add(new_movie)
            db.session.commit()  # Ensure the commit happens
            print(f"Added: {new_movie.movie_title}")  # Debug confirmation
            return redirect(url_for('index'))
        else:
            print("Form data is invalid!")  # If form data is missing or incorrect

    movies = Movie.query.all()
    print(f"Movies in database: {movies}")  # Check what movies are in the database
    return render_template('index.html', movies=movies)

# Route to drop the database
@app.route('/drop', methods=['POST'])
def drop_database():
    with app.app_context():
        db.drop_all()
        db.create_all()  # Recreate empty tables
    return redirect(url_for('index'))

if __name__ == '__main__':

    app.run(debug=True)
