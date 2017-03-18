import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = location
    def get_name(self):
        return self.name
    def get_location(self):
        result = ()
        for i in self.location:
            result += (float(i),)
        return result 
    def get_species_count(self):
        try:
            return self.copy
        except AttributeError:
            return self.species_types.copy()
    def get_number_of_species(self, species_name):
        return self.species_types[species_name]
    def adopt_pet(self, species_name):
        self.species_types[species_name] -= 1
        if self.species_types[species_name] <= 0:
            self.copy = self.species_types.copy()
            del self.copy[species_name]   


class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        return float(adoption_center.get_number_of_species(self.desired_species))



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        self.considered_species = considered_species 
        Adopter.__init__(self, name, desired_species)
    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self, adoption_center)
        num_other = 0
        for species in self.considered_species:
            num_other += float(adoption_center.get_number_of_species(species))
        return adopter_score + 0.3*num_other

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        self.feared_species = feared_species
        Adopter.__init__(self, name, desired_species)
    def get_score(self, adoption_center):
       adopter_score = Adopter.get_score(self, adoption_center)
       num_feared = adoption_center.get_number_of_species(self.feared_species)
       if adopter_score >= 0.3*num_feared:
           return adopter_score - 0.3*num_feared
       return 0.0

class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        self.allergic_species = allergic_species
        Adopter.__init__(self, name, desired_species)
    def get_score(self, adoption_center):
        for species in self.allergic_species:
            if species in adoption_center.species_types:
                return 0.0
        return Adopter.get_score(self, adoption_center)

class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        self.medicine_effectiveness = medicine_effectiveness 
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
    def get_score(self, adoption_center): 
        specials = {}
        for effectiveness in self.medicine_effectiveness.keys():
            if effectiveness in adoption_center.species_types:
                specials[effectiveness] = self.medicine_effectiveness[effectiveness]
        if specials != {}:
            return min(specials.values())*Adopter.get_score(self, adoption_center)
        return Adopter.get_score(self, adoption_center)
            


class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        self.location = location
        Adopter.__init__(self, name, desired_species)
    def get_linear_distance(self, to_location):
        self.to_location = to_location
        self.distance = ((self.to_location[0] - self.location[0])**2 + (self.to_location[1] - self.location[1])**2)**0.5
    def get_score(self, adoption_center):
        SluggishAdopter.get_linear_distance(self, adoption_center.get_location())
        if self.distance < 1:
            return 1 * self.desired_species
        elif 1 <= self.distance < 3:
            return rand.uniform(0.7, 0.9) * adoption_center.get_number_of_species(self.desired_species)
        elif 3 <= self.distance < 5:
            return rand.uniform(0.5, 0.7) * adoption_center.get_number_of_species(self.desired_species)
        elif 5 <= self.distance:
            return rand.uniform(0.1, 0.5) * adoption_center.get_number_of_species(self.desired_species)
            
    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the 
    scores for each AdoptionCenter to the Adopter will be ordered from highest 
    score to lowest score.
    """
    score = {}
    for adopter_center in list_of_adoption_centers:
        try:
            score[adopter_center] = adopter.get_score(adopter_center)
        except KeyError:
            score[adopter_center] = 0
            
    return sorted(sorted(score.items(),key = lambda name: name[0].get_name),key = lambda score: score[1], reverse=True)

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from 
    list_of_adopters (in numerical order of score)
    """
    score = {}
    for adopter in list_of_adopters:
        try:
            score[adopter] = adopter.get_score(adoption_center)
        except KeyError:
            score[adopter] = 0
            
    return sorted(score, key = score.__getitem__, reverse=True)[:n]
    
adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog") 

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))

# how to test get_adopters_for_advertisement
print get_adopters_for_advertisement(ac, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)
# you can print the name and score of each item in the list returned

adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat") 

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))

# how to test get_ordered_adoption_center_list
print get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac6])                            
# you can print the name and score of each item in the list returned
                            