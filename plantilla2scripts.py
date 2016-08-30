import sys
import os	

'''
	Crea los casos a simular a partir de una plantilla.
	Radios unicos para las particulas.
	Los scripts input que comparten las mismas proporciones de MgO y Al2O3
    se guardan en un mismo directorio.
'''

#############
# Variables #
#############

# Radios minimo y maximo considerados
Rmin_lab = 100 		# micras
Rmax_lab = 1500 	# micras

# Steps
prop_step = 5       # Paso porcentual en la proporcion de MgO en la mezcla
R_step = 200	    # Paso en micras entre radios considerados


##########################################
#   Experimentos con radios constantes   #
##########################################

# Crea la carpeta scripts donde se ordenaran los diferentes casos creados.
# Vacia su contenido por si acaso quedan casos generados anteriormente.
os.system("sudo mkdir scripts")
os.system("sudo rm -r ./scripts/*")

# Variacion de las proporciones en la mezcla
for percen_MgO in range(50,100+prop_step,prop_step):
	# Directorios para ordenar por proporciones
	os.system("sudo mkdir ./scripts/input_MgO-%.1f" % (percen_MgO))
	# Variacion del radio minimo de particula
	for Rmgo in range(Rmin_lab, Rmax_lab, R_step):
		# Variacion del radio maximo de particula
		for Ral2o3 in range(Rmin_lab, Rmax_lab, R_step):
			# quien tiene el menor radio
			Rmin = 0
			Rmax = 0
			if (Rmgo >= Ral2o3):
				Rmax = Rmgo
				Rmin = Ral2o3
			else:
				Rmax = Ral2o3
				Rmin = Rmgo

			# Carpetas para albergar la geometria y resultados de la simulacion
			os.system("sudo mkdir ./scripts/input_MgO-%.1f/Rmgo_%.0f_Ral2o3_%.0f" % (percen_MgO, Rmgo, Ral2o3))
			os.system("sudo cp -R ./meshes ./scripts/input_MgO-%.1f/Rmgo_%.0f_Ral2o3_%.0f/" % (percen_MgO, Rmgo, Ral2o3))
			os.system("sudo mkdir ./scripts/input_MgO-%.1f/Rmgo_%.0f_Ral2o3_%.0f/post" % (percen_MgO, Rmgo, Ral2o3))
			os.system("sudo chmod -R 777 ./scripts/")

			# Comando linux 'sed'(String EDitor)
			# Sustitucion de valores en in.plantilla1, in.plantilla2, in.plantilla3, in.plantilla4
			os.system("sed -e 's/VAR_percen_MgO/%.1f/g' -e 's/VAR_R_min/%.0f/g' -e 's/VAR_R_max/%.0f/g' \
			  -e 's/VAR_Rmgo/%.0f/g' -e 's/VAR_Ral2o3/%.0f/g' \
			  in.plantilla1 > scripts/%s/in1.MgO_%.1f_Rmgo_%.0f_Ral2o3_%.0f" % (percen_MgO,
			  Rmin, Rmax, Rmgo, Ral2o3, 'input_MgO-%.1f/Rmgo_%.0f_Ral2o3_%.0f' % (percen_MgO, Rmgo, Ral2o3), percen_MgO,
			  Rmgo, Ral2o3))
			os.system("sed -e 's/VAR_R_min/%.0f/g' in.plantilla2 > scripts/%s/in2.MgO_%.1f_Rmgo_%.0f_Ral2o3_%.0f" % (Rmin,
			  'input_MgO-%.1f/Rmgo_%.0f_Ral2o3_%.0f' % (percen_MgO, Rmgo, Ral2o3), percen_MgO, Rmgo, Ral2o3))
			os.system("sed -e 's/VAR_R_min/%.0f/g' in.plantilla3 > scripts/%s/in3.MgO_%.1f_Rmgo_%.0f_Ral2o3_%.0f" % (Rmin,
			  'input_MgO-%.1f/Rmgo_%.0f_Ral2o3_%.0f' % (percen_MgO, Rmgo, Ral2o3), percen_MgO, Rmgo, Ral2o3))
			os.system("sed -e 's/VAR_R_min/%.0f/g' in.plantilla4 > scripts/%s/in4.MgO_%.1f_Rmgo_%.0f_Ral2o3_%.0f" % (Rmin,
			  'input_MgO-%.1f/Rmgo_%.0f_Ral2o3_%.0f' % (percen_MgO, Rmgo, Ral2o3), percen_MgO, Rmgo, Ral2o3))

			# Genera archivos para la ejecucion de la simulacion completa
			#os.system("sudo cp ./ejecuta ./scripts/input_MgO-%.1f/Rmgo_%.0f_Ral2o3_%.0f/" % (percen_MgO, Rmgo, Ral2o3))
			os.system("sed -e 's/proporcion/%.1f/g' -e 's/radioMgO/%.0f/g' -e 's/radioAl2O3/%.0f/g' \
			  ./ejecuta > scripts/%s/ejecuta" % (percen_MgO, Rmgo, Ral2o3,
			  'input_MgO-%.1f/Rmgo_%.0f_Ral2o3_%.0f' % (percen_MgO, Rmgo, Ral2o3)))
