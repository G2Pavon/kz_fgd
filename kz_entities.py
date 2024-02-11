from copy import deepcopy


class Timer():
	"""
	Convert timer related entities to compatible entity for plugins and timercounter
	"""
	@staticmethod
	def func_button(entity):
		entity['classname'] = 'func_button'

	@staticmethod
	def zones(entity):
		if entity.classname == 'kz_start_zone':
			entity['classname'] = 'trigger_multiple'
			start_zone = deepcopy(entity)
			start_zone.brushes[0].set_texture('NULL')
			start_zone.properties.clear()
			start_zone.properties = {
				"classname" : "func_button",
				"master" : "power",
				"targetname" : "counter_start_button",
				"target" : "counter_start",
				"spawnflags" : "256",
				"zhlt_invisible" : "1",
				"zhlt_noclip" : "1"
			}
			return start_zone
		else:
			entity['classname'] = 'trigger_multiple'
			stop_zone = deepcopy(entity)
			stop_zone.brushes[0].set_texture('NULL')
			stop_zone.properties.clear()
			stop_zone.properties = {
				"classname" : "func_button",
				"master" : "stopsource",
				"targetname" : "counter_stop_button",
				"target" : "counter_off",
				"spawnflags" : "256",
				"zhlt_invisible" : "1",
				"zhlt_noclip" : "1"
			}
			return stop_zone
		
class Bhop():
	"""
	Convert bhop related entities to func_door
	"""
	@staticmethod
	def func_door(bhop):
		bhop['classname'] = 'func_door'
		direction = bhop['direction'] 
		if direction != '0':

			# Down -Z
			if direction == '1': 
				bhop['angles'] = '90 0 0'
			# Rigth +X
			elif direction == '2':
				bhop['angles'] = '0 0 0'
			# Left -X
			elif direction == '3': 
				bhop['angles'] = '0 180 0'
			# Forward +Y
			elif direction == '4':
				bhop['angles'] = '0 90 0'
			# Backward -Y
			elif direction == '5': 
				bhop['angles'] = '90 0 0'
			# Up +Z
			elif direction == '6':
				bhop['angles'] = '-90 0 0'

		if bhop['onlyduck'] == '1' and bhop['onlystand'] == '1':
			pass
		elif bhop['onlyduck'] == '1':
			pass
				
		elif bhop['onlystand'] == '1':
			pass