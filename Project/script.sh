#we retrieve the html link of marketwatch bitcoin prices
curl -s "https://www.marketwatch.com/investing/cryptocurrency/btceur" > btc.html

#we story the current timestamp in a local variable
timestamp=$(date +%Y-%m-%d-%H-%M)

#we retrieve the current bitcoin price threw marketwatch
price=$(cat btc.html | grep -oP '(?<="price":")[^"]*' | sed "s/,//")

#We stock the data retrieved in a csv file
echo "$timestamp,$price" >> btc.csv
