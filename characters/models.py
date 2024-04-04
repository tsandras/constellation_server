from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

ATTRIBUTES = [
    ("STR", _("Strength")),
    ("DEX", _("Dexterity")),
    ("STA", _("Stamina")),
    ("QUI", _("Quickness")),
    ("RES", _("Resistance")),
    ("INT", _("Intelligence")),
    ("CHA", _("Charisma")),
    ("WIL", _("Will")),
    ("POW", _("Power")),
]

NODE_CATEGORIES = [
    ("SKILL_PRO", _("skill_proficiency")),
    ("SKILL_EXP", _("skill_expertise")),
    ("SPELL_PRO", _("spell_proficiency")),
    ("SPELL_EXP", _("spell_expertise")),
    ("BACKGROUND", _("background")),
    ("NOTABLE", _("notable")),
    ("KEYSTONE", _("keystone")),
    ("ATTRIBUTE", _("attribute")),
]

SPELL_CATEGORIES = [
    ("MENTAL", _("mental")),
    ("HANDLING", _("handling")),
    ("ALTERATION", _("alteration"))
]

SKILL_CATEGORIES = [
    ("KNOWLEDGE", _("knowledge")),
    ("SOCIAL", _("social")),
    ("FIGHT", _("fight")),
    ("APTITUDE", _("aptitude")),
    ("TALENT", _("talent")),
]

class Notable(models.Model):
    name = models.CharField(_("name"), max_length=200)
    description = models.TextField(_("description"))

    def __str__(self):
        return self.name

class Keystone(models.Model):
    name = models.CharField(_("name"), max_length=200)
    description = models.TextField(_("description"))

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(_("name"), max_length=200)
    description = models.TextField(_("description"))
    category = models.CharField(choices=SKILL_CATEGORIES)

    def __str__(self):
        return self.name

class Speciality(models.Model):
    name = models.CharField(_("name"), max_length=200)
    skill = models.ForeignKey(
        Skill,
        on_delete=models.PROTECT,
        related_name="specialities",
        verbose_name=_("skill")
    )

    def __str__(self):
        return self.name

class Background(models.Model):
    name = models.CharField(_("name"), max_length=200)
    description = models.TextField(_("description"))
    rank_description = models.TextField(_("rank_description"))

    def __str__(self):
        return self.name

class Spell(models.Model):
    name = models.CharField(_("name"), max_length=200)
    description = models.TextField(_("description"))
    category = models.CharField(choices=SPELL_CATEGORIES)

    def __str__(self):
        return self.name

class Improvement(models.Model):
    name = models.CharField(_("name"), max_length=200)
    description = models.TextField(_("description"))
    spell = models.ForeignKey(
        Spell,
        on_delete=models.PROTECT,
        related_name="improvements",
        verbose_name=_("spell")
    )

    def __str__(self):
        return self.name

class Board(models.Model):
    name = models.CharField(_("name"), max_length=200)
    description = models.TextField(_("description"))
    width = models.IntegerField(_("width"), default=200)
    height = models.IntegerField(_("height"), default=150)
    is_advanced = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Node(models.Model):
    # A node can give to a character:
    # 1) proficiency in a skill or a new speciality in this skill if already proficient
    # 2) expertise in a skill (only from skill category)
    # 3) proficiency in a spell or a new improvement in this spell if already proficient
    # 4) expertise in a spell (only from spell category)
    # 5) +1 rank in a background
    # 6) one notable
    # 7) one keystone
    # 8) +1 in a attribute
    name = models.CharField(_("name"), max_length=200)
    description = models.TextField(_("description"))
    image_name = models.CharField(_("image_name"), max_length=200, null=True, blank=True)
    board = models.ForeignKey(
        Board,
        on_delete=models.PROTECT,
        related_name="nodes",
        verbose_name=_("board")
    )
    position_x = models.IntegerField(
        _("position_x"),
        default=0,
        validators=[MaxValueValidator(200), MinValueValidator(0)]
    )
    position_y = models.IntegerField(
        _("position_y"),
        default=0,
        validators=[MaxValueValidator(150), MinValueValidator(0)]
    )
    links = models.ManyToManyField("self", verbose_name=_("links"), blank=True)

    category = models.CharField(_("category"), choices=NODE_CATEGORIES)
    skill = models.OneToOneField(Skill, verbose_name=_("skill"), on_delete=models.PROTECT, null=True, blank=True)
    spell = models.OneToOneField(Spell, verbose_name=_("spell"), on_delete=models.PROTECT, null=True, blank=True)
    background = models.OneToOneField(Background, verbose_name=_("background"), on_delete=models.PROTECT, null=True, blank=True)
    notable = models.OneToOneField(Notable, verbose_name=_("notable"), on_delete=models.PROTECT, null=True, blank=True)
    keystone = models.OneToOneField(Keystone, verbose_name=_("keystone"), on_delete=models.PROTECT, null=True, blank=True)
    skill_expertise = models.CharField(_("skill_expertise"), choices=SKILL_CATEGORIES, null=True, blank=True)
    spell_expertise = models.CharField(_("spell_expertise"), choices=SPELL_CATEGORIES, null=True, blank=True)
    bonus = models.IntegerField(
        _("bonus"),
        default=0,
        validators=[MaxValueValidator(1), MinValueValidator(-1)]
    )
    bonus_range = ArrayField(
        models.CharField(choices=ATTRIBUTES),
        default=list,
        size=9,
        blank=True
    )

    def __str__(self):
        return self.name

def default_character_attributes():
    return list((1, 1, 1, 1, 1, 1, 1, 1, 1))

class Character(models.Model):
    name = models.CharField(_("name"), max_length=200)
    note = models.TextField(_("note"), blank=True, null=True)
    boards = models.ManyToManyField(Board, verbose_name=_("boards"), blank=True)
    nodes = models.ManyToManyField(Node, verbose_name=_("notable"), blank=True)
    skill_expertises = models.ManyToManyField(Skill, verbose_name=_("skill_expertises"), blank=True)
    spell_expertises = models.ManyToManyField(Spell, verbose_name=_("spell_expertises"), blank=True)
    specialities = models.ManyToManyField(Speciality, verbose_name=_("specialities"), blank=True)
    improvements = models.ManyToManyField(Improvement, verbose_name=_("improvements"), blank=True)
    attributes = ArrayField(
        models.IntegerField(validators=[MaxValueValidator(0), MinValueValidator(9)]),
        default=default_character_attributes,
        size=9,
    )

    def __str__(self):
        return self.name