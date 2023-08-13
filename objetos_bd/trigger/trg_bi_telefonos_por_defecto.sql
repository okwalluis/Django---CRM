create trigger trg_bi_telefonos_por_defecto before
insert
    or
update
    on
    public.telefonos for each row execute function fa_controla_telefono_por_defecto()