def water_lef(astronautas,agua_restante,dias_restante):
    for args in [astronautas,agua_restante,dias_restante]:
        try:
            #si el argumento es de tipo entero, la operacion se realizara sin errores
            args/10
        except TypeError:
            raise TypeError(f"Todos los argumentos deben de ser de tipo entero, pero se recibió '{args}'")

    uso_diario = astronautas * 11
    total_usado = uso_diario * dias_restante
    total_agua_restante = agua_restante - total_usado
    if total_agua_restante < 0:
        raise RuntimeError(f"No habrá suficiente agua para {astronautas} astronautas despues de {dias_restante} días !!!! ")
    return f"El agua restante despues de {dias_restante} días es : {total_agua_restante} litros"

print(water_lef("5",100,2))