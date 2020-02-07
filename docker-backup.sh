#!/bin/bash
echo 'Running docker backup'
echo 'Exporting .sql file'
docker-compose exec db pg_dump -U postgres -h localhost postgres >> backup.sql
echo 'Archiving database to zip file'
zip backup.sql database.zip