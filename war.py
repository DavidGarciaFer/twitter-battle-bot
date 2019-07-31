"""
File: war.py
Author: David Garcia Fernandez
Date: 27/07/2019
Description: Player and War classes for Twitter Battle Royale Bot.
"""
import csv
import cv2 as cv
import numpy as np
from shutil import copyfile


class Player:
    """
    Player data.

    Args:
        name (str): Player's name.
        message (str): Customizable message to display when player eliminates an opponent.
        day (str): Indicates the day when the player was eliminated, else '0'
        kills (str): Number of eliminations by this player.

    Attributes:
        name (str): Player's name.
        message (str): Customizable message to display when player eliminates an opponent.
        day (str): Indicates the day when the player was eliminated, else '0'
        kills (str): Number of eliminations by this player.
    """
    def __init__(self, name, message, day, kills):
        self.name = name
        self.message = message
        self.day = day
        self.kills = kills

    def killed_by(self, other, day):
        """
        Sets the elimination day for the player and increments kill
        counter of opponent.

        Args:
            other (Player): Opponent player.
            day (str): Day of the elimination.
        """
        other.kills = str(int(other.kills) + 1)
        self.day = day

    def __str__(self):
        return self.name

    def __iter__(self):
        return iter([self.name, self.message, self.day, self.kills])


class War:
    def __init__(self, file_name):
        """
        War data.

        Args:
            file_name (str): Path to the CSV file with the war data.

        Attributes:
            file_name (str): Path to the CSV file with the war data.
            players (list of Player): Total set of players.
            active (list of Player): Total set of alive players.
        """
        self.file_name = file_name
        self.players = []
        self.active = []

        # Reading csv file
        with open(file_name) as file:
            data = csv.DictReader(file, delimiter=',')
            for player in data:
                p = Player(player['name'], player['message'], player['day'], player['kills'])
                self.players.append(p)
                # If date of death is '0' the player is alive
                if player['day'] == '0':
                    self.active.append(p)
        # Current day is the maximum value of the dates of death
        self.day = max([int(p.day) for p in self.players])
        # Saving file to backup data
        copyfile(file_name, '{}_{}.csv'.format(file_name.split('.')[0], str(self.day)))

    def attack(self):
        """
        Eliminates a player and creates a message explaining the movement.

        Returns:
            (str): Message with the info of the winner / loser and the remaining
            players (if there are more than one) or a greeting message for the winner.
            In case there is only one player left it returns None.
        """
        # Checking if there are enough alive players to fight
        if len(self.active) == 1:
            return None

        # Increasing day before attack
        self.day = str(int(self.day) + 1)
        # Selecting two opponents from the alive players
        choice = np.random.choice(len(self.active), 2, replace=False)
        winner = self.active[choice[0]]
        loser = self.active[choice[1]]
        loser.killed_by(winner, self.day)

        # Popping loser player from array
        self.active.pop(choice[1])

        message = 'Día {}: {} {} {}. {} ha sido derrotado. '.format(self.day, winner, winner.message, loser, loser)
        if len(self.active) == 1:
            message += '¡{} ha ganado la partida!'.format(winner)
        else:
            message += 'Quedan {} jugadores'.format(len(self.active))
        return message

    def save_state(self):
        """
        Updates war information in the csv file.
        """
        with open(self.file_name, 'w') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(['name', 'message', 'day', 'kills'])
            for player in self.players:
                writer.writerow(list(player))

    def image(self, path, rows):
        """
        Generates an image with the list of players. Dead player will
        appear in red, alive players in bold black.

        Args:
            path (str): Path where the image will be stored.
        """
        w = 25 + 325 * int(np.ceil((len(self.players) / rows)))
        img = np.zeros((1080, w, 3))
        img[:] = (255, 255, 255)

        for i, player in enumerate(self.players):
            col = int(i / rows)
            width = col * 325 + 30
            jump = 1000 / rows
            height = int(i % rows * jump) + int(720 / rows)
            color = (0, 0, 0) if player in self.active else (0, 0, 255)
            thickness = 3 if player in self.active else 2
            cv.putText(img, player.name, (width, height), cv.FONT_HERSHEY_SIMPLEX, 1, color, thickness=thickness)

        cv.imwrite(path, img)


if __name__ == '__main__':
    w = War('data/war_data.csv')
    ret = w.attack()
    print(ret)
    w.save_state()
    w.image('output.jpg', 6)
