#!/usr/bin/env python
# # -*- coding: utf-8 -*-

from pyknow import *
import sys

"""
    Sistema experto para detectar si una persona sufre de diabetes
    @author: Hector Morales Cod:1113624878. 
    Grupo: 90169_21

    Material Consultado
    
        * http://www. Cod.org/quoi-faire-si-mon-enfant-a-le-diabete/
        * http://www.nospetitsmangeurs.org/les-hauts-et-les-bas-du-taux-de-sucre/
        * http://www.childrenshospital.org/conditions-and-treatments/conditions/hypoglycemia-and-low-blood-sugar/symptoms-and-causes
        * https://www.mayoclinic.org/diseases-conditions/hyperglycemia/symptoms-causes/syc-20373631
"""


class Paciente(Fact):
    """Informacion acerca del paciente"""
    pass


def SUMA_CAMPOS(p, *campos):
    return sum([p.get(x, 0) for x in campos])


class InreferenceEngine(KnowledgeEngine):
    @Rule(Paciente(edad=P(lambda x: x <= 50)))
    def paciente_candidato(self):
        self.declare(Fact(candidato=True))

    @Rule(Fact(candidato=True),
          Paciente(glicemia=MATCH.glicemia))
    def hiperglicemia(self, glicemia):
        if glicemia > 10:
            self.declare(Fact(riesgo_hiperglicemico=True))
            print("Alerta! Alto nivel de azucar en la sangre!")
        else:
            self.declare(Fact(riesgo_hiperglicemico=False))

    @Rule(Fact(candidato=True),
          Paciente(glicemia=MATCH.glicemia))
    def hipoglicemia(self, glicemia):
        if glicemia < 4:
            print("Alerta! Bajo nivel de azucar en la sangre!")
            self.declare(Fact(riesgo_hipoglicemico=True))
        else:
            self.declare(Fact(riesgo_hipoglicemico=False))

    @Rule(Fact(candidato=True),
          AS.p << Paciente(),
          TEST(lambda p: SUMA_CAMPOS(p,
                                   'temblores',
                                   'hambre',
                                   'sudoracion',
                                   'jaqueca',
                                   'palidez') > 2))
    def tiene_signos_azucar_bajo(self, p):
        self.declare(Fact(tiene_signos_azucar_bajo=True))


    # If the patient is a child and has one or many signes or his blood sugar level is low
    @Rule(Fact(candidato=True),
          Fact(tiene_padres_diabeticos=True),
          Fact(tiene_signos_azucar_bajo=True))
    def protocolo_riesgo_bajo(self):
        print("Peligro! Paciente puede ser diabetico!")

    # If the patient is a child and has one or many signes, and his blood sugar level is low and passed the test
    @Rule(Fact(candidato=True),
          Fact(riesgo_hipoglicemico=True),
          Fact(tiene_signos_azucar_bajo=True))
    def protocolo_alerta_bajo(self):
        print("Alerta! Alto riesgo de diabetes, tu debes ver un doctor!")


    #If the patient is child and has at least one of his parents diabetic
    @Rule(Fact(candidato=True),
          Paciente(padres_diabeticos=True))
    def tiene_padres_diabeticos(self):
        self.declare(Fact(tiene_padres_diabeticos=True))


    @Rule(Fact(candidato=True),
          AS.p << Paciente(),
          TEST(lambda p: SUMA_CAMPOS(p,
                                   'miccion_frecuente',
                                   'sed',
                                   'vision_borrosa',
                                   'jaqueca',
                                   'boca_seca',
                                   'mal_aliento',
                                   'falta_de_aliento') > 2)
    )
    def tiene_signos_azucar_alto(self, **_):
        self.declare(Fact(tiene_signos_azucar_alto=True))

    @Rule(Fact(candidato=True),
          Fact(tiene_padres_diabeticos=True),
          Fact(tiene_signos_azucar_alto=True))
    def protocolo_riesgo_alto(self):
        print("Peligro! Paciente puede ser diabetico!")

    @Rule(Fact(candidato=True),
          Fact(riesgo_hiperglicemico=True),
          Fact(tiene_signos_azucar_alto=True))
    def protocolo_alerta_alto(self):
        print("Alerta! Alto riesgo de diabetes, tu debes ver un doctor!")


engine = InreferenceEngine()
engine.reset()

# Datos Iniciales

# datos del enfermo
# engine.declare(Paciente(edad= int(sys.argv[1]),
#                         glicemia=int(sys.argv[2]),
#                         temblores= bool(sys.argv[3]),
#                         hambre= bool(sys.argv[4]),
#                         sudoracion= bool(sys.argv[5]),
#                         jaqueca= bool(sys.argv[6]),
#                         padres_diabeticos = bool(sys.argv[7]),
#                         palidez= bool(sys.argv[8]),
#                         miccion_frecuente = bool(sys.argv[9]),
#                         sed = bool(sys.argv[10]),
#                         vision_borrosa = bool(sys.argv[11]),
#                         boca_seca = bool(sys.argv[12]),
#                         mal_aliento = bool(sys.argv[13]),
#                         falta_de_aliento = bool(sys.argv[14]),
#                         ))

engine.declare(Paciente(edad=32,
                        glicemia=11,
                        temblores= False,
                        hambre= False,
                        sudoracion= False,
                        jaqueca= False,
                        padres_diabeticos = True,
                        palidez= False,
                        miccion_frecuente = True,
                        sed = True,
                        vision_borrosa = False,
                        boca_seca = True,
                        mal_aliento = False,
                        falta_de_aliento = False,
                        ))
engine.run()
