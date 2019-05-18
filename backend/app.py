from bottle import get, post, run, request
import uuid


class Game:
    def __init__(self, game_id, current_coordinates):
        self.id = game_id
        self.current_coordinates = current_coordinates


games = []


@get('/api/games')
def get_games():
    return {
        "games": [{"game_id": g.id, "coordinates": g.current_coordinates} for g in games]
    }


@post('/api/games')
def post_game():
    g = Game(str(uuid.uuid4()), (56.832469, 60.605989))

    games.append(g)

    return {
        "game_id": g.id
    }


@get('/api/games/<game_id>')
def get_game(game_id):
    return {
        "id": game_id
    }


run(host='localhost', port=8080, debug=True, server='paste')
