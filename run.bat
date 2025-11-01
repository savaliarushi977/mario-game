@echo off
echo Starting Super Mario Game...
echo.

python mario_game.py
if errorlevel 1 (
    python3 mario_game.py
)

pause
