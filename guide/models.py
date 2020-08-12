from django.db import models


class Sideshow(models.Model):
    image = models.ImageField(default="banner.png", upload_to="sideshow_pics")
    title = models.CharField(max_length=70)
    content = models.CharField(max_length=200, help_text="Put //...// around a word if you wnat to make it bold")
    link = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class ThankYou(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return f"Thank you ({self.name})"


class Tactic(models.Model):
    formation_text = models.CharField(max_length=50, help_text="Put //...// around a word if you wnat to make it bold")
    formation_image = models.ImageField(upload_to="tactics/formations")

    style_of_play_text = models.CharField(max_length=50, help_text="Put //...// around a word if you wnat to make it bold")
    style_of_play_image = models.ImageField(upload_to="tactics/style_of_play")

    line_tactics_text = models.CharField(max_length=50, help_text="Put //...// around a word if you wnat to make it bold")
    line_tactics_image = models.ImageField(upload_to="tactics/line_tactics")

    marking_offside_text = models.CharField(max_length=50, help_text="Put //...// around a word if you wnat to make it bold")
    marking_offside_image = models.ImageField(upload_to="tactics/marking_offside")

    tackling_index_text = models.CharField(max_length=50, help_text="Put //...// around a word if you wnat to make it bold")
    tackling_index_image = models.ImageField(upload_to="tactics/tackling_index")

    class Meta:
        abstract = True


class CounterTactic(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class CounterTacticWeaker(Tactic):
    title = models.ForeignKey(CounterTactic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} (weaker opponent)"

    class Meta:
        verbose_name_plural = 'Counter tactic (weaker opponent)'


class CounterTacticStronger(Tactic):
    title = models.ForeignKey(CounterTactic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} (stronger opponent)"

    class Meta:
        verbose_name_plural = 'Counter tactic (stronger opponent)'


class BestTactic(Tactic):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class BeginnerTip(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to="beginner_tips_images")
    content = models.CharField(max_length=1000, help_text="BOLD: //x// to make x bold ................. "
                                                          "LINK: --x@/link@-- to go page link with text x")

    def __str__(self):
        return self.title


class PlayerGroup(models.Model):
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Player(models.Model):
    group = models.ForeignKey(PlayerGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    player_image = models.ImageField(upload_to="players/player_images")
    content = models.CharField(max_length=1000, help_text="BOLD: //x// to make x bold ............... "
                                                          "LINK: --x@/link@-- to go page link with text x")
    scout_image = models.ImageField(upload_to="players/scout_images")

    def __str__(self):
        return self.name


class TipGroup(models.Model):
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Tip(models.Model):
    group = models.ForeignKey(TipGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    tip_image = models.ImageField(upload_to="players/player_images", blank=True, null=True)
    content = models.CharField(max_length=1000, help_text="BOLD: //x// to make x bold ................ "
                                                          "LINK: --x@/link@-- to go page link with text x")

    def __str__(self):
        return self.name
