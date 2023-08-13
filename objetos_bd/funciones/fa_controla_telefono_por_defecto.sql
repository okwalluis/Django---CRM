CREATE OR REPLACE FUNCTION public.fa_controla_telefono_por_defecto()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
DECLARE
  vcount numeric;
BEGIN
  IF TG_OP IN ('INSERT', 'UPDATE') THEN
    SELECT SUM(CASE WHEN por_defecto THEN 1 ELSE 0 END)
    INTO vcount
    FROM public.telefonos
    WHERE persona_id = new.persona_id;
    
    IF vcount > 1 THEN
      RAISE EXCEPTION 'Debe existir un solo teléfono por defecto para una persona';
    END IF;
  END IF;

  RETURN NEW;
END;
$function$
;
