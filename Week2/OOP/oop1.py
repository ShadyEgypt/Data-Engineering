
class Pokemon:
    name = "This is the default name"
    type = "default type"
    health = "default health"


Pikachu_obj = Pokemon()
print(Pikachu_obj.name)
Pikachu_obj.name = 'Pikachu'
Pikachu_obj.type = 'Electric'
Pikachu_obj.health = 70

print(Pikachu_obj.name,Pikachu_obj.type,Pikachu_obj.health)

Charizard_obj = Pokemon()
print(Charizard_obj.name)
Charizard_obj.name = 'Charizard'
Charizard_obj.type = 'Electric'
Charizard_obj.health = 70