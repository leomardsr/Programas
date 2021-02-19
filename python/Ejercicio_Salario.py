print ("Bienvenido al calculador de salario")

horas_trabajadas = float(input(" Ingrese las horas trabajadas durante esta semana: "))

salario_hora = float(input(" Ingrese el pago de su trabajo por horas: "))

salario_bruto= salario_hora*40

if horas_trabajadas > 40:

	horas_extras = horas_trabajadas - 40
	salario_extra = salario_hora*1.5
	salario_extra = salario_extra * horas_extras
	salario_total = salario_bruto+salario_extra
	
	print ("Su salario bruto es de: " )
	print (salario_bruto, "$ semanales")
	print (f"Usted ha trabajado {horas_extras} horas extras. Cada hora extra tiene un valor de 1.5 mas que las horas de trabajo normales")
	print (f"Por lo tanto, su salario para esta semana es de: {salario_total} $")

else:

	horas_trabajadas = 40 - horas_trabajadas
	salario_total = horas_trabajadas*salario_hora
	Print ("Su salario bruto es de: ", salario_bruto, "$ semanales")
	print ("Usted ha trabajado ", horas_trabajadas)
	print ("Su salario en esta semana sera de: ", salario_total)


