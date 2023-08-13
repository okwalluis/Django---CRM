CREATE OR REPLACE FUNCTION public.fa_cancela_saldo_cuota()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
BEGIN
	if TG_OP = 'INSERT' then
		if new.monto_pago > 0 then
			update cuotas_prestamo 
			   set saldo_cuota = saldo_cuota - new.monto_pago,
			   	   saldo_interes = 0,
			   	   saldo_capital = 0,
			   	   fecha_ultimo_pago = new.fecha_pago
			 where id = new.cuota_id;
			RAISE NOTICE 'Se ha realizado un INSERT en la tabla "pagos".';
		ELSE
			RAISE EXCEPTION 'El valor del pago debe ser mayor a cero.';
		END IF;
	elsif TG_OP = 'UPDATE' then
		if new.monto_pago > 0 then
			update cuotas_prestamo 
			   set saldo_cuota = saldo_cuota + old.monto_pago - new.monto_pago,
			   	   saldo_interes = 0,
			   	   saldo_capital = 0,
			   	   fecha_ultimo_pago = new.fecha_pago
			 where id = new.cuota_id;
			RAISE NOTICE 'Se ha realizado un INSERT en la tabla "pagos".';
		else
			RAISE EXCEPTION 'El valor del pago debe ser mayor a cero.';
		end if;
	elsif TG_OP = 'DELETE' then
		if old.monto_pago > 0 then
			update cuotas_prestamo 
			   set saldo_cuota = saldo_cuota + old.monto_pago,
			   	   saldo_interes = monto_interes,
			   	   saldo_capital = monto_capital,
			   	   fecha_ultimo_pago = null
			 where id = old.cuota_id;
			RAISE NOTICE 'Se ha realizado un INSERT en la tabla "pagos".';
		else
			RAISE EXCEPTION 'El valor del pago debe ser mayor a cero.';
		end if;
	end if;

    RETURN NULL; -- Si es un disparador "BEFORE", se debe retornar NEW o NULL
END;
$function$
;
