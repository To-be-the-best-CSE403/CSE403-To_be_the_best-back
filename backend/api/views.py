from flask import Blueprint, request, jsonify

views = Blueprint('views', __name__)


@views.route('/')
def api_index():
    return 'Index'


@views.route('/home')
def api_home():
    return 'Hello, World!'


@views.route('/generate-team')
def api_generate_team():
    return [
        {
            'name': 'Pikachu',
            'item': 'Light Ball',
            'ability': 'Static',
            'nature': 'Timid',
            'moves': [
                'Thunderbolt',
                'Volt Switch',
                'Grass Knot',
                'Quick Attack',
            ],
        },
        {
            'name': 'Charizard',
            'item': 'Assault Vest',
            'ability': 'Blaze',
            'nature': 'Modest',
            'moves': [
                'Flamethrower',
                'Air Slash',
                'Dragon Pulse',
                'Focus Blast',
            ],
        }
    ]


@views.route('/usage-rate')
def api_usage_rate():
    return [
        {
            'name': 'Pikachu',
            'usage': 0.5,
        },
        {
            'name': 'Charizard',
            'usage': 0.5,
        },
    ]


@views.route('/common-movesets', methods=['GET'])
def api_common_movesets():
    pokemon = request.args.get('pokemon')

    if not pokemon:
        return jsonify({'error': 'Missing "pokemon" parameter'}), 400
    
    return jsonify({
        'pokemon': pokemon,
    })
