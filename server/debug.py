import ipdb
from models import db, Game
from faker import Faker
from flask import Flask
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/debug')
def debug():
    fake = Faker()
    with app.app_context():
       game=Game.query.first()
       ipdb.set_trace()
       game_dict=game.to_dict()
       return str(game_dict)
if __name__=='__main__':
    app.run(debug=True)

