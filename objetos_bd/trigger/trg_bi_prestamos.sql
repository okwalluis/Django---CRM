create trigger trg_bi_prestamos before
insert
    on
    public.prestamos for each row execute function fa_inicial_prestamos()