I'm going to re-implement echo in python

the goal is to write something that I could put at ~/bin/myecho
such that I couldn't tell the difference between if I used echo or myecho

known differences
* echo will interpret optional flags after the first non-optional flag as args (eg `echo yeet -e` will print `yeet -e` instead of interpreting -e as a flag)
* myecho doesn't have \\c or \\E as escape chars