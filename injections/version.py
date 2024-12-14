#  _     _ _    _            __                                             _    
# | |__ (_) | _| | ____ _   / _|_ __ __ _ _ __ ___   _____      _____  _ __| | __
# | '_ \| | |/ / |/ / _` | | |_| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
# | | | | |   <|   < (_| | |  _| | | (_| | | | | | |  __/\ V  V / (_) | |  |   < 
# |_| |_|_|_|\_\_|\_\__,_| |_| |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\
#                                                                               
# description: change your version to 9.9.9
# version: 1.0.0
# author: hikka framework

__version__ = (9, 9, 9)

import os

import git

try:
    branch = git.Repo(
        path=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    ).active_branch.name
except Exception:
    branch = "master"
