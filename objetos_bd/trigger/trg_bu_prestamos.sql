create trigger trg_bu_prestamos before
update
    on
    public.prestamos for each row execute function fa_valida_cambioestado_prestamos()