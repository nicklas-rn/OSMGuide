from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView

from . import models
from .models import Sideshow, CounterTactic, BestTactic, CounterTacticWeaker, CounterTacticStronger,\
    BeginnerTip, PlayerGroup, Player, TipGroup, Tip, ThankYou


def home(request):
    sideshows = Sideshow.objects.all()
    return render(request, 'guide/home.html', {'sideshows': sideshows})


def counter_tactics(request):
    counter_tactics = CounterTactic.objects.all()
    best_tactics = BestTactic.objects.all()
    counter_tactics_weaker = CounterTacticWeaker.objects.all()
    counter_tactics_stronger = CounterTacticStronger.objects.all()
    context = {
        'counter_tactics': counter_tactics,
        'best_tactics': best_tactics,
        'counter_tactics_weaker': counter_tactics_weaker,
        'counter_tactics_stronger': counter_tactics_stronger,
    }
    return render(request, 'guide/counter-tactics.html', context)


def overall_tactics(request):
    best_tactics = BestTactic.objects.all()
    context = {
        'best_tactics': best_tactics,
    }
    return render(request, 'guide/overall-tactics.html', context)


def counter_tactic_detail(request, title):
    title = title.replace("_", " ")
    counter_tactics = CounterTactic.objects.filter(title=title)
    best_tactics = BestTactic.objects.all()
    counter_tactics_weaker = CounterTacticWeaker.objects.all()
    counter_tactics_stronger = CounterTacticStronger.objects.all()
    context = {
        'counter_tactics': counter_tactics,
        'best_tactics': best_tactics,
        'counter_tactics_weaker': counter_tactics_weaker,
        'counter_tactics_stronger': counter_tactics_stronger,
    }
    return render(request, 'guide/tactics-detail.html', context)


def beginners_guide(request):
    tips = BeginnerTip.objects.all()
    context = {
        'tips': tips,
    }
    return render(request, 'guide/beginners_guide.html', context)


def players(request):
    player_groups = PlayerGroup.objects.all()
    players = Player.objects.all()
    context = {
        'player_groups': player_groups,
        'players': players,
    }
    return render(request, 'guide/players.html', context)


def tips(request):
    tip_groups = TipGroup.objects.all()
    tips = Tip.objects.all()
    context = {
        'tip_groups': tip_groups,
        'tips': tips,
    }
    return render(request, 'guide/tips.html', context)


def terms_of_use(request):
    return render(request, 'guide/terms_of_use.html')


def thank_you(request):
    supporters = ThankYou.objects.all()
    return render(request, 'guide/thank_you.html', {'supporters': supporters})

