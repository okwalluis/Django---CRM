create trigger trg_bd_tipos_persona before
delete
    on
    public.tipos_persona for each row execute function fa_bloquear_delete_tipospersona()