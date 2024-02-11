import os
import argparse
import goldsrcmap as gsm 

from kz_entities import Timer, Bhop

FGD_VERSION = "1.0"

def main(map_file, version):
	
	# Variables
	m = gsm.load_map(map_file)
	new_entities = []
	
	# Translate the kz entities into compatible entities for the engine
	# and generate new entities
	for entity in m.entities:
		if entity.classname in ['kz_start_button', 'kz_end_button']:
			Timer.func_button(entity)

		elif entity.classname in ['kz_start_zone', 'kz_stop_zone']:
			new_entities.append(Timer.zones(entity))
		
		elif entity.classname in ['kz_bhop']:
			Bhop.func_door(entity)

	# Adding entities
	m.add_entity(new_entities)

	# Save modified map
	base_name, _ = os.path.splitext(os.path.basename(map_file))
	output_file = f"{base_name}.map"
	m.worldspawn['kz_fgd_version'] = version
	gsm.save_map(m, output_file)


if __name__ == "__main__":
	print(f'KZ Mapping FGD v{FGD_VERSION}')
	parser = argparse.ArgumentParser(description=f"KZ Mapping FGD {FGD_VERSION}")
	parser.add_argument("map_file", help="Path to the input .map file")
	args = parser.parse_args()
	main(args.map_file, FGD_VERSION)
	print('__________________________________________')