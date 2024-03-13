#!/bin/bash

MYSQL_USER="root"
MYSQL_PASSWORD="Godbless@"
MYSQL_HOST="localhost"

SQL_FILE="/home/eng/alx-higher_level_programming/0x0D-SQL_introduction"
echo "Listing all databases:"
mysql -h$MYSQL_HOST -u$MYSQL_USER -p$MYSQL_PASSWORD < $SQL_FILE
