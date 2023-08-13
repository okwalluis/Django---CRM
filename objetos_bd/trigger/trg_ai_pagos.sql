create trigger trg_ai_pagos after
insert
    or
delete
    or
update
    on
    public.pagos for each row execute function fa_cancela_saldo_cuota()