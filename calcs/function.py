import math

def pipecalc(size, construction, length, inlet, outlet):

	length = float(length)
	inlet = float(inlet)
	outlet = float(outlet)

	d = size/100
	A = (math.pi*d**2)/4
	wp = math.pi*d
	R = A/wp
	if construction == 'concrete':
		n = 0.012
	elif construction == 'clayware':
		n = 0.014
	elif construction == 'brick':
		n = 0.025
	elif construction == 'corrugated metal':
		n = 0.022
	elif construction == 'UV CIPP liner':
		n = 0.01
	elif construction == 'HDPE plastic pipe':
		n = 0.011
	S = (inlet - outlet)/length
	pipecalc.Q = int((A*R**(2/3)*S**(0.5)/n))

def linercalc(size, shape, distance):

	distance = float(distance)
	d = size

	if d < 100 or d > 1200:
		linercalc.doc = 'FAILED: Size Unacceptable'
		linercalc.thickness = 0


	if distance < 0.9 or distance > 10.15:
		linercalc.doc = 'FAILED: Distance Unacceptable '
		linercalc.thickness = 'FAILED: '


	if d > 100 and d <= 200:
		if shape == 'circular':
			linercalc.doc = 'LNE/140154/EAR/DRG/IAB/002'
			linercalc.thickness = 6
		elif shape == 'non-circular':
			linercalc.doc = 'LNE/140154/EAR/DRG/IAB/013'
			linercalc.thickness = 6

	elif d > 200 and d <= 400:
		if shape == 'circular':
			if distance >= 0.9 and distance <= 5.65:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/003'
				linercalc.thickness = 8
			elif distance > 5.65 and distance <= 10.15:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/004'
				linercalc.thickness = 10
		elif shape == 'non-circular':
			if distance >= 0.9 and distance <= 3.9:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/013'
				linercalc.thickness = 6
			elif distance > 3.9 and distance <= 9.4:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/014'
				linercalc.thickness = 8
			elif distance > 9.4 and distance <= 10.15:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/015'
				linercalc.thickness = 10

	elif d > 400 and d <= 600:
		if shape == 'circular':
			if distance >= 0.9 and distance <= 2.65:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/004'
				linercalc.thickness = 10
			elif distance > 2.65 and distance <= 5.65:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/005'
				linercalc.thickness = 12
			elif distance > 5.65 and distance <= 8.9:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/006'
				linercalc.thickness = 14
			elif distance > 8.9 and distance <= 10.15:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/007'
				linercalc.thickness = 16
		elif shape == 'non-circular':
			if distance >= 0.9 and distance <= 1.9:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/014'
				linercalc.thickness = 8
			elif distance > 1.9 and distance <= 5.65:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/015'
				linercalc.thickness = 10
			elif distance > 5.65 and distance <= 9.4:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/016'
				linercalc.thickness = 12
			elif distance > 9.4 and distance <= 10.15:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/017'
				linercalc.thickness = 14

	elif d > 600 and d <= 800:
		if shape == 'circular':
			if distance >= 0.9 and distance <= 3.9:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/006'
				linercalc.thickness = 14
			elif distance > 3.9 and distance <= 5.65:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/007'
				linercalc.thickness = 16
			elif distance > 5.65 and distance <= 8.15:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/008'
				linercalc.thickness = 18
			elif distance > 8.15 and distance <= 10.15:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/009'
				linercalc.thickness = 20
		elif shape == 'non-circular':
			if distance >= 0.9 and distance <= 3.9:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/016'
				linercalc.thickness = 12
			elif distance > 3.9 and distance <= 6.4:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/017'
				linercalc.thickness = 14
			elif distance > 6.4 and distance <= 9.4:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/018'
				linercalc.thickness = 16
			elif distance > 9.4 and distance <= 10.15:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/019'
				linercalc.thickness = 18

	elif d > 800 and d <= 1000:
		if shape == 'circular':
			if distance >= 0.9 and distance <= 1.9:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/007'
				linercalc.thickness = 16
			elif distance > 1.9 and distance <= 3.9:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/008'
				linercalc.thickness = 18
			elif distance > 3.9 and distance <= 5.65:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/009'
				linercalc.thickness = 20
			elif distance > 5.65 and distance <= 7.65:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/010'
				linercalc.thickness = 22
			elif distance > 7.65 and distance <= 9.65:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/011'
				linercalc.thickness = 24
			else:
				linercalc.doc = 'n/a'
				linercalc.thickness = 0
		elif shape == 'non-circular':
			if distance >= 0.9 and distance <= 2.9:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/017'
				linercalc.thickness = 14
			elif distance > 2.9 and distance <= 4.9:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/018'
				linercalc.thickness = 16
			elif distance > 4.9 and distance <= 7.15:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/019'
				linercalc.thickness = 18
			elif distance > 7.15 and distance <= 9.4:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/020'
				linercalc.thickness = 20
			elif distance > 9.4 and distance <= 10.15:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/021'
				linercalc.thickness = 22

	elif d > 1000 and d <= 1200:
		if shape == 'circular':
			if distance >= 0.9 and distance <= 2.65:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/009'
				linercalc.thickness = 20
			elif distance > 2.65 and distance <= 4.15:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/010'
				linercalc.thickness = 22
			elif distance > 4.15 and distance <= 5.65:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/011'
				linercalc.thickness = 24
			else:
				linercalc.doc = 'n/a'
				linercalc.thickness = 0
		elif shape == 'non-circular':
			if distance >= 0.9 and distance <= 1.9:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/018'
				linercalc.thickness = 16
			elif distance > 1.9 and distance <= 3.9:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/019'
				linercalc.thickness = 18
			elif distance > 3.9 and distance <= 5.65:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/020'
				linercalc.thickness = 20
			elif distance > 5.65 and distance <= 7.4:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/021'
				linercalc.thickness = 22
			elif distance > 7.4 and distance <= 9.4:
				linercalc.doc = 'LNE/140154/EAR/DRG/IAB/022'
				linercalc.thickness = 24
			else:
				linercalc.doc = 'n/a'
				linercalc.thickness = 0

	# Proposed LINER diameter and internal diameter

	if linercalc.thickness > 0:
		linercalc.external = d
		linercalc.internal = linercalc.external - (2*linercalc.thickness)
	else:
		linercalc.external = 0
		linercalc.internal = 0




