from django.db import models


class WizardsManager(models.Manager):
    
    def basic_validator(self, postData):
        errors = {}

        if len(postData['name']) < 4:
            errors["name"] = "El nombre del Mago debe tener al menos 4 letras"
        
        if len(postData['house_id']) < 1:
            errors["house_id"] = "Debe seleccionar al menos 1 casa"
        
        if len(postData['pet']) < 4:
            errors["pet"] = "El nombre de la Mascota debe tener al menos 4 letras"
        
        try:
            year = int(postData['year'])
            if year < 1:
                errors['year'] = "El año debe ser al menos 1"

        except ValueError:
            errors["year"] = "El campo 'Año' debe ser un número"
        
        return errors


class Houses(models.Model):
    name = models.CharField(max_length=45)
    color = models.CharField(max_length=45)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # wizards => Lista de Magos de esta casa


class Wizards(models.Model):
    name = models.CharField(max_length=45)
    house = models.ForeignKey(Houses, related_name="wizards", on_delete = models.CASCADE)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()
    avatar = models.URLField(
        default='https://partfy.com/blog/wp-content/uploads/2020/05/mejoresmagosespa%C3%B1oles-1000x550.jpg'
    )

    # spells = models.ManyToManyField(Spell, related_name='wizards')

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = WizardsManager()

    def __repr__(self) -> str:
        return f'{self.id}: {self.name}'