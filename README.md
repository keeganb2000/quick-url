# QURL - short for 'Quick Url'

## Description
This tool allows you to launch a frequently used webpage through the command
line, or through Linux **i3's** `mod + d` function.

### Useage
qu followed by 'keyword argument'

Example : `qu jump`

### Creating your own keywords
Keywords are simply an identifier for the url you wish to associate with. New
keywords should be between 2 and 5 characters only, outside of this range will
not work in the tool.

To add your own keywords/url to the tool simply edit your local `qurl_url.csv`
file in the project folder and add a new lines. Below is an example line.
Keyword and urls are seperated by a comma.

`goog,https://www.google.com/`

### Bash File to Launch Tool
Create a bash script named `qu` and add the lines below. Best to store the
script in `~/bin`. Note that the line of code pointing to your qurl project
folder may differ to the example given.

#### Bash file contents

`#!/bin/bash ` <br />
`python3 ~/repos/qurl/__main__.py "$@"`

#### View keywords
If you forget your keywords you can quickly check them by running `qu list`

#### Existing keywords
`goog` : https://www.google.com/
