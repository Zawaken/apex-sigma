@echo off
set "VIRTENV_DIR=sigma.env"

virtualenv --python=C:\\Python35\\python.exe %VIRTENV_DIR%
%VIRTENV_DIR%\\Scripts\\activate.bat
pip install -r requirements.txt