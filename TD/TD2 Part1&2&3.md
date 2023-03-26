__Part1__

__Exercise 1__

1  cd /

2  ls -l

3  grep bin | awk '{print $5}' | xargs stat -c '%y %n' | awk '{print $1, $2, $3, $6, $7}'

4  

5

6
