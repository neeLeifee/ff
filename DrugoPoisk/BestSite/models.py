from django.db import models

# Создаём класс, через который сможем потом сделать таблицу в базе данных
# Название класса = название таблицы
# Каждое новое поле - новый столбец в таблице
# Cколько мы создали переменных в классе, столько столбцов и будет, в этом случае их будет три
#_________________________
#|number |name   |x      |
#|-------|-------|-------|
#|       |       |       |
#|       |       |       |
#|       |       |       |
#________|_______|_______|
class  MyNewModel(models.Model):
    name = models.CharField(max_length=128)
    number = models.PositiveSmallIntegerField()
    x = models.TextField()
    # Имена переменных могут быть любыми!!! Мы могли так же написать наоброт и получилось бы:
    #     name = models.PositiveSmallIntegerField()
    #     number = models.CharField(max_length=128)