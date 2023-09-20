@echo off

set project_name=python_server
set api_module=apis
set react_module=react

cd ..

django-admin startproject %project_name%

cd %project_name%
django-admin startapp %api_module%

django-admin startapp %react_module%