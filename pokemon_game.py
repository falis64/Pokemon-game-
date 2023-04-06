import requests
import random

# Define constants
api_base_url = 'https://pokeapi.co/api/v2'
MAX_POKEMON_ID = 898  # latest pokemon as of 2021


# Helper functions
def get_pokemon_data(pokemon_id):
    url = f'{api_base_url}/pokemon/{pokemon_id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data['name'].capitalize(),
            'type': data['types'][0]['type']['name'].capitalize(),
            'attack': data['stats'][1]['base_stat'],
            'defense': data['stats'][2]['base_stat']
        }
    else:
        raise ValueError(f'Could not get data for pokemon with ID {pokemon_id}')


def print_pokemon_info(pokemon_data):
    print(
        f"{pokemon_data['name']} ({pokemon_data['type']}) - Attack: {pokemon_data['attack']}, Defense: {pokemon_data['defense']}")


def calculate_damage(attacker_data, defender_data):
    # Simple damage calculation using attacker's attack and defender's defense stats
    damage = attacker_data['attack'] - defender_data['defense']
    return max(damage, 1)  # minimum damage is 1


# Game logic
def choose_pokemon():
    # You can modify this function to implement your own pokemon selection logic
    pokemon_id = random.randint(1, MAX_POKEMON_ID)
    return get_pokemon_data(pokemon_id)


def play_game():
    print('Welcome to the Pokemon Battle!')
    player_pokemon = choose_pokemon()
    cpu_pokemon = choose_pokemon()

    print('Player 1, your pokemon is:')
    print_pokemon_info(player_pokemon)

    input('Press enter to continue...')

    print('The CPU has chosen its pokemon:')
    print_pokemon_info(cpu_pokemon)

    input('Press enter to start the battle...')

    player_damage = calculate_damage(player_pokemon, cpu_pokemon)
    cpu_damage = calculate_damage(cpu_pokemon, player_pokemon)

    if player_damage > cpu_damage:
        print('Congratulations! You win!')
    elif cpu_damage > player_damage:
        print('Sorry, you lose. Better luck next time.')
    else:
        print('It\'s a tie!')


# Main program
if __name__ == '__main__':
    while True:
        print('Choose a mode:')
        print('1. Single player')
        print('2. Two players')
        mode = input('Enter the number of the mode you want to play: ')

        if mode == '1':
            play_game()
            break
        elif mode == '2':
            print('Sorry, two player mode is not implemented yet.')
            # Implement two player mode here
        else:
            print('Invalid mode. Please choose 1 or 2.')
