from flask import Blueprint, request, jsonify

from app.models import db
from app.models.moods import Mood
from app.models.actions import Action
from ..config import Configuration
from ..auth import require_auth

bp = Blueprint("mood", __name__, url_prefix='/api/mood')

@bp.route('', methods=["POST"])
def create():
  data = request.json
  mood = Mood(user_id=data['currentUserId'], level=data['level'],
              title=data['title'], content=data['content'])
  db.session.add(mood)
  
  for action in data['actions']:
    action = Action(act_id=(action))
    action.mood = mood
    db.session.add(action)
  
  db.session.commit()

  return {'message': 'done'}