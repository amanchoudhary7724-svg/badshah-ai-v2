@echo off
if not exist exports mkdir exports
powershell Compress-Archive -Path * -DestinationPath exports\repo_backup_before_migration.zip -Force
echo Backup created: exports\repo_backup_before_migration.zip
pause
