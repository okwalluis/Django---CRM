CREATE OR REPLACE FUNCTION public.fa_controla_direccion_por_defecto()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
declare
  vcount numeric;
begin
	if TG_OP in ('INSERT', 'UPDATE') then
		select count(1)
		  into vcount
		  from public.direcciones
		 where persona_id = new.persona_id
		   and por_defecto = true;
		  
		 if vcount > 0 then
			RAISE EXCEPTION 'Debe existir una sola dirección por defecto para una persona';
		 end if;
	end if;

    RETURN NEW; -- Si es un disparador "BEFORE", se debe retornar NEW o NULL
END;
$function$
;
