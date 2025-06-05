# Healitics---Attack-Defense
Healitics is a role-based prompt engine which uses Gemini API to predict disease and suggest diagnostics. But the system and role prompt sometimes are seen as the developer's intellectual property. So in this project my target is to make an attack and defense module using reinforcement learning so that there be a race condition between them.
Through this race condition our main terget is to minimize the loss of prompt leakage (PLeak) through bypassing the attack.

Project structure
|----_pycache_/
|----data/
|     |--logs.csv
|     |--reward_curve.png
|----attack_module.py
|----defense_module.py
|----medical.py
|----model_factory.py
|----reinforcement_loop.py

In the defense module we have used logic of signature based defense and simple rejection to answer on leak detection.
In attack module we have used the logic of passing adversarial queries to the model for bypassing the defense.
The medical.py is the main ginipig here ie, this model will be examined by attack and defense modules.
We have to run >>python <directory>reinforcement_loop.py to get evaluation of accuracy of defending and loss through attacks.
