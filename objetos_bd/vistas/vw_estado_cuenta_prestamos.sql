CREATE OR REPLACE VIEW public.vw_estado_cuenta_prestamos
AS SELECT p.persona_id,
    pe.nombre::text || pe.apellido::text AS cliente,
    p.id,
    p.nro_prestamo,
    p.fecha,
    cp.nro_cuota,
    cp.fecha_vencimiento,
    cp.monto_cuota,
    cp.saldo_cuota,
    pa.fecha_pago,
    COALESCE(pa.monto_pago, 0::numeric) AS monto_pago,
    (cp.nro_cuota || '/'::text) || (( SELECT count(cp2.id) AS count
           FROM cuotas_prestamo cp2
          WHERE cp2.prestamo_id = p.id)) AS cuota_actual_total,
    sum(COALESCE(pa.monto_pago, 0::numeric)) OVER (PARTITION BY cp.id ORDER BY pa.fecha_pago ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS acumulado_pago,
    cp.monto_cuota - sum(COALESCE(pa.monto_pago, 0::numeric)) OVER (PARTITION BY cp.id ORDER BY pa.fecha_pago ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS saldo_actual,
    pa.id AS nro_pago
   FROM prestamos p
     JOIN personas pe ON p.persona_id = pe.id
     JOIN cuotas_prestamo cp ON p.id = cp.prestamo_id
     LEFT JOIN pagos pa ON cp.id = pa.cuota_id
  WHERE 1 = 1 AND p.estado_prestamo_id = 1;