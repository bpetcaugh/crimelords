
 def add_points(objects):
     for object in objects: 
         if object.type == PoliceStation: 
             for object_again in objects: 
                 if object_again.type ==  Mafioso or Hitman or Demo: 
                     if distance(object, object_again) == 1: 
                         tcolor = object_again.color 
                         if tcolor == red: 
                             rd_influence = rd_influence + 10
                         if tcolor == blue: 
                             bl_influence = bl_influence + 10
        if object.type == Bank: 
             for object_again in objects: 
                 if object_again.type ==  Mafioso or Hitman or Demo: 
                     if distance(object, object_again) == 1: 
                         tcolor = object_again.color 
                         if tcolor == red: 
                             rd_money = rd_money + 10
                         if tcolor == blue: 
                             bl_money = money + 10