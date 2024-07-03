import os
import string
import random

env_vars = [
	"AllUSERSPROFILE",
	"CommonProgramFiles",
	"CommonProgramW6432",
	"ComSpec",
	"PATHEXT",
	"ProgramData",
	"ProgramFiles",
	"ProgramW6432",
	"PUBLIC",
	"SystemDrive",
	"SystemRoot",
	"windir",
]

#Build out dictionary
env_mapping = {}
for character in string.printable:
	env_mapping[character] = {}
	for var in env_vars:
		value = os.getenv(var)
		if character in value:
			env_mapping[character][var] = []
			for i, c in enumerate(value):
				if character == c:
					env_mapping[character][var].append(i)

#map characters to environment variables
def envhide_obfuscate(string):
	obf_code = []
	for c in string:
		possible_vars = list(env_mapping[c].keys())
		if not possible_vars:
			obf_code.append(f'[char]{ord(c)}')
			continue

		chosen_var = random.choice(possible_vars)
		possible_indicies = env_mapping[c][chosen_var]
		#print(f"{chosen_var=}{possible_indicies=}")
		chosen_index = random.choice(possible_indicies)

		new_character = os.getenv(chosen_var)[chosen_index]
		pwsh_syntax = f'$env:{chosen_var}[{chosen_index}]'
		obf_code.append(pwsh_syntax)

	return obf_code

#Return powershell
def pwsh_obfuscate(string):
	iex = envhide_obfuscate('iex')
	pieces = envhide_obfuscate(string)
	iex_stage = f'({",".join(iex)} -Join ${random.randint(1,9999)})'
	payload_stage = f'({",".join(pieces)} -Join ${random.randint(1,9999)})'

	return f'& {iex_stage} {payload_stage}'

powershell_command = 'Write-Output 420'
print(pwsh_obfuscate(powershell_command))	
