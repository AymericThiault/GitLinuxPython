__Part1__

__Exercise 1__

1  cd /

2  ls -l

3  grep bin | awk '{print $5}' | xargs stat -c '%y %n' | awk '{print $1, $2, $3, $6, $7}'

4  curl https://en.wikipedia.org/wiki/List_of_cyberattacks |

5  grep "meta" |

6  grep -oP "(?<=meta )\w+" |

7  grep -A1 -P "mw-content-text.*A <a href=\"/wiki/Cyberattack\" title=\"Cyberattack\">cyberattack</a> is any type" |

8  grep -v "mw-content-text" |

9  grep -oP "(?<=<title>).*?(?= - Wikipedia</title>)" ; echo ""; 

10  echo "List of cyber attacks:"; 

11  grep -oP "(?<=<span class=\"mw-headline\" id=\")(.*?)(?=\")" cyberattacks.txt

12 history > history7.md
