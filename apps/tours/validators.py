from django.core.exceptions import ValidationError
 
 
 # CHECK(rate>0 AND rate<5)
def rating_range(value):
    if value < 1 or value > 5:
        raise ValidationError(f"Please choose rating's value from 1 to 5")