CREATE OR REPLACE FUNCTION public.fa_inicial_prestamos()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
declare 
	vnro_prestamo INT;
	vestado_prestamo INT := 1;
begin
	begin
		select MAX(nro_prestamo) into vnro_prestamo from prestamos;
	exception
		when no_data_found then
			vnro_prestamo := null;
	end;
	
	if vnro_prestamo is not null then
		vnro_prestamo := vnro_prestamo + 1;
	else
		vnro_prestamo := 1;
	end if;

	new.nro_prestamo := vnro_prestamo;
	new.estado_prestamo_id := vestado_prestamo; --ACTIVO

    RETURN NEW; -- Si es un disparador "BEFORE", se debe retornar NEW o NULL
END;
$function$
;
