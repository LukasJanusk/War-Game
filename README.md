# War-Game
Game rules:

1.Game has to be between 2 players. 
2.Player1 is human(program user)
3.Player2 is computer
4.Computer moves are calculated randomly(reading the rules of the game online suggests that there are no moves really)
5.Game ends when one player runs out of cards. Player without cards loses
6.Deck has 52 cards, each player gonna randomly draw 15 cards at the beggining of the game. 


Initial to do:

1. Create card class in separate file. each car will have name and value (unicode symbol optionaly). ex 10 value will be set for 10 of clubs card. Queen of hearts will have value of 12 etc. this way we will know which cards can take which.
2. Create class for player which will have two instances Human and Computer. Inside this class we can make a list for currently owned cards each. This way tracking current decks. 
3. Create game phases:
   a. draw from shuffled deck.<br>
   b. randomly decide player to go first.<br>
   c. drawing from players deck phase. Game loop starts here(optionally can make user type "draw" to initialize this         phase.<br>
   d. placing on table phase. We should type which cards have been placed. Here __str__ methind should work(optionaly        implement visuals how cards can be represented on table using unicode symbols)
   e. comparing phase<br>
   f. war phase if equal value cards have been placed and comparing again.(war according to wiki is one car face down        second is face up.<br>
   g. taking phase (whoever wins cards takes them to their current deck)<br>
   h. implement check for game end inside gameloop<br>
   i. game over message.<br>
   
   
   
