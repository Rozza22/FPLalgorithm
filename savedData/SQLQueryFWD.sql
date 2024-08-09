use FPL
select * from CombinedDataWithRolling
where position != 'GK'
and expectedGsConcededHistory != '0.0'
--AND form != '0.0';
--where player_ID = 17
--order by round + 0 ASC;
