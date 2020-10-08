# ChatBot-ML

Development
-----------------------
> Developed using python packages such as keras, nltk over tensorflow. It can store the user's previous messgaes and replies accordingly.Need to train with more data inorder to work efficiently.

Installation
---------------------------
> 1. Clone this repo
> 2. **pip install requirements.txt**
> 3. Train the model by running below command
  > * change to app directory and run 
  > * python training.py
  > * All the required classes, words, models will be generated to trained-data folder
> 4. Running Server
  > * change to root directory and run
  > * **python server.py**
  > * Now the server is running at http://localhost:5000
  > * Check the response at http://localhost:5000/api/v1/resources?id=message&&user=name
> 5. Open **http://localhost:5000**
> 6. Enjoy chatting with bot
