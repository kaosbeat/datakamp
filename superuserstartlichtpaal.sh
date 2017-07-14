#!/bin/sh
su pi -c "olad&"
su pi -c "cd ~/datakamp"
su pi -c "python LichtpaalReader.py&"
