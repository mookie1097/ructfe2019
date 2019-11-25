wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update
sudo apt-get install google-chrome-stable

CHROMEDRIVER_VERSION=`curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE`
CHROMEDRIVER_ARCH=linux64
echo $CHROMEDRIVER_ARCH
wget https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_${CHROMEDRIVER_ARCH}.zip

unzip chromedriver_${CHROMEDRIVER_ARCH}.zip
mv chromedriver env/bin/
rm chromedriver_*.zip