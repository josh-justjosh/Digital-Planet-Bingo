# Digital-Planet-Bingo
A simple python program to generate bingo boards containing common words, phrases and topics to use while listening to [BBC Digital Planet](https://www.bbc.co.uk/programmes/p002w6r2)

## Requirements:
- Just [Python](https://www.python.org/downloads/) *- I've tested the code in Python 3.8.5 but it should work in older versions*

## How to use:
1. Go to the [releases](https://github.com/josh-justjosh/Digital-Planet-Bingo/releases) page and download the latest zip file
2. Once downoaded extract the `Bingo Board Generator.py` file
3. Run the file
   - If the script opens in IDLE, press `F5` to start the programme 

### Once it's open:
- A bingo card will generate automatically
- Click on the words as you hear them in the show to check them off
- If you click on one by mistake, just click it again to clear it
- You can press `Generate New Card` to get a new bingo card with new words
- Or you can press `Clear Card` to reset the one you have

## A Note on Randomness
Each time the script generates the bingo card it shuffles the list of words. It then shuffles the list again before it allocates the first word in the list to the next empty space on the board. There are 180,503,769,600 possible boards so while I can't guarantee that you will not get the same board as some one else, or twice in a row - it's very unlikely.
