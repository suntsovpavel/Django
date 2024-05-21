from django import forms

class GamesForm(forms.Form):
    game_type = forms.ChoiceField(choices=[('coin', 'монетка'),
                                  ('cube', 'кубик'),
                                  ('number', 'число')])
    num_tries = forms.IntegerField(min_value=1, max_value=64)