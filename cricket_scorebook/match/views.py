from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Match, Batsman, Bowler, FallOfWicket


# Serve the index.html page
def index(request):
    return render(request, 'match/index.html')  # Ensure the HTML file is in the templates folder

# API to save match data
@csrf_exempt
def save_match(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Save match details
            match = Match.objects.create(
                competition=data['competition'],
                match_between=data['matchBetween'],
                versus=data['versus'],
                toss_won_by=data['tossWonBy'],
                elected_to=data['electedTo'],
                overs=data['overs'],
                pitch_type=data['pitchType'],
                ball_type=data['ballType'],
                date=data['date'],
                scorer_signature=data.get('scorerSignature', ''),
                losing_captain=data.get('losingCaptain', ''),
                umpires=data.get('umpires', ''),
                team1_score=data['team1Score'],
                team1_wickets=data['team1Wickets'],
                team2_score=data['team2Score'],
                team2_wickets=data['team2Wickets'],
            )

            # Save batsmen details
            for batsman in data['batsmen']:
                Batsman.objects.create(
                    match=match,
                    innings=batsman['innings'],
                    name=batsman['name'],
                    runs=batsman['runs'],
                    balls_faced=batsman['ballsFaced'],
                    fours=batsman['fours'],
                    sixes=batsman['sixes'],
                    strike_rate=batsman['strikeRate'],
                )

            # Save bowlers details
            for bowler in data['bowlers']:
                Bowler.objects.create(
                    match=match,
                    innings=bowler['innings'],
                    name=bowler['name'],
                    overs=bowler['overs'],
                    maidens=bowler['maidens'],
                    runs_given=bowler['runsGiven'],
                    wickets=bowler['wickets'],
                    wides=bowler['wides'],
                    no_balls=bowler['noBalls'],
                    economy=bowler['economy'],
                )

            # Save fall of wickets
            for wicket in data['fallOfWickets']:
                FallOfWicket.objects.create(
                    match=match,
                    innings=wicket['innings'],
                    wicket_number=wicket['wicketNumber'],
                    score_at_wicket=wicket['scoreAtWicket'],
                )

            return JsonResponse({'status': 'success', 'id': match.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def load_match(request, match_id):
    try:
        # Fetch the match from the database
        match = Match.objects.get(id=match_id)

        # Fetch related batsmen, bowlers, and fall of wickets
        batsmen = Batsman.objects.filter(match=match).values(
            'innings', 'name', 'runs', 'balls_faced', 'fours', 'sixes', 'strike_rate'
        )
        bowlers = Bowler.objects.filter(match=match).values(
            'innings', 'name', 'overs', 'maidens', 'runs_given', 'wickets', 'wides', 'no_balls', 'economy'
        )
        fall_of_wickets = FallOfWicket.objects.filter(match=match).values(
            'innings', 'wicket_number', 'score_at_wicket'
        )

        # Return all the data for the match
        match_data = {
            'id': match.id,
            'competition': match.competition,
            'matchBetween': match.match_between,
            'versus': match.versus,
            'tossWonBy': match.toss_won_by,
            'electedTo': match.elected_to,
            'overs': match.overs,
            'pitchType': match.pitch_type,
            'ballType': match.ball_type,
            'date': match.date,
            'scorerSignature': match.scorer_signature,
            'losingCaptain': match.losing_captain,
            'umpires': match.umpires,
            'team1Score': match.team1_score,
            'team1Wickets': match.team1_wickets,
            'team2Score': match.team2_score,
            'team2Wickets': match.team2_wickets,
            'batsmen': list(batsmen),
            'bowlers': list(bowlers),
            'fallOfWickets': list(fall_of_wickets)
        }

        return JsonResponse({'status': 'success', 'match': match_data})

    except Match.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Match not found'})

@csrf_exempt
def delete_match(request, match_id):
    if request.method == 'DELETE':
        try:
            # Get the match by ID
            match = Match.objects.get(id=match_id)

            # Delete the match from the database
            match.delete()

            # Return a success response
            return JsonResponse({'status': 'success', 'message': 'Match deleted successfully.'})
        except Match.DoesNotExist:
            # If the match doesn't exist
            return JsonResponse({'status': 'error', 'message': 'Match not found.'})
    else:
        # Invalid HTTP method
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def get_saved_matches(request):
    matches = Match.objects.all()
    data = [{'id': match.id, 'matchBetween': match.match_between, 'versus': match.versus} for match in matches]
    return JsonResponse(data, safe=False)
