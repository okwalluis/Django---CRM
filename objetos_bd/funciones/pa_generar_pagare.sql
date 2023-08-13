CREATE OR REPLACE PROCEDURE public.pa_generar_pagare(IN p_cuota_id bigint)
 LANGUAGE plpgsql
AS $procedure$
-- autor: lolmedo
-- date: 22/07/2023
-- objetivo: Generar un pagare para una cuota determinada.
DECLARE
	r_cuota RECORD;
BEGIN
   for r_cuota in 
     select p.persona_id, q.id as cuota_id, q.monto_cuota, q.fecha_vencimiento
       from prestamos p join cuotas_prestamo q on p.id = q.prestamo_id 
      where q.id  = p_cuota_id
   loop
	insert into pagares(monto_pagare, fecha_emision, fecha_vencimiento , nombre_co_deudor , documento_co_deudor , direccion_co_deudor , cuota_id , persona_id)
	values(r_cuota.monto_cuota, CURRENT_DATE, r_cuota.fecha_vencimiento, null, null, null, r_cuota.cuota_id, r_cuota.persona_id)
	/*RETURNING id INTO v_pagare_id;*/;
   end loop;
END;
$procedure$
;
