@echo off

set project_name=python_server
set module_name=apis

@REM ******************************************************
@REM create-project
@REM ******************************************************

echo "create django project %project%"
django-admin startproject %project_name%


cd %project_name%
echo "start django app %module_name%"
django-admin startapp %module_name%