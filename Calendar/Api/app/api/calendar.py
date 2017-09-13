from flask import Blueprint, make_response, jsonify

from app.models import ToDoItem, make_calendar, make_todo

ics_feed = Blueprint('ics', __name__)


@ics_feed.route('/ics', methods=['GET'])
def index():

    calendar = make_calendar()

    todos = ToDoItem.query.all()

    # for todo in todos:
    #    component = make_todo(todo)
    #    calendar.add_component(component)

    # response = make_response(calendar.to_ical())

    # response.headers["Content-Disposition"] = "attachment; filename=calendar.ics"
    # return response
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
