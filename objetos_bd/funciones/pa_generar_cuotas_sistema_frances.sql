CREATE OR REPLACE PROCEDURE public.pa_generar_cuotas_sistema_frances(IN p_prestamo_id bigint, IN p_cantidad_cuotas integer, IN p_capital numeric, IN p_interes_anual double precision, IN p_fecha_primer_vencimiento date)
 LANGUAGE plpgsql
AS $procedure$
DECLARE
    v_fecha_vencimiento DATE;
    v_monto_cuota NUMERIC;
    v_monto_interes NUMERIC;
    v_monto_capital numeric := 0;
    v_saldo_cuota NUMERIC := p_capital;
    v_saldo_interes NUMERIC := 0;
    v_saldo_capital numeric := 0;
    v_nro_cuota INT := 1;
    -- convierto mi valor de interes a porcentaje.
    v_interes_anual numeric := p_interes_anual/100;
BEGIN
    -- Calcular el monto de la cuota y el monto del interés
    v_monto_cuota := p_capital * (v_interes_anual / 12) / (1 - POWER(1 + (v_interes_anual / 12), - p_cantidad_cuotas));
    v_monto_interes := v_saldo_cuota * (v_interes_anual / 12);
	v_monto_capital := v_monto_cuota - v_monto_interes;
	v_saldo_cuota := v_monto_cuota;
	v_saldo_interes := v_monto_interes;
	v_saldo_capital := p_capital;
    -- Generar las cuotas

	WHILE v_nro_cuota <= p_cantidad_cuotas LOOP
        -- Calcular la fecha de vencimiento de la cuota
        IF v_nro_cuota = 1 THEN
            v_fecha_vencimiento := p_fecha_primer_vencimiento;
        ELSE
            v_fecha_vencimiento := v_fecha_vencimiento + INTERVAL '1 month';
        END IF;

        -- Insertar la cuota en la tabla 
        INSERT INTO cuotas_prestamo(nro_cuota, fecha_vencimiento, monto_cuota, 
        							monto_interes, saldo_cuota, saldo_interes, 
        							prestamo_id, monto_capital, saldo_capital)
        					VALUES (v_nro_cuota, v_fecha_vencimiento, v_monto_cuota, 
        							v_monto_interes, v_monto_cuota, v_monto_interes, 
        							p_prestamo_id, v_monto_capital, v_monto_capital);

        -- Actualizar los saldos
      	v_saldo_capital := v_saldo_capital - v_monto_capital;
        --v_saldo_cuota := v_saldo_cuota - (v_monto_cuota - v_monto_interes);
        --v_saldo_interes := v_saldo_cuota * (p_interes_anual / 12);
       	--v_monto_cuota :=  v_saldo_capital * (p_interes_anual / 12 / (1 - POWER(1 + (p_interes_anual / 12), -p_cantidad_cuotas));
    	v_monto_interes := v_saldo_capital * (v_interes_anual / 12);
    	v_monto_capital := v_monto_cuota - v_monto_interes;

        -- Incrementar el número de cuota
        v_nro_cuota := v_nro_cuota + 1;
    END LOOP;
END;
$procedure$
;
