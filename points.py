from objects import distance

def calc_points(buildings, units, color, radius=3):
	influence, money = 0, 10
	for object in buildings:
		if object.type == "Police":
			for object_again in units:
				if distance(object.location, object_again.location) == radius and object_again.color == color:
					influence = 10
		elif object.type == "Bank":
			for object_again in units:
				if distance(object.location, object_again.location) == radius and object_again.color == color:
					money = 20
	return influence, money