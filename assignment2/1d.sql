select count(*) from (
	select count from frequency where term = 'parliament'
) x;
