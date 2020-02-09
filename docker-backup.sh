#!/bin/bash
echo 'Running docker backup'
cd /Users/dstrants/Documents/Projects/backups/
echo 'Exporting .sql file'
docker-compose exec db pg_dump -U postgres -h localhost postgres >> backups.sql
echo 'Archiving database to zip file'
zip -u backup.zip backups.sql
cd -
python backup.py