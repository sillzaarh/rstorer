# Response Storer
This is a simple python tool which request a bunch of URLs provided and stores the response in different files and folders. It requests new URL without waiting for the resposne of the last request and stores the response in a folder. But this can be hard on system resources.

# Usage
<pre><code>
<img src="https://github.com/mmbverse/rstorer/blob/main/uploads/rstorer%20demo.gif?raw=true" alt="rstorer demo" width="80%"/><br><br>
usage: rstorer.py [-h] [-u] [-l] [-p] [-o]

Response Storer

options:
  -h, --help      show this help message and exit
  -u , --url      enter the URL (URL should be provided in proper format)
  -l , --list     enter the path to file of list of URLs
  -p , --proxy    enter the proxy URL
  -o , --output   enter the folder name to save the output
</code></pre>

# Installation
Clone the repository
<pre><code>git clone https://github.com/mmbverse/rstorer.git
cd rstorer
</pre></code>
Python
<pre><code>pip install -r requirements.txt
python rstorer.py
</pre></code>
Bash
<pre><code>pip3 install -r requirements.txt
chmod +x rstorer.py

# copy to /usr/local/bin to access the tool from anywhere
sudo cp rstorer.py /usr/local/bin/rstorer
</pre></code>
