@echo off

:: This file is UTF-8 encoded, so we need to update the current code page while executing it
chcp 65001 > nul

:: variables
set "project-dir=%~dp0"
set "pyvenvcfg-path=%project-dir%venv\pyvenv.cfg"

setlocal enabledelayedexpansion
	:: getting python home dir from PATH
	for %%a in ("%path:;=";"%") do (
		set str=%%a
		set str1=!str:Python=!
		set str2=!str1:Scripts=!

		if not !str1! == %%a (
			if !str2! == !str1! (
				set pypath=%%a
				set pypath=!pypath:^"=!
			)
		)
	)

	set "search=PYHOME_PLACEHOLDER"
	set "replace=%pypath%"

	:: replacing paths
	for /f "delims=" %%a in ('type "%pyvenvcfg-path%" ^& break ^> "%pyvenvcfg-path%" ') do (
		set "line=%%a"
		>>%pyvenvcfg-path% echo(!line:%search%=%replace%!

	)
endlocal

:: startup
cd %project-dir%
@echo on
venv\Scripts\python.exe manage.py runserver

pause
