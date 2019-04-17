#!/bin/bash
  
echo "content-type: text/html"
echo
echo
echo "<html> <head> <title> CGI script </title> </head>
<body>"
  
echo $QUERY_STRING 

echo "</body>"
echo "</html>"
