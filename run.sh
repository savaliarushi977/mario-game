#!/bin/bash

echo "🎮 Starting Super Mario Game..."
echo ""

# Check if Python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Error: Python3 is not installed"
    echo "Please install Python3 first"
    exit 1
fi

# Check if Pygame is installed
if ! python3 -c "import pygame" &> /dev/null
then
    echo "📦 Pygame not found. Installing..."
    pip install pygame
    echo ""
fi

# Run the game
python3 mario_game.py
