# rstorer
Request a bunch of URLs provided and stores the response in different files and folders.

This is a simple python tool which request new URl without waiting for the resposne of the last request and stores the response in a folder. But this can be hard on system resources.

# Usage
<pre><code>
usage: rstorer.py [-h] [-u] [-l] [-p] [-o]

Response Storer Tool

options:
  -h, --help      show this help message and exit
  -u , --url      enter the URL (URL should be provided in proper format)
  -l , --list     enter the path to file of list of URLs
  -p , --proxy    enter the proxy URL
  -o , --output   enter the folder name to save the output
</code></pre>
