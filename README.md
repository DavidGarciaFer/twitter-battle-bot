# Twitter Battle Royale Bot

This project consists of a bot developed in Python, which allows the user to recreate a Battle Royale style war, publishing each update as a tweet. The game generates random fights between different people or characters, each fight will have a loser and a winner, losers will be eliminated for the next rounds. Game ends when there is only one player left.

Each time the main script is executed a tweet like the following will be published. An image with the updated list of players will be automatically generated. Eliminated players appear in a red font style:

<p align="center">
    <img alt="Tweet example" src="readme/tweet_example.png" width="350px">
</p>

## Getting Started

Before starting to customize the battle it is necessary to follow the next steps to get the copy of the bot up and running.

### Prerequisites

The project was developed using [Python 3.7.4](https://www.python.org/downloads/).

Requiered packages are:

* [Numpy](https://www.numpy.org/) (v 1.17.0) -  Used to create random choices from a list.
* [OpenCV](https://opencv.org/) (v 4.1.0.25) -  Image generation.
* [Tweepy](https://www.tweepy.org/) (v 3.8.0) - Library to handle Twitter API.

### Installing required packages

A simple way to get every package installed in your environment is using [pip](https://pypi.org/project/pip/) executing the following command in the project root.

```
pip3 install -r requirements.txt
```

## Customizing war data

### Tweet message

Every tweet published by the bot will follow the same format:

```
Day <number of current round>: <Winner name> <Winner message> <Loser name>. <Loser name> has been defeated. <Number of remaining players> players remaining.
```

Last tweet (when the last two players have the last fight) follows a similar format, changing the final message:

```
Day <number of current round>: <Winner name> <Winner message> <Loser name>. <Loser name> has been defeated. <Winner name> has won the game!
```

Tweet format can be modified editing [these lines of war.py](https://github.com/DavidGarciaFer/twitter-battle-bot/blob/d1d5444f4b5636e41dc1bb38f99876dbd508502e/war.py#L109-113).

### Player information file

A comma separated value file should be provided in order to generate the list of players and the message for each tweet. Each row in the file should follow the format ```name,message``` where ```name``` will represent player's name and ```message``` the message to be displayed in the tweet. 

```
Harry Potter,has called Hedwig to attack
Ron Weasley,has killed (unintentionally)
Hermione Granger,has managed to get rid of
```

An [example file](data/harry_potter.txt) is provided for testing purposes, with *Harry Potter* characters.

## Generating war data

Once you have set the name and messages for the player you can generate the data file which the bot will use to generate tweets. It can be donde by executing the script called [generate_dataset.py](generate_dataset.py).

```
python3 generate_dataset.py <file_name>
```

For example, to use the *Harry Potter* example file we type:

```
python3 generate_dataset.py data/harry_potter.txt
```

A file will appear in the ```data``` directory called ```war_data.csv```. This file will contain different information, as the name, message, date of death and number of kills for each player, with the following format:

```
name,message,day,kills
name1,msg1,d1,k1
...
```

For example:

```
name,message,day,kills
Harry Potter,has called Hedwig to attack,0,2
Ron Weasley,has killed (unintentionally),3,0
Hermione Granger,has managed to get rid of,1,1
```

### Restore old data

You can easily restart the game at any desired point. The file ```war_data.csv``` is the one that the bot will take into account to generate the next elimination, so you can replace it at any time. Also, a backup file is generated after each tweet is published, so after the n-th tweet a file called ```war_data_<n-1>.csv``` will be generated (in the data directory) storing previous values, so if you want to rewind the game one turn just rename the last of this files to ```war_data.csv```.

## Running tests

Once ```war_data.csv``` is generated you can run the test included in war.py by executing:
```
python3 war.py
```
Tweet's message should appear on screen. Check if the image has been correctly generated in the file ```output.jpg```, you can change the number of rows per column [by changing this variable on the tests](https://github.com/DavidGarciaFer/twitter-battle-bot/blob/master/war.py#L155) and, once you have find a fine value change the definitive value [here](https://github.com/DavidGarciaFer/twitter-battle-bot/blob/master/bot.py#L9). 

You can try this command as many times as you wish, but nothing will appear on Twitter until you double check next step.

## Setting up Twitter API

First of all you will need a [Twitter developer account](https://developer.twitter.com/en/apply-for-access). Just fill the application (check Hobbyist -> Making a bot). Once your developer account is ready just create an App, and fill [this lines](https://github.com/DavidGarciaFer/twitter-battle-bot/blob/master/bot.py#L19) with your keys.

Now everything is ready! Run the next command to see your first tweet published!

```
python3 bot.py
```

## How to automate the execution

There are different forms to automate the execution in a determined time period. I use ```crontab```. Check [this tutorial](https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/) to see how it works. For example, if I want to publish a tweet at the start of every hour type in your ```crontab``` file:

```
0 * * * * python3 <path to the repository>/twitter-battle-bot/bot.py
```

## Authors

* [David García Fernández](https://github.com/DavidGarciaFer) - *Initial work* - Personal blog: [davidgarciafer.github.io](https://davidgarciafer.github.io)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* This bot is inspired in the twitter account [@spanishwarbot](https://twitter.com/spanishwarbot).
