from django.shortcuts import render,redirect
from .forms import PlayersForm
from .models import Players, Game_board,TruthQuestion,DareQuestion
import random
# Create your views here.
def index(request):
    return render(request,'home.html')





def addPlayer(request):
    if request.method == 'POST':
        player_data = []
        player_count = len([key for key in request.POST.keys() if key.startswith('player') and key.endswith('-name')])

        # Gather all player data
        for i in range(1, player_count + 1):
            player_data.append({
                'name': request.POST.get(f'player{i}-name'),
                'gender': request.POST.get(f'player{i}-gender'),
                'ageType': request.POST.get(f'player{i}-ageType'),
            })

        # Save each player's data
        players = []
        for data in player_data:
            form = PlayersForm(data)
            if form.is_valid():
                player = form.save()  # Save each player's data
                players.append(player)
            else:
                # Re-render the form with errors if any form is invalid
                return render(request, 'add_players.html', {'form': form})

        # Create a new Game_board and associate players with it
        game_board = Game_board.objects.create()  # Create a new game board instance
        game_board.players.set(players)  # Associate players with the game board
        game_board.save()  # Save the game board

        # Save the game board ID (you can use it for later access, like in the game view)
        game_board_id = game_board.id

        # Redirect to a page that shows the created game board or another part of the game
        return redirect('game_board_detail', game_board_id=game_board_id)  # Redirect to the game board detail page

    # Render the initial form if it's a GET request
    form = PlayersForm()
    return render(request, 'add_players.html', {'form': form})

def game_board_detail(request, game_board_id):
    game_board = Game_board.objects.get(id=game_board_id)
    return render(request, 'game_board_detail.html', {'game_board': game_board})
from django.http import JsonResponse
from .models import Game_board
import random

def spin_wheel(request, game_board_id):
    # Fetch the game board and associated players
    game_board = Game_board.objects.get(id=game_board_id)
    players = list(game_board.players.all())  # Get all players associated with the game board

    # Randomly select a player
    selected_player = random.choice(players)

    # Randomly select whether it's Truth or Dare
    truth_or_dare = random.choice(["Truth", "Dare"])

    if truth_or_dare=="Truth":
        truth_question=TruthQuestion.objects.all()
        selected_truth=random.choice(truth_question)
        selected_question=selected_truth.question
    if truth_or_dare=="Dare":
        dare_question=DareQuestion.objects.all()
        selected_dare=random.choice(dare_question)
        selected_question=selected_dare.question


    # Return the result as a JSON response
    return JsonResponse({
        'selected_player': {'name': selected_player.name},
        'truth_or_dare': truth_or_dare,
        'selected_question':selected_question
    })


   
