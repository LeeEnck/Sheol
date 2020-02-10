from sys import exit
from random import randint
from textwrap import dedent


#Start
class area(object):

    def play(self):
        pass


class Death(area):

    def enter(self):
        print(dedent("""
            You have died
            """))

        exit(1)


class Hell(area):



    def play(self):
        print(dedent("""
               You have been sent to hell for your vulger and dispicable behavior.

               You can venture into the hellish boundaries.

               You can curl up into a ball and weep.
               """))

    choice = input('what do you do? Venture or Weep?')
    if choice == 'weep':
             print('You have failed miserably and are turned to ash!')

             return 'Death'
    else:
             print(dedent("""
                   Congrats pal you won't be swallowed by the
                   never-ending abyss we call hell!"""))

             return 'LavaPit'

class LavaPit(area):



    def play(self):
        print(dedent("""
              You have now arrived at the lava pit, and see a
              giant plumbus levitating.
              """))

        choice = input('What do you? Take it, leave it, or punt it?')
        if choice == 'take it':
            print(dedent("""
                  You gained a stupendous feat against all who defy you!"""))

            return 'Graveyard'

        if choice == 'leave it':
            print(dedent("""
                  A cursed Cyclopse runs towards you and cuts your worthless mortal body in half!"""))

            return 'death'

        else choice == 'punt it'
              print(dedent("""
                    The plumbus slides like a pregnant elephant on ice
                    across the glassy film on top of the pit. Then a it falls
                    into the endless pit of Hell, never to be retrieved!"""))

            return 'Graveyard'

class Graveyard(area):


    def play(self):
        print(dedent("""
              You have approached the graveyard of the banished
              and now you must choose what to do next. Either ignore
              the graveyard and continue on, or go into the undead land."""))

        choice = input('what will decide to do? Choose to ignore the graveyard, or go ahead.')
        if choice == 'ignore':
            print(dedent("""
                  You had decided to ignore the banished lands and have been turned to ash by a dark angel.
                  """))

            return 'Death'

        else choice == 'go ahead':
            print(dedent("""
                  You chose to move ahead and have gained some holy water from a dead frost giant,
                  to which you should cherish."""))

            return 'LavaFalls'

class LavaFalls(area):


    def play(self):
        print(dedent("""
               You feel the unwrenching heat of the lavafalls ahead and now have to overcome
               the largest obstacle that you have yet to discover.  """))

        choice = input('What will you decide to do build a raft of somesort to charge on? Or attempt to find an alternate route around the falls?')
        if choice == 'build raft':
            print(dedent("""
                  Congrats you have successfully built a hellish raft to get across the falls!
                  But little did you know an ancient demonic serpent lives below and
                  tosses you in the air and eats you!"""))

            return 'Death'

        else choice == 'alternate route'
             print(dedent("""
                   Fantastic job you have found another route aroudn the falls.
                   Now you much push on your journey to escape Hell's grasp!"""))

        return 'LucifersLair'

class LucifersLair(area):


    def play(self):
        print(dedent("""
              You fought through much of what Hell has to offer but now you
              must approach the demonic entity himself. While feeling his presence
              since you have arrived you feel a cold touch to your shoulder."""))

        choice = input('What will you do now? Turn around and try you skills in combat? Or throw what little holy water that you have saved on Lucifer to attempt to tourture him.')
        if choice == 'combat':
            Print(dedent("""
                  Lucifer accends from the depths of hell and completely abliterates your worthless corps into oblivion!"""))

        return 'death'

        else choice == 'throw holy water'
        print(dedent("""
              In a break of panic you decide to throw the holy water into the eyes of the hellish
              Lucifer, he yelps a war cry scream and slowly dwindles to the depths of the abyss.
              An old wrinkly spirit flows to your side and hands you Lucifers ancient coin, which
              is the token out of hell. He explains how you have knocked Lucifer into a century of
              deep sleep from the ancient holy water. Now you may speak his forsaken name and flip the
              coin."""))

        return 'HolyGrail'

class HolyGrail(area):


    def play(self):
        print(dedent("""
              You spoken his forsaken name and have also flipped the coin in the air.
              At first nothing happens, then all of a sudden
              you start falling into what seems like an endless black hole. Then
              you awake sweaty and cold in a hospital bed, free of the shackles of Hell.
              Congrats on proving your stoic perseverance as an individual especially
              against the cruel unwrenching being Lucifer!"""))

        exit(1)





class Map(object):

    areas = {
    'Death': Death(),
    'Hell': Hell(),
    'LavaPit': LavaPit(),
    'Graveyard': Graveyard(),
    'LavaFalls': LavaFalls(),
    'LucifersLair': LucifersLair(),
    'HolyGrail': HolyGrail(),
    }

def __init__(self, start_area):
    self.start_area = start_area

def next_area(self, area_name):
    val = Map.areas.get(area_name)
    return val

def opening_area(self):
    return self.next_area(self.start_area)
