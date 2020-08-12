from django.contrib import admin

from .models import Sideshow, CounterTactic, BestTactic, CounterTacticWeaker, CounterTacticStronger, \
    BeginnerTip, PlayerGroup, Player, TipGroup, Tip, ThankYou


# COMBINE PLAYERGROUP AND PLAYERS
class PlayerInline(admin.StackedInline):
    model = Player
    extra = 0


class PlayerGroupAdmin(admin.ModelAdmin):
    fieldsets = [
        ('PlayerGroup', {'fields': ['title', 'keywords']})
    ]
    inlines = [PlayerInline]
    list_display = ('title', 'keywords')


admin.site.register(PlayerGroup, PlayerGroupAdmin)


# COMBINE TIPGROUP AND TIPS
class TipInline(admin.StackedInline):
    model = Tip
    extra = 0


class TipGroupAdmin(admin.ModelAdmin):
    fieldsets = [
        ('TipGroup', {'fields': ['title', 'keywords']})
    ]
    inlines = [TipInline]
    list_display = ('title', 'keywords')


admin.site.register(TipGroup, TipGroupAdmin)


# COMBINE COUNTER TACTICS
class CounterTacticWeakerInline(admin.StackedInline):
    model = CounterTacticWeaker
    extra = 0


class CounterTacticStrongerInline(admin.StackedInline):
    model = CounterTacticStronger
    extra = 0


class CounterTacticAdmin(admin.ModelAdmin):
    fieldsets = [
        ('CounterTactic', {'fields': ['title']})
    ]
    inlines = [CounterTacticWeakerInline, CounterTacticStrongerInline]
    list_display = ('title', )


admin.site.register(CounterTactic, CounterTacticAdmin)


admin.site.register(Sideshow)
admin.site.register(BestTactic)
admin.site.register(BeginnerTip)
admin.site.register(ThankYou)



