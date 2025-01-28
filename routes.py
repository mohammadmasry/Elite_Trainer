from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import db, PlayerProfile, Event, Lineup
from datetime import datetime


bp = Blueprint('player', __name__, template_folder='templates')

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/lineup_manager', methods=['GET'])
def lineup_manager():
    players = PlayerProfile.query.all()  
    return render_template('lineup_manager.html', players=players)

@bp.route('/save_lineup', methods=['POST'])
def save_lineup():
    lineup_data = request.json
    for item in lineup_data:
        lineup = Lineup(position=item['position'], player_id=item['playerId'])
        db.session.add(lineup)
    db.session.commit()
    return jsonify({'message': 'Lineup saved successfully!'})

@bp.route('/events/rsvp/<int:event_id>', methods=['POST'])
def rsvp_event(event_id):
    player_name = request.form['player_name']
    event = Event.query.get_or_404(event_id)

    # Ensure attendees is initialized as a list if it's None
    if event.attendees is None:
        event.attendees = []

    # Check if the player has already RSVP'd
    if player_name in event.attendees:
        return redirect(url_for('player.view_events', error="Player has already RSVP'd!"))

    # Append the player to the attendees list
    attendees = event.attendees  # Get the current attendees list
    attendees.append(player_name)
    event.attendees = attendees  # Reassign to ensure changes are persisted

    # Commit changes to the database
    db.session.commit()

    return redirect(url_for('player.view_events'))


@bp.route('/players/new', methods=['GET', 'POST'])
def create_player():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        player_number = request.form['player_number']  # Replace position and statistics

        # Create a new player instance
        new_player = PlayerProfile(
            name=name,
            age=int(age),
            player_number=int(player_number)  # Save player_number instead
        )

        # Add and commit the new player to the database
        db.session.add(new_player)
        db.session.commit()

        # Redirect to the view players page
        return redirect(url_for('player.view_players'))

    # Render the form for GET requests
    return render_template('create_player.html')


@bp.route('/players', methods=['GET'])
def view_players():
    players = PlayerProfile.query.all()
    return render_template('view_players.html', players=players)

@bp.route('/players/edit/<int:id>', methods=['GET', 'POST'])
def edit_player(id):
    player = PlayerProfile.query.get_or_404(id)
    if request.method == 'POST':
        # Update player fields
        player.name = request.form['name']
        player.age = int(request.form['age'])
        player.player_number = int(request.form['player_number'])  # Update player_number
        db.session.commit()
        return redirect(url_for('player.view_players'))
    return render_template('edit_player.html', player=player)


@bp.route('/players/delete/<int:id>', methods=['POST'])
def delete_player(id):
    player = PlayerProfile.query.get_or_404(id)
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for('player.view_players'))

# Event CRUD
@bp.route('/events/new', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description', None)  # Handle optional fields
        location = request.form['location']
        
        # Convert the form inputs for `date` and `time` into Python objects
        form_date = request.form['date']
        form_time = request.form['time']
        
        try:
            event_date = datetime.strptime(form_date, '%Y-%m-%d').date()  # Convert to `datetime.date`
            event_time = datetime.strptime(form_time, '%H:%M').time()    # Convert to `datetime.time`
        except ValueError as e:
            # Handle invalid date or time formats
            return render_template('create_event.html', error=f"Invalid date or time: {e}")
        
        attendees = []  # Default to an empty list
        new_event = Event(
            title=title,
            description=description,
            date=event_date,
            time=event_time,
            location=location,
            attendees=attendees
        )
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('player.view_events'))
    return render_template('create_event.html')

@bp.route('/events', methods=['GET'])
def view_events():
    events = Event.query.all()
    return render_template('view_events.html', events=events)
