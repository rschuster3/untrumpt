from django.db import models

from multiselectfield import MultiSelectField


CATEGORY_CHOICES = (
    ('women', "Women's Rights"),
    ('racial_minorities', 'Rights of Racial Minorities'),
    ('religious_minorities', 'Rights of Religious Minorities'),
    ('immigrants', "Immigrants' Rights"),
    ('youths', "Helping Kids"),
    ('disabled', 'Rights of the Disabled'),
    ('environment', 'The Environment'),
    ('civil_rights', 'Civil Rights'),
    ('sexual_abuse', 'Protecting from Sexual Abuse'),
    ('lgbt', 'LGBT Rights'),
    ('reproduction', 'Reproductive Rights'),
    ('homeless', 'Homelessness'),
    ('guns', 'Gun Laws'),
    ('drugs', 'Drug Laws'),
)


class Organization(models.Model):
    # Required fields
    name = models.CharField(
        max_length=100,
        help_text="The name of the organization", blank=False
    )
    website = models.URLField(
        max_length=250,
        help_text="URL of the ogranization's website",
        blank=False
    )
    categories = MultiSelectField(
        choices=CATEGORY_CHOICES,
        max_choices=3,
        blank=False
    )

    # Non-required fields
    acronym = models.CharField(
        max_length=25,
        help_text="Acronym of the organization if it's widely used",
        blank=True
    )
    donate_url = models.URLField(
        help_text="URL to org's 'donate' page",
        blank=True
    )
    involvement_url = models.URLField(
        help_text="URL to org's 'take action' or 'get involved' or 'volunteer' page",
        blank=True
    )
    description = models.TextField(
        help_text="Mission statement of the org",
        blank=True
    )
    facebook_url = models.URLField(
         help_text="URL of org's Facebook group",
         blank=True
    )
    twitter_handle = models.CharField(
        max_length=50,
        help_text="Twitter handle of the organization, including @ sign",
        blank=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
