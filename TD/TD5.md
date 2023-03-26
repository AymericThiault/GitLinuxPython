__Exercise 1__

7 mkdir td4

8 cd td4

9 git init

10 sudo apt-get install python3-pip

11 pip3 install virtualenv

12 virtualenv -p python3 .env

13 ls -la

14 source .env/bin/activate

15 pip freeze

16 git status

17 touch .gitignore

18 echo ".env" >> .gitignore

19 echo "*.pyc" >> .gitignore

20 git status

21 git add .

22 git commit -m "initial commit"

23 git status

__Exercise 2__

26 pip install requests

27 touch domesday.py

28 nano domesday.py

29 ls

30 git add domesday.py

31 history > history10.md
