import time
import random

print()
print('-' * 65)
print('A wild Jigglypuff appears!')
time.sleep(0.2)
print('You only have one Pokemon, Snorlax.')
time.sleep(0.2)
print('I choose you Snorlax!!!!!')
print()
time.sleep(0.2)

# Pokemon's HP
snorlax_hp = 200
jigglypuff_hp = 125

# Print out the starting HP
print('Pokemon HP')
time.sleep(0.2)
print('- Snorlax HP: ' + str(snorlax_hp))
time.sleep(0.2)
print('- Jigglypuff HP: ' + str(jigglypuff_hp))
time.sleep(0.2)
print()
time.sleep(0.2)

while snorlax_hp > 0 and jigglypuff_hp > 0:
	print('Battle Options:')
	time.sleep(0.2)
	print('- (1) Sleep Heal')
	time.sleep(0.2)
	print('- (2) Tackle')
	time.sleep(0.2)
	print('- (3) Roundhouse Kick')
	time.sleep(0.2)
	print('- (4) Hyperbeam')
	time.sleep(0.2)
	print('- (5) Capture')
	time.sleep(0.2)
	print('- (6) Run Away')
	your_move = input('Choose a move using the corresponding number: ')
	print()

	if your_move == '1':
		print('Snorlax uses Sleep Heal')
		snorlax_hp = snorlax_hp + 50
		print('Snorlax uses Sleep Heal, his HP increases to ' + str(snorlax_hp))
		time.sleep(0.2)
	elif your_move == '2':
		jigglypuff_hp = jigglypuff_hp - 25
		print('Snorlax uses Tackle and deals 25 damage to Jigglypuff!')
		time.sleep(0.2)
	elif your_move == '3':
		jigglypuff_hp = jigglypuff_hp - 10
		print('Snorlax uses Roundhouse Kick and deals 10 damage to Jigglypuff!')
		time.sleep(0.2)
	elif your_move == '4':
		jigglypuff_hp = jigglypuff_hp - 40
		print('Snorlax uses Hyperbeam and deals 40 damage to Jigglypuff!')
		time.sleep(0.2)
	elif your_move == '5':
		capture_roll = random.randint(0,125)
		if capture_roll > jigglypuff_hp:
			print('You have captured Jigglypuff!')
			break
		else:
			print('You have failed to capture Jigglypuff!')
	elif your_move == '6':
		run_roll = random.randint(1,2)
		run_roll = str(run_roll)
		if run_roll == '1':
			print('You ran away from Jigglypuff!')
			break
		else:
			print('Jigglypuff stopped you from running!')
	print()

	enemy_move = random.randint(1,2)
	enemy_move = str(enemy_move)

	if enemy_move == '1':
		snorlax_hp = snorlax_hp - 20
		jigglypuff_hp = jigglypuff_hp + 15
		print('Jigglypuff uses Drink Blood and deals 20 HP and restores 15 HP!')
		time.sleep(0.2)
	elif enemy_move == '2':
		snorlax_hp = snorlax_hp - 40
		print('Jigglypuff uses Breathe FIre and deals 40 HP!')
		time.sleep(0.2)
	print()

# No negative HP when killed
	if snorlax_hp < 0:
		snorlax_hp = 0
	if jigglypuff_hp < 0:
		jigglypuff_hp = 0

	print('Updated HP!')
	time.sleep(0.2)
	print('- Snorlax HP: ' + str(snorlax_hp))
	time.sleep(0.2)
	print('- Jigglypuff HP: ' + str(jigglypuff_hp))
	time.sleep(0.2)
	print()
	time.sleep(0.2)

if snorlax_hp == 0:
	print('You lost the battle! Snorlax has fainted!')
elif jigglypuff_hp == 0:
	jigglypuff_hp('You won the battle! Jigglypuff has fainted!')

