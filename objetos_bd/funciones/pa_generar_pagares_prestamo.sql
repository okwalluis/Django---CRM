CREATE OR REPLACE PROCEDURE public.pa_generar_pagares_prestamo(IN p_prestamo_id bigint)
 LANGUAGE plpgsql
AS $procedure$
DECLARE
	r_cuota RECORD;
BEGIN
   for r_cuota in 
     select p.persona_id, q.id as cuota_id, q.monto_cuota, q.fecha_vencimiento
       from prestamos p join cuotas_prestamo q on p.id = q.prestamo_id 
      where p.id  = p_prestamo_id
      order by q.nro_cuota asc
   loop
	insert into pagares(monto_pagare, fecha_emision, fecha_vencimiento , nombre_co_deudor , documento_co_deudor , direccion_co_deudor , cuota_id , persona_id)
	values(r_cuota.monto_cuota, CURRENT_DATE, r_cuota.fecha_vencimiento, null, null, null, r_cuota.cuota_id, r_cuota.persona_id)
	/*RETURNING id INTO v_pagare_id;*/;
   end loop;
END;
$procedure$
;
