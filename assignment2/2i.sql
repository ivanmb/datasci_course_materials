CREATE VIEW frequency_query AS 
    SELECT * FROM frequency
	UNION
	SELECT 'q' as docid, 'washington' as term, 1 as count 
	UNION
	SELECT 'q' as docid, 'taxes' as term, 1 as count
	UNION 
	SELECT 'q' as docid, 'treasury' as term, 1 as count;

select MAX(similarity) from (
	select Bdocid, SUM(value) similarity from (
		select A.docid Adocid, B.docid Bdocid, SUM(A.count*B.count) as value
		from frequency_query A, frequency_query B
		where A.term = B.term -- Join column to column because it's transposed
			--and a.docid < B.docid -- Optimization for simetrical matrix
			and A.docid = 'q'
		group by B.docid, B.term
	) x
	group by Bdocid
) distances;
