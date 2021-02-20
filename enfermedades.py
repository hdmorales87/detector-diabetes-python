class enfermedad:
	def __init__(self,DIARREA,TOS,CANSANCIO,FIEBRE,DOLOR_MUSCULAR, NAUSEAS, ICTERICIA, APATIA, ESCALOFRIO, CEFALEA, SECRECION):
		self.DIARREA = DIARREA
		self.TOS = TOS
		self.CANSANCIO = CANSANCIO
		self.FIEBRE = FIEBRE
		self.DOLOR_MUSCULAR = DOLOR_MUSCULAR
		self.NAUSEAS = NAUSEAS
		self.ICTERICIA = ICTERICIA
		self.APATIA = APATIA
		self.ESCALOFRIO = ESCALOFRIO 
		self.CEFALEA = CEFALEA
		self.SECRECION = SECRECION
		self.ENFERMEDAD = ENFERMEDAD


listaSintomas = []
listaSintomas.append(enfermedad('TOS=0','CANSANCIO=0','FIEBRE=0','DOLOR_MUSCULAR=0','GRIPA=0'))
listaSintomas.append(enfermedad('FIEBRE','ESCALOFRIO','CEFALEA','SECRECION','RUBEOLA'))
listaSintomas.append(enfermedad('DIARREA','FIEBRE','ICTERICIA','ESCALOFRIO','MALARIA'))
listaSintomas.append(enfermedad('DIARREA','NAUSEAS','ICTERICIA','HEPATITIS'))
listaSintomas.append(enfermedad('TOS','CANSANCIO','FIEBRE','ESCALOFRIO','TUBERCULOSIS'))
listaSintomas.append(enfermedad('CANSANCIO','NAUSEAS','APATIA','ANEMIA'))

DIARREA = INPUT('El paciente tiene DIARREA si, no:')
TOS = INPUT('El paciente tiene TOS si, no:')
CANSANCIO = INPUT('El paciente tiene CANSANCIO si, no:')
FIEBRE = INPUT('El paciente tiene FIEBRE si, no:')
DOLOR_MUSCULAR = INPUT('El paciente tiene DOLOR_MUSCULAR si, no:')
NAUSEAS = INPUT('El paciente tiene NAUSEAS si, no:')
ICTERICIA = INPUT('El paciente tiene ICTERICIA si, no:')
APATIA = INPUT('El paciente tiene APATIA si, no:')
ESCALOFRIO = INPUT('El paciente tiene ESCALOFRIO si, no:')
CEFALEA = INPUT('El paciente tiene diarrea CEFALEA, no:')
SECRECCION = INPUT('El paciente tiene diarrea SECRECCION, no:')

def puntaje(sintoma):
	valor = 0
	if str(sintoma.DIARREA) == int(str(diarrea).strip()):
		valor +=1
	if str(sintoma.TOS).upper() == str(tos).strip().upper():
		valor +=1
	if str(sintoma.CANSANCIO).upper() == str(cansancio).strip().upper():
		valor +=1
	if str(sintoma.FIEBRE).upper() == str(fiebre).strip().upper():
		valor +=1
	if str(sintoma.DOLOR_MUSCULAR).upper() == str(dolor_muscular).strip().upper():
		valor +=1
	if str(sintoma.NAUSEAS).upper() == str(nauseas).strip().upper():
		valor +=1
	if str(sintoma.ICTERICIA).upper() == str(ictericia).strip().upper():
		valor +=1
	if str(sintoma.APATIA).upper() == str(apatia).strip().upper():
		valor +=1
	if str(sintoma.ESCALOFRIO).upper() == str(escalofiro).strip().upper():
		valor +=1
	if str(sintoma.CEFALEA).upper() == str(cefalea).strip().upper():
		valor +=1
	if str(sintoma.SECRECION).upper() == str(secrecion).strip().upper():
		valor +=1


listatemporal =[]
for index,sintomas in enumerate(listaSintomas):
	listatemporal.append([puntaje(sintomas),index])
listatemporal.sort(reverse=True)
print("SU ENFERMEDAD ES: ",listaSintomas[listatemporal[0][1]].ENFERMEDAD.upper())
exit(0)
