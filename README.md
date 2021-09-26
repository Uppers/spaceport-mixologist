# spaceport-mixologist
A game about a spaceport mixologist 

## Setup
This only works on Windows OS as far as I am aware. 

You will need to:
1. have pygame and the Algorand Python SDK installed:
   - `pip install pygame` 
   - `pip install py-algorand-sdk`

2. Set up an algorand node running the sandbox environment:
  - Github repo with setup instructions in readme: https://github.com/algorand/sandbox
  - Article explaining what it is: https://developer.algorand.org/articles/introducing-sandbox-20/
4. Clone the main branch of this repository 
5. If you are running the sandbox environment then there should be 3 accounts which are automatically set up for you, get the mnemonics for these accounts, and the public key for at least one of them. save these in a file called Transactions/private_info.py like so:

```
player = "5KLSI3AHMBBDALXBEO2HEA3PBBCBAYT4PIHCD3B25557WGWUZGRTQETPHQ"

account1_mnemonic = "carpet choice floor ... etc."
account2_mnemonic = "bottom divide magic ... etc."
player_mnemonic = "photo possible become ... etc."

algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
```
6. After you have done these things run main.py in the terminal <-- this will run the game for the first time and create a new ASA type in account 1

** At this stage the game should be running and you should see a menu page. If you proceed to play the game it will crash because you need to add your account public key in order to receive funds and also opt-in to the new ASA you just created for that account. If you click on the Create Player option you will see that there is an option available to add you account's public key however you will generate an error message if you have not opted in.** 

7. Close the game.
8. Run opt_in_script.py in the terminal <-- this will opt in the account listed in Transactions/private_info.py as "player"
9. Run main.py in the terminal. 
10. Navigate to the Create Player page, copy and paste in your player account details and press Submit & navigate back to the Main Menu
11. Play the game.  




