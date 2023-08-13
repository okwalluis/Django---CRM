create trigger trg_ai_prestamos after
insert
    on
    public.prestamos for each row execute function fa_genera_cuotas_prestamo()