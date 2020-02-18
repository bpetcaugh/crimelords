from objects import distance

def calc_points(objects, color, radius=3):
	influence, money = 0, 0
	for object in objects:
		if object.type == "Police":
			for object_again in objects:
				if object_again.type in ["Mafioso", "Hitman", "Demo"]:
					if distance(object, object_again) == radius and object_again.color == color:
						influence = 10
		elif object.type == "Bank":
		 	for object_again in objects:
			 	if object_again.type in ["Mafioso", "Hitman", "Demo"]:
				 	if distance(object, object_again) == radius and object_again.color == color:
						money = 10
	return influence, money