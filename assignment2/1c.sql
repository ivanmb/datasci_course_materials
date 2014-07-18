select count(*) from (
	select term from frequency where docId = '10398_txt_earn' and count = 1
	UNION
	select term from frequency where docId = '925_txt_trade' and count = 1
) x;
