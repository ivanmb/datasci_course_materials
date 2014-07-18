select count(*) from (
	select distinct t.docid from
		(select docid from frequency where term = 'transaction') t,
		(select docid from frequency where term = 'world') w
	where t.docid = w.docid
) x;
