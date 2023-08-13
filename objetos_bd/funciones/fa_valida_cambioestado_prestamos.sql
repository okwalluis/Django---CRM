CREATE OR REPLACE FUNCTION public.fa_valida_cambioestado_prestamos()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
declare 
  vcount numeric := 0;
begin
	if new.estado_prestamo_id = 2 then -- estado de cancelado
		begin
			select count(1)
			  into vcount
			  from cuotas_prestamo q
			 where q.monto_cuota != q.saldo_cuota
			   and q.prestamo_id  = new.id;
		end;
		if vcount > 0 then
	  		RAISE EXCEPTION 'No se puede cambiar el estado del prestamo. Existen cuotas pagadas.';
	  	end if;
	end if;
  RETURN null;
END;
$function$
;
