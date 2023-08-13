CREATE OR REPLACE FUNCTION public.fa_bloquear_delete_tipospersona()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
BEGIN
  RAISE EXCEPTION 'No se puede eliminar el registro de tipos_persona. Consultar con administrador de Sistemas.';
  RETURN OLD;
END;
$function$
;
