from django.db import models

class Match(models.Model):
    competition = models.CharField(max_length=100)
    match_between = models.CharField(max_length=100)
    versus = models.CharField(max_length=100)
    toss_won_by = models.CharField(max_length=100)
    elected_to = models.CharField(max_length=50)
    overs = models.IntegerField()
    pitch_type = models.CharField(max_length=50)
    ball_type = models.CharField(max_length=50)
    date = models.DateField()
    scorer_signature = models.CharField(max_length=100, blank=True)
    losing_captain = models.CharField(max_length=100, blank=True)
    umpires = models.CharField(max_length=100, blank=True)
    team1_score = models.IntegerField(default=0)
    team1_wickets = models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)
    team2_wickets = models.IntegerField(default=0)

class Batsman(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    innings = models.IntegerField()  # 1 for first innings, 2 for second innings
    name = models.CharField(max_length=100)
    runs = models.IntegerField(default=0)
    balls_faced = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)
    strike_rate = models.FloatField(default=0.0)

class Bowler(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    innings = models.IntegerField()
    name = models.CharField(max_length=100)
    overs = models.FloatField(default=0.0)
    maidens = models.IntegerField(default=0)
    runs_given = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    wides = models.IntegerField(default=0)
    no_balls = models.IntegerField(default=0)
    economy = models.FloatField(default=0.0)

class FallOfWicket(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    innings = models.IntegerField()
    wicket_number = models.IntegerField()
    score_at_wicket = models.IntegerField()
