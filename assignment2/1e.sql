select count(*) from (
	select docid from frequency group by docid having sum(count) > 300
) x;
