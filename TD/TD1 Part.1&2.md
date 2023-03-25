// here is the commands history of my linux envirronement ( I didn't manage to retrieve the outputs )

__TD1.1__

__Exercise 1__

1  cd /

2  pwd

3  ls

4  mkdir test

5  cd home

6  cd /

7  pwd

8  sudo adduser athlt

9  cd athlt

10  cd home

11  cd athlt

12  cd ..

13  cd ~

14  pwd

15  mkdir test

16 cd home

17 cd home

18 cd ubuntu

19 cd linux_ex1

20 history > history5.md

16  cd test

17  pwd

18  history > history.md


__Exercise 2__


75  cd ubuntu

76  mkdir linux_ex_1

77  cd linux_ex_1

78  touch aymeric_thiault.txt

79  mv aymeric_thiault.txt aymeric_thiault_2023.txt

80  ls

81  mkdir notes

82  mv aymeric_thiault_2023.txt notes

83  ls

84  cd notes

85  ls

86  cd ..

87  cp notes notes_2023

88  cp -r  notes notes_2023

89  ls

90  rm -r -v notes

91  ls

92  history > history2.md


__Exercice 3__


98  linux_ex_1

99  cd linux_ex_1

100  ls

101  nano history2.md

102  ls

103  cd/linux_ex_1

104  cd linux_ex_1

105  touch script_1.ssh

106  nano script_1.ssh

107  cat script_1.ssh

108  sh script.ssh

109  mv script_1.ssh script_1.sh

110  cat script_1.ssh

111  cat script_1.sh

112  sh script.sh

113  sh script_1.sh

114  history > history3.md


__Exercice 4__

__4.1__

1 echo "name : blake" > credentials

2 cat credentials

3 ls -l credentials

4 chmod 444 credentials

5 ls -l credentials

6 echo "Age : 22" >> credentials

7 cat credentials

8 chmod 666 credentials

9 ls -l credentials

10 echo "Age : 22" >> credentials

11 cat creditentials

12 chmod u+x credentials

13 ls -l credentials

14 chmod o-r credentials

15 ls -l credentials

16 chmod 777 credentials

17 ls -l credentials

__4.2__

18 cd/

19 cd /

20 sudo su

21 echo "abc" > .private_file

22 cat .private_file

23 ls -a

24 sudoedit .private_file

25 cat .private_file

__4.3__

26 sudo chmod 666 .private_file

27 sudo chown athlt .private_file

28 chmod 666 .private_file

__4.4__

29 sudo apt update

30 sudo apt upgrade

31 sudo apt-install cmatrix

32 cmatrix

33 sudo apt-install tmux

34 tmux

35 echo "Hello Session 0"

36 cmatrix

37 tmux new

38 echo "Hello session 1"

39 tmux ls

40 tmux a -t 0

41 tmux a -t 1

42 tmux ls

43 tmux kill-server

44 tmux ls

__4.5__

45 camtrix --help

46 cmatrix -C white

47 cmatrix -u 6

48 cmatrix -u 6 -C blue

49 man cmatrix

50 tmux --help

51 man tmux

__TD1.2__

__Exercise 1__

52 sudo apt update

53 uname -a

54 top

55 nproc

56 lscpu | grep -i cache

57 df -h

58 mount | column -t

59 lsusb

60 hostname

__Exercise 2__

61 x="piri pimpin"

62 echo $x

63 x+=" piri pimpon"

64 echo $x

65 mkdir my_programs

66 cd my_programs

67 echo "pilou pilou" > pilou

68 bash pilou

69 chmod +x pilou

70 ./pilou

71 echo $PATH

72 export PATH=$PATH:$(pwd)

73 echo $PATH

74 cd ~

75 pilou

76 echo 'export PATH=$PATH:$(pwd)/my_programs' >> .profile

77 source .profile

78 pilou

__Exercise 3__

4 echo '#!/bin/bash' > say_hello.sh

5 echo 'echo "$(date "+%Y-%m-%d %H:%M:%S") Hello" >> hellos.txt' >> say_hello.sh

6 chmod +x say_hello.sh

7 echo '* * * * * /home/ubuntu/linux_ex_1/say_hello.sh' | crontab -

__Exercise 4__

8 mkdir hash_checksum

9 cd hash_checksum

10 touch .sensible_addresses

11 touch .sensible_passwords

12 ls

13 echo 'echo "Have a good day"' > gentle_script.sh

14 bash gentle_script.sh

15 sha256sum gentle_script.sh > log_sha

16 echo 'rm -f .sensible*' >> gentle_script.sh

17 sha256sum gentle_script.sh > log_sha

18 bash gentle_script.sh

19 ls

20 cat log_sha
 
