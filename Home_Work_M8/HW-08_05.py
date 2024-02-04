import random


def get_random_winners(quantity, participants):
    print(f'Quantity: {quantity}, \nParticipants: {participants}')
    if len(participants) == 0:
        return []

    user_list = list(participants.keys())
    print(f'Users: {user_list}')
    random.shuffle(user_list)
    print(f'Users after Schuffle: {user_list}')
    
    winner_list = random.sample(user_list, k=quantity)
    print(f'Winners: {winner_list}')

    if quantity > len(participants):
        return []

    return winner_list