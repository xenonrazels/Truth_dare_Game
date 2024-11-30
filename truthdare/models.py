from django.db import models

# Create your models here.

    
class Players(models.Model):
    GENDER_CHOICES=[('Male',"Male"),("Female","Female")]
    AGE_TYPE_CHOICES=[('Adult','Adult'),("Child","Child"),("Old",'Old')]
    name=models.CharField(max_length=30,blank=False)
    gender=models.CharField(choices=GENDER_CHOICES,max_length=40)
    ageType=models.CharField(choices=AGE_TYPE_CHOICES,max_length=30)

    def __str__(self):
        return self.name
    
class TruthQuestion(models.Model):
    question=models.TextField()
    hot_rank=models.IntegerField()
    
    def __str__(self):
        return f'{self.question} +{self.hot_rank}'
class DareQuestion(models.Model):
    question=models.TextField()
    hot_rank=models.IntegerField()

    def __str__(self):
        return f'{self.question} +{self.hot_rank}'
    
class Game_board(models.Model):
    players = models.ManyToManyField(Players,related_name='players')
    
    def __str__(self):
        # Get a list of player names
        player_names = ', '.join([player.name for player in self.players.all()])
        return f"Game Board with players: {player_names}"

class playing_with(models.Model):
    Choices=[("family","family"),("friends","friends"),("family & friends","family & friends")]
    Typechoices=models.CharField(choices=Choices,max_length=20)